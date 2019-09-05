
import tarfile
import pandas as pd

def check_files_in_txz(fp):
    tar = tarfile.open(fp)
    members = tar.getmembers()
    tar.close()
    return [ str(mem) for mem in members ]

def read_df_from_txz(fp, target_file):
    content = None
    tar = tarfile.open(fp)
    members = tar.getmembers()
    for mem in members:
        if target_file in str(mem):
            f = tar.extractfile(mem)
            #content=f.read()
            content = pd.read_csv(f)
            f.close()
    tar.members = []
    tar.close()
    return content