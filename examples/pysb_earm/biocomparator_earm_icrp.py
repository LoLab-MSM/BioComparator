import numpy as np
import scipy
from earm.lopez_direct import model as direct
from earm.lopez_indirect import model as indirect
from earm.lopez_embedded import model as embedded
# Make a list of the models.

models = list([direct, indirect, embedded, smallest])
from biocomparator import BioComparator

exp_data = np.genfromtxt('EC-RP_IMS-RP_IC-RP_data_for_models.csv', delimiter=',', names=True)

# Build time points for the integrator, using the same time scale as the
# experimental data but with greater resolution to help the integrator converge.
ntimes = len(exp_data['Time'])
# Factor by which to increase time resolution
tmul = 10
# Do the sampling such that the original experimental timepoints can be
# extracted with a slice expression instead of requiring interpolation.
tspan = np.linspace(exp_data['Time'][0], exp_data['Time'][-1],
                    (ntimes-1) * tmul + 1)


integrator_options = {"rtol": 1e-6, "atol": 1e-6}
int_args = {'integrator': 'lsoda', 'integrator_options':integrator_options}

# Define a BioComparator custom cost function for the EARM IC-RP data.
def cost_icrp(model, sim):
    """Cost function for the IC-RP data.
    """
    # Get the total amount of Bid
    bid_tot = model.parameters['Bid_0'].value
    # Get mBid observable trajectory (this is the slice expression
    # mentioned above in the comment for tspan)
    bid_sim = sim['mBid'][::tmul]
    # Normalize it to 0-1
    bid_sim_norm = bid_sim / bid_tot
    # Get experimental measurement and variance
    bid_exp = exp_data['norm_ICRP']
    bid_exp_var = exp_data['nrm_var_ICRP']
    # Compute error between simulation and experiment
    e = np.sum((bid_exp - bid_sim_norm) ** 2 / (2 * bid_exp_var)) / len(bid_exp)
    return e

biocomp_icrp = BioComparator(models)
# Generate the PSO instances for this BioComparator instance.
biocomp_icrp.gen_pso(tspan, None,
                     pso_kwargs=dict({'save_sampled':False, 'verbose':True}),
                     solver_kwargs=int_args,
                     cost_type='custom',
                     custom_cost=cost_icrp,
                     swarm_params=None)

# run it
num_particles = 20
num_iterations = 20
optima_icrp = biocomp_icrp.run_pso(num_particles, num_iterations)

print("best: ")
print(optima_icrp)
