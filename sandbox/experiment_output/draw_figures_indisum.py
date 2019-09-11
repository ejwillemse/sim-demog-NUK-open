import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from tqdm import tqdm

import read_txz as txz

basedir = 'compress'
all_fs = sorted(os.listdir(basedir))
#all_fs

group_fs = {}
for f in all_fs:
    ff = f.split('-')
    cat = ff[1]
    pset = ff[2].split('_')[-1]
    dn = ff[0].split('_')
    if len(dn)<4:
        dd = 1
    else:
        dd = int(float(dn[3]))
    #print(dd)
    #seed = ff[3].split('_')[2]
    if not(cat in group_fs): group_fs[cat] = {}
    if not(dd in group_fs[cat]): group_fs[cat][dd] = {}
    if not(pset in group_fs[cat][dd]): group_fs[cat][dd][pset] = []
    group_fs[cat][dd][pset].append(f)
    #print(seed)
    #break

def process_cat(cat):
    #cat = 'couple_prob'
    print('reading file')
    dfs = {1:None, 2:None, 3:None}
    for dlvl, probs in group_fs[cat].items():
        this_df = None
        #print(probs)
        for catp, v in probs.items():
            for f in v:
                fp = os.path.join(basedir, f)
                ff = f.split('-')
                seed = ff[3].split('_')[2]
                df = txz.read_df_from_txz(fp, 'yearly_summary.csv')
                df['detail_level'] = dlvl
                df[cat] = float(catp)
                df['seed'] = seed
                if this_df is None:
                    this_df = df
                else:
                    this_df = this_df.append(df)
        dfs[dlvl] = this_df
        print(dlvl)
    print('done reading file')
    return dfs

def make_fig(col, cat, dfs):

    fig, axs = plt.subplots(3, 1, figsize=(12,18))
    sns.lineplot(x='years', y=col, hue=cat, data=dfs[1], ax=axs[0])
    axs[0].set_title('(a) detail floating 1 digit, {}'.format(col), loc='left')
    sns.lineplot(x='years', y=col, hue=cat, data=dfs[2], ax=axs[1])
    axs[1].set_title('(b) detail floating 2 digit, {}'.format(col), loc='left')
    sns.lineplot(x='years', y=col, hue=cat, data=dfs[3], ax=axs[2])
    axs[2].set_title('(c) detail floating 3 digit, {}'.format(col), loc='left')
    plt.tight_layout()

    fname = 'res_figs/fig_indisum_{}_{}.png'.format(cat, col)
    plt.savefig(fname, dpi=92, bbox_inches='tight')
    plt.close()


def process_one_cat(cat):
    dfs = process_cat(cat)

    #cols = [ 'type_{}'.format(str(c)) for c in range(7) ]
    cols = ['no_individuals', 'no_births', 'no_deaths']
    for col in cols:
        print('making figure {} {}'.format(cat, col))
        make_fig(col, cat, dfs)

if __name__ == '__main__':
    cats = ['couple_prob', 'divorce_prob', 'leaving_prob']
    for cat in cats:
        process_one_cat(cat)
