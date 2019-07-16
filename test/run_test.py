import population.main as main
import pandas as pd

p = main.load_params()
p['ext'] = 'svg'
sim = main.go_single_store_pop(p, store_from=190, over_ride=True)
pop_final = pd.concat(sim.pop_pd)
pop_final.to_csv('pop_output/pop_10_years.csv', index=False)
