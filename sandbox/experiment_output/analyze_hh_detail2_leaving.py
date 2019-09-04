
import pandas as pd
import analyze_hh as ahh

def main():
    import os
    res_base = '_run_output_2'
    cd = 'leaving_prob'
    prop_dirs = sorted(os.listdir(os.path.join(res_base, cd)))
    for rd in prop_dirs:
        seed_dirs = sorted(os.listdir(os.path.join(res_base, cd, rd)))
        for sd in seed_dirs:
            fp = os.path.join(res_base, cd, rd, sd, 'stored_household.csv')
            fout_size = os.path.join(res_base, cd, rd, sd, 'household_size_dynamic.csv')
            fout_struc = os.path.join(res_base, cd, rd, sd, 'household_structure_dynamic.csv')
            if os.path.exists(fout_struc): continue
            df = pd.read_csv(fp, index_col=0)
            hsize_df = ahh.analyse_household_size_dynamic(df)
            hstruc_df = ahh.analyse_household_structure_dynamic(df)
            hsize_df.to_csv(fout_size, index_label='ind')
            hstruc_df.to_csv(fout_struc, index_label='ind')
            print('done:', fp)


if __name__ == '__main__':
    main()