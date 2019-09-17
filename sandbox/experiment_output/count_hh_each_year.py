import os
import pandas as pd
from tqdm import tqdm

basedirs = [ '_run_output_{}'.format(str(i)) for i in range(1, 4) ]
catdirs = ['couple_prob', 'divorce_prob', 'leaving_prob']


def counting(cat):
    for bdir in basedirs:
        pdirs = sorted(os.listdir(os.path.join(bdir, cat)))
        #print(pdirs)
        for pdir in tqdm(pdirs, desc='prob {}'.format(bdir)):
            p = float(pdir.split('_')[-1])
            sdirs = sorted(os.listdir(os.path.join(bdir, cat, pdir)))
            #print(sdirs)
            for sdir in sdirs:
                seed = sdir.split('_')[-2]
                fpout = os.path.join(bdir, cat, pdir, sdir, 'summary_household.csv.xz')
                if os.path.exists(fpout): continue
                #print(seed)
                fp = os.path.join(bdir, cat, pdir, sdir, 'stored_household.csv.xz')
                df = pd.read_csv(fp, index_col=0)
                df = df.groupby('time')['household_id'].count().reset_index(name='no_household')
                df[cat] = p
                df['seed'] = seed
                df.to_csv(fpout, index_label='ind')


if __name__ == '__main__':
    for cat in catdirs:
        counting(cat)
