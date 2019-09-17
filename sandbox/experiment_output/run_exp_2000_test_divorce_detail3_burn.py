
import os
import pickle
import random
import time

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


def run_test1_2000(popsize_scale):
    random.seed(100)
    random_seeds = [ random.randint(0, 1000000) for i in range(10) ]
    for seed in random_seeds:
        for p in range(11):
            t0 = time.time()
            pp = p*0.001 + 0.000
            print(pp)
            #store_iterations = [ i*1 for i in range(21) ]
            store_iterations = [ i*10 for i in range(10) ] + [ i+100 for i in range(21) ]
            e = ex.Experiment(param_file='../../data/processed_dat/params_sg_y2000.cfg', store_iterations=store_iterations)
            e.params['pop_size'] = int(round(e.params['pop_size']*popsize_scale))
            e.params['seed'] = seed
            e.params['years'] = 121
            e.params['demo_burn'] = 100
            e.params['divorce_prob'] = pp
            e.output_path = e.output_path.replace('/y', '/divorce_prob/divorce_prob_{:.3f}/burned_{}_s{}_y'.format(pp, str(popsize_scale), str(seed)))
            e.output_path = e.output_path.replace('_run_output', '../../sandbox/experiment_output/_burned_run_output_3')
            #print(e.params.keys())
            if os.path.exists(e.output_path): continue
            e.prepare_simulation()
            e.run_sumulation()
            e.output_results()
            #save_exp(e, 'test_exp.experiment')
            t1 = time.time()
            print('run using time: {0:.3f}s'.format(t1-t0))


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
