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
                df = txz.read_df_from_txz(fp, 'stored_sex_age_stats.csv')
                df['detail_level'] = dlvl
                df[cat] = float(catp)
                df['seed'] = seed
                if this_df is None:
                    this_df = df
                else:
                    this_df = this_df.append(df)
        this_df['both_age'] = this_df['male'] + this_df['female']
        this_df['age_group'] = [ int(a/5)*5 for a in this_df['age'] ]
        dfs[dlvl] = this_df
        print(dlvl)
    print('done reading file')
    return dfs

def make_fig(year, cat, dfs):

    dfs3 = { k:v[v['time']==year] for k,v in dfs.items() }
    fig, axs = plt.subplots(3, 1, figsize=(12,18))
    sns.lineplot(x='age', y='ag_prop', hue=cat, data=dfs3[1], ax=axs[0])
    axs[0].set_title('(a) detail floating 1 digit, {}'.format(str(year)), loc='left')
    sns.lineplot(x='age', y='ag_prop', hue=cat, data=dfs3[2], ax=axs[1])
    axs[1].set_title('(b) detail floating 2 digit, {}'.format(str(year)), loc='left')
    sns.lineplot(x='age', y='ag_prop', hue=cat, data=dfs3[3], ax=axs[2])
    axs[2].set_title('(c) detail floating 3 digit, {}'.format(str(year)), loc='left')
    plt.tight_layout()

    fname = 'res_figs/popyramid_{}/fig_poppyramid_{}_{}.png'.format(cat, str(year), cat)
    plt.savefig(fname, dpi=92, bbox_inches='tight')
    plt.close()


def process_one_cat(cat):
    dfs = process_cat(cat)
    dfs2 = {}

    for dlvl, df in dfs.items():
        this_df = pd.DataFrame(df.groupby(['time', cat, 'seed', 'age'])['both_age'].sum())
        subtot = this_df.groupby(['time', cat, 'seed'])['both_age'].sum().to_dict()
        subtot_col = []
        for i in range(len(this_df)):
            row = this_df.iloc[i]
            time, couple_prob, seed, age = row.name
            tot = subtot[(time, couple_prob, seed)]
            subtot_col.append(tot)
        this_df['year_total'] = subtot_col
        this_df['ag_prop'] = this_df['both_age'] / this_df['year_total']
        this_df.reset_index(drop=False, inplace=True)
        dfs2[dlvl] = this_df

    years = sorted(list(set(dfs2[1]['time'].tolist())))
    for year in years:
        print('making figure {} {}'.format(cat, year))
        make_fig(year, cat, dfs2)

if __name__ == '__main__':
    cats = ['couple_prob', 'divorce_prob', 'leaving_prob']
    #cats = ['divorce_prob', 'leaving_prob']
    for cat in cats:
        process_one_cat(cat)
