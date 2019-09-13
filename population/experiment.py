"""
A stub for testing/evaluating dynamic demography simulations.
"""
# import default modules
import sys, os, time
from math import floor
from random import Random

# import dependent modules
import pandas as pd
from tqdm import tqdm

# import local modules
from .utils import parse_params, create_path
from .simulation import Simulation
from .individual import Individual
#from .data_processing_pop import *
#from .plotting_pop import *
#from .output_pop import *



class Experiment(object):
    def __init__(self, param_file='params.cfg', store_iterations=[]):
        #self.params_file = param_file
        self.store_iterations = store_iterations
        print('experiment store snapshots for these years: {}'.format(','.join([str(y) for y in store_iterations])))
        self.params = self._load_params(param_file)
        self.timesteps = self.params['years'] * floor(365.0/self.params['t_dur'])
        self.burn_steps = self.params['demo_burn'] * floor(365.0/self.params['t_dur'])
        self.sim_timesteps = self.timesteps - self.burn_steps


    def _load_params(self, param_file):
        print("Loading parameters...")
        #print(os.path.dirname(__file__))
        params = parse_params(param_file, os.path.join(
            os.path.dirname(__file__), 'paramspec_pop.cfg'))
        self.output_path = os.path.join(os.path.dirname(param_file), params['prefix'])
        params['resource_prefix'] = os.path.join(os.path.dirname(param_file), params['resource_prefix'])
        return params


    def set_new_seed(self, seed=None):
        if seed is None:
            seed = Random().randint(0, 99999999)
        self.params['seed'] = seed


    def prepare_simulation(self):
        print("Creating population...")
        self.sim = Simulation(self.params, ind_type=Individual, create_pop=True)


    def run_sumulation(self):
        print("Running simulation...")
        #print('\t'.join(['years', 'days', 'no. individuals', 'no. births', 'no. deaths', 'no. immigrants']))
        cols = ['years', 'days', 'no_individuals', 'no_births', 'no_deaths', 'no_immigrants']
        self.sum_dic = {}
        self.pop_py = []
        self.sim.start_time = time.time()
        for y in tqdm(range(self.timesteps), desc='Updating years'):
            is_burn = y<self.params['demo_burn']
            t = y * self.params['t_dur']
            # y=year, t=day
            b,d,im,bd = self.sim.update_all_demo(t, burn_flag=is_burn)
            #print('\t'.join([ str(x) for x in [i, t, len(sim.P.I), len(b), len(d), len(im)]]))
            vals=  [y, t, len(self.sim.P.I), len(b), len(d), len(im)]
            self.sum_dic[y] = { k:v for k,v in zip(cols, vals) }
            #sim.record_stats_demo(t)
            if y in self.store_iterations:
                self.sim.save_demog_stats(y)
                self.sim.save_population(y)
                self.sim.save_households(y)
        self.sim.end_time = time.time()
        print("Done running simulation...")


    def get_results(self):
        print("Getting results...")
        sum_df = pd.DataFrame.from_dict(self.sum_dic, orient='index')

        if len(self.store_iterations)>0:
            pop_py_df = self.sim.get_save_demog_stats()
            pop_long_df = self.sim.get_save_pop(level='individual')
            hh_long_df = self.sim.get_save_pop(level='household')
            #return sum_df, pop_py_df, pop_long_df, hh_long_df
        else:
            pop_py_df = None
            pop_long_df = None
            hh_long_df = None
            #return sum_df
        return sum_df, pop_py_df, pop_long_df, hh_long_df


    def output_results(self):
        create_path(self.output_path)
        create_path(os.path.join(self.output_path, 'thumbnails'))
        print("Exporting outputs to...", self.output_path)
        sum_df, pop_py_df, pop_long_df, hh_long_df = self.get_results()
        f0 = os.path.join(self.output_path, 'yearly_summary.csv.xz')
        f1 = os.path.join(self.output_path, 'stored_sex_age_stats.csv.xz')
        f2 = os.path.join(self.output_path, 'stored_population.csv.xz')
        f3 = os.path.join(self.output_path, 'stored_household.csv.xz')

        tables = [sum_df, pop_py_df, pop_long_df, hh_long_df]
        destinations = [f0, f1, f2, f3]
        for tab, des in zip(tables, destinations):
            tab.to_csv(des, index_label='ind', compression='xz')
