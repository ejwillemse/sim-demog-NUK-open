
import argparse
from tqdm import tqdm
import pandas as pd
import os


def counting_total_hh(df):
    df2 = df.groupby('time')['household_id'].count().reset_index(name='no_household')
    return df2

def process_a_household(df_hh):
    df_hh = df_hh.sort_values('time')
    ts = df_hh.time.tolist()
    df_hh = df_hh.set_index('time')
    pre_hhsize = df_hh.loc[ts[0]]['household_size']
    changed_info = []
    if ts[0]>0:
        changed_info.append((ts[0], 'new-household', pre_hhsize))
    hh_change = []
    for t in ts[1:]:
        row = df_hh.loc[t]
        cur_hhsize = row['household_size']
        hhsize_change = float(cur_hhsize - pre_hhsize)
        hh_change.append(hhsize_change)
        pre_hhsize = cur_hhsize
    for t,c in zip(ts[1:], hh_change):
        if c!=0:
            if c>0:
                changed_info.append((t, 'size-up', c))
            else:
                changed_info.append((t, 'size-down', c))
    return changed_info


def analyse_household_size_dynamic(df):
    df['children'] = df['infant'] + df['school_age']
    households = list(set(df.household_id.tolist()))
    all_times = list(set(df['time'].tolist()))
    hh_events = None
    for hh in tqdm(households, desc='processing households'):
        df_hh = df[df['household_id'] == hh]
        changes = process_a_household(df_hh)
        if len(changes) > 0:
            df_changes = pd.DataFrame.from_records(changes)
            df_changes['hh_id'] = hh
            if not (hh_events is None):
                hh_events = hh_events.append(df_changes)
            else:
                hh_events = df_changes
    hh_events = hh_events.reset_index(drop=True)
    hh_events = hh_events.rename(columns={0: 'time', 1: 'event', 2: 'size'})

    time_sum = {}
    for t in all_times[1:]:
        events_on_t = hh_events[hh_events['time'] == t]
        size_up = len(events_on_t[events_on_t['event'] == 'size-up'])
        size_down = len(events_on_t[events_on_t['event'] == 'size-down'])
        new_hh = len(events_on_t[events_on_t['event'] == 'new-household'])
        time_sum[t] = {'size_up': size_up, 'size_down': size_down, 'new_household': new_hh,
                       'sub_total': size_up + size_down + new_hh}
    time_sum_df = pd.DataFrame.from_dict(time_sum, orient='index')
    time_sum_df.index.name = 'time'
    time_sum_df = time_sum_df.reset_index()
    return time_sum_df

"""
simple version with same meaning

$$
R = \big\{ household ~|~ at~least~one~member~with~age~ \geq 65 \big\}
$$

$$
A = \big\{ household ~|~ at~least~one~member~with~age~in~between~  \geq 18 ~and~ < 65 \big\}
$$

$$
C = \big\{ household ~|~ at~least~one~member~with~age~ < 18 \big\}
$$

$$
type~I = R \setminus \big( A \cup C \big)
$$

$$
type~II = A \setminus \big( A \cup C \big)
$$

$$
type~III = R \cap A \setminus C
$$

$$
type~IV = R \cap C \setminus A
$$

$$
type~V = A \cap C \setminus R
$$

$$
type~VI = R \cap A \cap C
$$
"""


def analyse_household_structure(df, y):
    df_y = df[df['time']==y]
    household_type_counts = { ty:0 for ty in range(8) }

    # age_groups = ['children', 'adult', 'retired']
    for i in range(len(df_y)):
        row = df_y.iloc[i]
        c = row['children']
        a = row['adult']
        r = row['retired']
        if r==0 and a==0 and c>0: # only children household, not exist by rules
            household_type_counts[0]+=1
        elif r>0 and a==0 and c==0:
            household_type_counts[1]+=1
        elif r==0 and a>0 and c==0:
            household_type_counts[2]+=1
        elif r>0 and a>0 and c==0:
            household_type_counts[3]+=1
        elif r>0 and a==0 and c>0:
            household_type_counts[4]+=1
        elif r==0 and a>0 and c>0:
            household_type_counts[5]+=1
        elif r>0 and a>0 and c>0:
            household_type_counts[6]+=1
        else:
            # all == 0, a no-people household, not possible to be exist, just for safely capture the else statement
            household_type_counts[7]+=1
    return household_type_counts


