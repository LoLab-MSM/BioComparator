"""
PSO run script for dimerization_model.py using swarm_it
classes.
"""
from grouped_reaction_models.model_0 import model as model_0
from grouped_reaction_models.model_1 import model as model_1
from grouped_reaction_models.model_2 import model as model_2
import numpy as np

from biocomparator.biocomparator import BioComparator

if __name__ == '__main__':
    # Initialize PySB solver object for running simulations.
    # Simulation timespan should match experimental data.
    # Load the data.
    data = np.load("model_0_AB_complex_data.npy")
    # The timespan of the simulations.
    tspan = np.linspace(0, 5, 20)
    # Define the fancy indexer or mask for the time points that the data
    # corresponds to. -- In this case it is the last ten (out of 20) time points.
    data_time_idxs = np.array(list(range(len(tspan))))[10:]

    # Setup the PSO run
    # Generate the observable data tuple for this observable: (data, data_sd, data_time_idxs)
    obs_data_t = tuple((data,None,data_time_idxs))
    # Generate the dictionary of observable data that is to be used in
    # computing the likelihood. -- Here we are just using the AB_complex
    # observable, which is the amount of A(B=1)%B(A=1).
    observable_data = dict()
    observable_data['AB_complex'] = obs_data_t
    # Initialize the GAlibrateIt instance with the model details.
    # swarmit = SwarmIt(model, observable_data, tspan, swarm_param=swarm_param)
    models = list([model_0, model_1, model_2])
    #swarm_params = list([swarm_param])
    biocomp = BioComparator(models)
    # Now build the GAO object. -- All inputs are
    # optional keyword arguments.
    biocomp.gen_pso(tspan, observable_data,
                    pso_kwargs=dict({'save_sampled':False, 'verbose':True}),
                    cost_type='sse',
                    swarm_params=None)

    # run it
    num_particles = 20
    num_iterations = 50
    optima = biocomp.run_pso(num_particles, num_iterations)
    print("best: ")
    print(optima)
