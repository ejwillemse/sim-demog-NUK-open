import population.experiment as ex
import pandas as pd

def run_test_1():
    p = ex.load_params(params_file='params.cfg')
    p['ext'] = 'svg'
    sim = ex.go_single_store_pop(p, store_from=190, over_ride=True)
    pop_final = pd.concat(sim.pop_pd)
    pop_final.to_csv('pop_output/pop_10_years.csv', index=False)


def run_test2():
    p = ex.load_params(params_file='params2.cfg')
    #for k,v in p.items():
    #    print(k, ':', v)
    sim, sum_df, pop_py_df, pop_long_df, hh_long_df = main.go_single_store_pop(p, store_from=199, over_ride=True)
    sum_df.to_csv('summary_df.csv', index_label='ind')
    pop_py_df.to_csv('population_pyramid_df.csv', index_label='ind')
    pop_long_df.to_csv('time_snapshots_population_df.csv', index_label='ind')
    hh_long_df.to_csv('time_snapshots_household_df.csv', index_label='ind')

if __name__ == '__main__':
    #run_test_1()
    run_test2()