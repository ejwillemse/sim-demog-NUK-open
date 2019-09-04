
import os
import pickle
import random

import population.experiment as ex

#import analyze_hh

def save_exp(ee, fname):
    print("Saving experiment...")
    ee.sim.P.flatten()
    pickle.dump(ee, open(fname, 'wb'), pickle.HIGHEST_PROTOCOL)
    ee.sim.P.lift()


def load_exp(fname):
    print("Loading simulation...")
    ee = pickle.load(open(fname, 'rb'))
    ee.sim.P.lift()
    return ee


def run_test1_1990(popsize_scale):
    e = ex.Experiment(param_file='../data/processed_dat/params_sg_y1990.cfg', store_iterations=[ i*1 for i in range(21) ])
    e.params['pop_size'] = int(round(e.params['pop_size']*popsize_scale))
    e.output_path = e.output_path.replace('/y', '/nonburn_{}_y'.format(str(popsize_scale)))
    e.prepare_simulation()
    e.run_sumulation()
    e.output_results()
    #save_exp(e, 'test_exp.experiment')


def run_test1_2000(popsize_scale):
    random.seed(100)
    random_seeds = [ random.randint(0, 1000000) for i in range(10) ]
    for seed in random_seeds:
        for p in range(11):
            pp = p*0.1
            print(pp)
            e = ex.Experiment(param_file='../../data/processed_dat/params_sg_y2000.cfg', store_iterations=[ i*1 for i in range(21) ])
            e.params['pop_size'] = int(round(e.params['pop_size']*popsize_scale))
            e.params['seed'] = seed
            e.params['leaving_prob'] = pp
            e.output_path = e.output_path.replace('/y', '/leaving_prob/leaving_prob_{:.1f}/nonburn_{}_s{}_y'.format(pp, str(popsize_scale), str(seed)))
            e.output_path = e.output_path.replace('_run_output', '../../sandbox/experiment_output/_run_output')
            #print(e.params.keys())
            if os.path.exists(e.output_path): continue
            e.prepare_simulation()
            e.run_sumulation()
            e.output_results()
            #save_exp(e, 'test_exp.experiment')


def run_test1_2010(popsize_scale):
    e = ex.Experiment(param_file='../data/processed_dat/params_sg_y2010.cfg', store_iterations=[ i*1 for i in range(21) ])
    e.params['pop_size'] = int(round(e.params['pop_size']*popsize_scale))
    e.output_path = e.output_path.replace('/y', '/nonburn_{}_y'.format(str(popsize_scale)))
    e.prepare_simulation()
    e.run_sumulation()
    e.output_results()
    #save_exp(e, 'test_exp.experiment')


def run_test2():
    e = load_exp('test_exp.experiment')
    sum_df, pop_py_df, pop_long_df, hh_long_df = e.get_results()
    print(sum_df.head())


if __name__ == '__main__':
    #print(os.listdir('../data/processed_dat'))
    import time
    t0 = time.time()
    print(t0)
    #run_test1_1990(popsize_scale=0.02)
    run_test1_2000(popsize_scale=0.005)
    #run_test1_2010(popsize_scale=0.02)
    t1 = time.time()
    #run_test2()
    print('done', 'run using time: {0:.3f}s'.format(t1-t0))
