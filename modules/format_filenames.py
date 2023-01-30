import os
from pathlib import Path


def fetch_files(directory_path):
    p = Path(directory_path)
    return p.glob('*.jpg')


def rename(file_path, new_name):
    old_cwd = os.getcwd()
    file_dir = Path(file_path).parent
    cur_filename = Path(file_path).name
    os.chdir(file_dir)
    os.rename(cur_filename, new_name)
    os.chdir(old_cwd)
    print(f"""
    ###################################################################
    Renamed file: {file_path}.
    New file path: {file_dir.joinpath(new_name)}
    ###################################################################
    """)


def reformat(directory_path):
    files = fetch_files(directory_path)
    for file in files:
        file_stem = Path(file).stem
        # filename = Path(file).name
        # print(filename)
        base = file_stem.split('-')[0]
        number = file_stem.split('-')[1]
        padded_num = number.zfill(4)
        new_filename = base + '_' + padded_num + '.jpg'
        # print
        rename(file, new_filename)


if __name__ == '__main__':
    reformat(Path(r'C:\Users\LinWin-001\Documents\Datasets\74.220.215.205\RAW\CASME_A\Section A\sub01\EP01_5 - Copy'))
