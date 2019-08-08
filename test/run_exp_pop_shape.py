
import pickle
import os
import population.experiment as ex


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


def run_test1():
    age_dist_files = sorted(os.listdir('data_files/test_age_shape'))
    age_dist_files = [ f for f in age_dist_files if f[-4:]=='.dat']
    for fname in age_dist_files[9:]:
        print(fname)
        e = ex.Experiment(param_file='params2.cfg', store_iterations=[ i*10 for i in range(21) ])
        e.params['age_distribution'] = 'test_age_shape/'+fname
        #e.params['prefix'] = 'data_files/test_age_shape/output/'+fname+'_'
        e.output_path = 'data_files/test_age_shape/output/'+fname
        e.prepare_simulation()
        e.run_sumulation()
        e.output_results()
        save_exp(e, os.path.join('data_files', 'test_age_shape', 'experiment', fname+'_test.exp'))


def run_test2():
    e = load_exp('test_exp.experiment')
    sum_df, pop_py_df, pop_long_df, hh_long_df = e.get_results()
    print(sum_df.head())


if __name__ == '__main__':
    run_test1()
    #run_test2()
    print('done')