def analyse_household_structure_dynamic(df, ys=None):
    df['children'] = df['infant'] + df['school_age']
    if ys is None:
        all_times = list(set(df['time'].tolist()))
    else:
        all_times = ys
    hs_dy = {}
    for y in tqdm(all_times, desc='time'):
        strc = analyse_household_structure(df, y)
        strc2 = { 'type_{}'.format(str(ty)): v for ty, v in strc.items() }
        hs_dy[y] = strc2
    hs_dynamic = pd.DataFrame.from_dict(hs_dy, orient='index')
    hs_dynamic.index.name = 'time'
    hs_dynamic = hs_dynamic.reset_index()
    return hs_dynamic

"""
def main2():
    res_base = '_run_output'
    cat_dirs = sorted(os.listdir(res_base))
    for cd in cat_dirs:
        prop_dirs = sorted(os.listdir(os.path.join(res_base, cd)))
        for rd in prop_dirs:
            seed_dirs = sorted(os.listdir(os.path.join(res_base, cd, rd)))
            for sd in seed_dirs:
                fp = os.path.join(res_base, cd, rd, sd, 'stored_household.csv.xz')
                fout_size = os.path.join(res_base, cd, rd, sd, 'household_size_dynamic.csv.xz')
                fout_struc = os.path.join(res_base, cd, rd, sd, 'household_structure_dynamic.csv.xz')
                fout_sum = os.path.join(res_base, cd, rd, sd, 'summary_household.csv.xz')
                if os.path.exists(fout_struc): continue
                df = pd.read_csv(fp, index_col=0)
                hsize_df = analyse_household_size_dynamic(df)
                hstruc_df = analyse_household_structure_dynamic(df)
                hhsum_df = counting_total_hh(df)
                hsize_df.to_csv(fout_size, index_label='ind', compression='xz')
                hstruc_df.to_csv(fout_struc, index_label='ind', compression='xz')
                hhsum_df.to_csv(fout_sum, index_label='ind', compression='xz')
                print('done:', fp)
"""


def process_one_file(fp, target_file):
    fout_size = fp.replace(target_file, 'household_size_dynamic.csv.xz')
    fout_struc = fp.replace(target_file, 'household_structure_dynamic.csv.xz')
    fout_sum = fp.replace(target_file, 'summary_household.csv.xz')

    if os.path.exists(fout_struc):
        print('done before with this file {}'.format(fp))
    else:
        df = pd.read_csv(fp, index_col=0)
        hsize_df = analyse_household_size_dynamic(df)
        hstruc_df = analyse_household_structure_dynamic(df)
        hhsum_df = counting_total_hh(df)
        hsize_df.to_csv(fout_size, index_label='ind', compression='xz')
        hstruc_df.to_csv(fout_struc, index_label='ind', compression='xz')
        hhsum_df.to_csv(fout_sum, index_label='ind', compression='xz')
        print('done processing {}'.format(fp))


def walk_search(dirpath, target_file):
    fps = []
    for root, dirs, files in os.walk(dirpath):
        path = root.split(os.sep)
        #print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            #print(len(path) * '---', file)
            fp = os.path.join(root, file)
            if file==target_file:
                fps.append(fp)
    return fps


def process_command():
    parser = argparse.ArgumentParser(prog='analyzing results', description='Processing some basic analysis and generate output csv results')
    parser.add_argument('--dir', help='targeted directory, will walk into the directory to look for stored_household.csv.xz')
    return parser.parse_args()


def main():
    args = process_command()
    #print(args.dir)

    target_file = 'stored_household.csv.xz'
    fs = walk_search(args.dir, target_file)
    for fp in fs:
        process_one_file(fp, target_file)


if __name__ == '__main__':
    main()
