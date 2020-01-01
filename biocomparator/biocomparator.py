import numpy as np
import pandas as pd
import os
import shutil
import glob
import importlib
import warnings
import pysb

from swarm_it import SwarmIt

class BioComparator(object):
    """A model comparator based on model-selection methodologies using PSO-based optimization.

    Args:
        models (list of :obj:pysb.Model): A list PySB models to compare.

    Attributes:
        psos (list of :obj:): A list containing the PSO
            objects for each model. Must call the gen_pso function to build the
            optimizer instances.
        optima (pandas.DataFrame): The DataFrame containing the optimized
            model data, including their name, minimum cost, and best parameter
            vector. Only generated after calling
            the run_pso function.
        models

    """

    def __init__(self, models):
        """Inits BioComparator."""
        self.psos = None
        self._swarm_its = None
        self.optima = None
        self.models = models
        return

    def number_of_models(self):
        """Number of models being tested.

        Returns:
            int: The number of models.

        """
        return len(self.models)

    def gen_pso(self, timespan, observable_data,
                        solver=pysb.simulator.ScipyOdeSimulator,
                        solver_kwargs=None,
                        pso_kwargs=None,
                        cost_type='sse',
                        custom_cost=None,
                        swarm_params=None):
        """Generate the PSO objects for each model.

        The PSO object instances are stored in a list as the
        `psos` attribute.

        Args:
            timespan (numpy.array): The timespan for model simulations.
            observable_data (dict of tuple): Defines the observable data to
                use when computing the loglikelihood function. It is a dictionary
                keyed to the model Observables (or species names) that the
                data corresponds to. Each element is a 3 item tuple of format:
                (:numpy.array:data, None or :numpy.array:data_standard_deviations,
                None or :list like:time_idxs or :list like:time_mask).
            solver (:obj:): The ODE solver to use when running model simulations.
                Defaults to pysb.simulator.ScipyOdeSimulator.
            solver_kwargs (dict): Dictionary of optional keyword arguments to
                pass to the solver when it is initialized. Defaults to dict().
            pso_kwargs (dict): Dictionary of any additional optional keyword
                arguments to pass to PSO object constructor.
                If None, defaults to {'save_sampled':False, 'verbose':True}.
            log_likelihood_type (str): Define the type of loglikelihood estimator
                to use. Options are 'norm_logpdf'=>Compute the loglikelihood using
                the normal distribution estimator, 'mse'=>Compute the
                loglikelihood using the negative mean squared error estimator,
                'sse'=>Compute the loglikelihood using the negative sum of
                 squared errors estimator. Defaults to 'norm_logpdf'.

        Returns:
            None
        """
        if solver_kwargs is None:
            solver_kwargs = dict()
        if pso_kwargs is None:
            pso_kwargs = dict({'save_sampled':False, 'verbose':True})
        swarm_its = list()
        psos = list()
        for i,model in enumerate(self.models):
            swarm_param = None
            if swarm_params is not None:
                swarm_param = swarm_params[i]
            swarm_it = SwarmIt(model, observable_data, timespan,
                                       solver=solver,
                                       solver_kwargs=solver_kwargs,
                                       swarm_param=swarm_param)
            pso = swarm_it(pso_kwargs=pso_kwargs,
                           cost_type=cost_type, custom_cost=custom_cost)
            swarm_its.append(swarm_it)
            psos.append(pso)
        self._swarm_its = swarm_its
        self.psos = psos
        return

    def run_pso(self, num_particles=20, pso_iterations=50,
                pso_stop_threshold=1e-5, verbose=True):
        """Run PSO on each model.

        Returns:
            pandas.DataFrame: The models with their minimum cost and
                best parameter vector.

        """
        # nprocs = 1
        if self.psos is None:
            warnings.warn("Unable to run. Must call the 'gen_pso' function first!")
            return
        frame = list()
        for i in range(len(self.psos)):
            if verbose:
                print("Running PSO on model {}".format(self.models[i].name))
            self.psos[i].run(num_particles, pso_iterations,
                             stop_threshold=pso_stop_threshold)
            best = self.psos[i].best
            min_cost = self.psos[i].best.fitness.values[0]
            # print(min_cost)
            k = len(best)
            ML = -1. * min_cost
            data_d = dict()
            #data_d['model'] = "model_{}".format(i)
            data_d['model'] = self.models[i].name
            data_d['cost'] = min_cost
            data_d['AIC'] = self.akaike_ic(k, ML)
            #print(self._n_data())
            #data_d['BIC'] = self.bayesian_ic(k, ML, self._n_data())
            data_d['n_theta'] = k
            data_d['theta_best'] = best
            if verbose:
                print("model: {} cost: {} AIC: {} n_theta: {}".format(data_d['model'], data_d['cost'], data_d['AIC'], data_d['n_theta']))
            frame.append(data_d)
        #frame = list()
        #for i,pso in enumerate(self.psos):
        #    best = pso.best
        #    min_cost = pso.best.fitness.values[0]
        #    # print(min_cost)
        #    k = len(best)
        #    ML = -1. * min_cost
        #    data_d = dict()
        #    #data_d['model'] = "model_{}".format(i)
        #    data_d['model'] = self.models[i].name
        #    data_d['cost'] = min_cost
        #    data_d['AIC'] = self.akaike_ic(k, ML)
        #    #print(self._n_data())
        #    #data_d['BIC'] = self.bayesian_ic(k, ML, self._n_data())
        #    data_d['n_theta'] = k
        #    data_d['theta_best'] = best
        #    if verbose:
        #        print("model: {} cost: {} AIC: {} n_theta: {}".format(data_d['model'], data_d['cost'], data_d['AIC'], data_d['n_theta']))
        #    frame.append(data_d)
        optima = pd.DataFrame(frame)
        #selection.sort_values(by=['log_evidence'], ascending=False, inplace=True)
        self.optima = optima
        #return selection.reset_index(drop=True)
        return optima

    @staticmethod
    def akaike_ic(k, ML):
        return 2.*k - 2.*ML

    def _n_data(self):
        n_dat = 0
        obs_dat = self._swarm_its[0].observable_data
        for item in obs_dat:
            n_dat += len(obs_dat[item][0])
        return n_dat

    @staticmethod
    def bayesian_ic(k, ML, n_data):
        bic = np.log(n_data) * k - 2. * ML
        return bic
