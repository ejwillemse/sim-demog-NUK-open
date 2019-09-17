import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from tqdm import tqdm

def get_dfs(cat, target_file):
    ds = [1, 2, 3]
    #group_fs = { dd:{} for dd in ds }
    dfs = {1:None, 2:None, 3:None}
    for dd in ds:
        basedir = '_run_output_{}'.format(str(dd))
        pdirs = sorted(os.listdir(os.path.join(basedir, cat)))
        #print(pdirs)
        for pdir in pdirs:
            pset = pdir.split('_')[-1]
            #print(pset)
            seeds = sorted(os.listdir(os.path.join(basedir, cat, pdir)))
            #print(seeds)
            for sr in seeds:
                fp = os.path.join(basedir, cat, pdir, sr, target_file)
                #print(fp)
                seed = sr.split('_')[2]
                df = pd.read_csv(fp)
                df['prob'] = float(pset)
                df['seed'] = seed
                df['detail_level'] = dd
                df['both_age'] = df['male'] + df['female']
                df['age_group'] = [ int(a/5)*5 for a in df['age'] ]
                #print(df.head())
                if dfs[dd] is None:
                    dfs[dd] = df
                else:
                    dfs[dd] = dfs[dd].append(df)
                #print(len(dfs[dd]))
            #break
        #break
    return dfs


def make_fig(year, cat, dfs):
    fig, axs = plt.subplots(3, 1, figsize=(12,18))
    labs = 'abc'
    for dd, df in dfs.items():
        #print(df.head())
        ax = axs[dd-1]
        df_sub = df[df['time']==year]
        sns.lineplot('age', 'both_age', hue='prob', hue_order=sorted(list(set(df_sub['prob'].tolist()))), data=df_sub, legend="full", ax=ax)
        ax.set_title('({}) detail level {}, {}, year {}'.format(labs[dd-1], str(dd), cat, str(year)), loc='left')
        #break
    plt.tight_layout()

    fname = 'res_figs/popyramid_{}/fig_poppyramid_{}_{}.png'.format(cat, str(year), cat)
    outdir = os.path.dirname(fname)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    plt.savefig(fname, dpi=92, bbox_inches='tight')
    plt.close()


def process_cat(cat, target_file):
    #cat = 'couple_prob'
    print('reading file')
    dfs = get_dfs(cats[0], target_file)

    for year in sorted(list(set(dfs[1]['time'].tolist()))):
        print('making figure {} {}'.format(cat, year))
        make_fig(year, cat, dfs)

if __name__ == '__main__':
    target_file = 'stored_sex_age_stats.csv.xz'

    cats = ['couple_prob', 'divorce_prob', 'leaving_prob']
    #cats = ['divorce_prob', 'leaving_prob']
    for cat in cats:
        process_cat(cat, target_file)
    print('---done---')
