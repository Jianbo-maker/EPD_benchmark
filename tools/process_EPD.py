import os
import scipy.io as sio
import random
import numpy
import pickle
import csv
from tqdm import tqdm
import pandas as pd

def get_meta_info():
    info_file = './datasets/score1.csv'

    save_meta_path = './datasets/meta_info/meta_info_EPDDataset.csv'
    with open(info_file, 'r') as f, open(save_meta_path, 'w+') as sf:
        csvreader = csv.reader(f)
        head = next(csvreader)
        print(head)

        new_head = ['dist_name', 'dmos']
        csvwriter = csv.writer(sf)
        csvwriter.writerow(new_head)
        for idx, row in enumerate(csvreader):
            print(row)
            dis_name = row[0]
            # ref_name = row[1]
            dmos = row[2]
            csvwriter.writerow([dis_name, dmos])
            #  msg = f'{ref_name:<15}\t{dis_name:<15}\t{dmos:<15}\n'
            #  sf.write(msg)

def get_random_splits(seed=123):
    random.seed(seed)
    meta_info_file = './datasets/meta_info/meta_info_EPDDataset.csv'
    save_path = f'./datasets/meta_info/EPD_{seed}.pkl'
    ratio = 0.8

    meta_info = pd.read_csv(meta_info_file)

    ref_img_list = list(set(meta_info['dist_name'].tolist()))
    ref_img_num = len(ref_img_list)
    num_splits = 10
    train_num = int(ratio * ref_img_num)

    split_info = {}
    for i in range(num_splits):
        split_info[i + 1] = {'train': [], 'val': [], 'test': []}

    for i in range(num_splits):
        random.shuffle(ref_img_list)
        train_ref_img_names = ref_img_list[:train_num]
        for j in range(meta_info.shape[0]):
            tmp_ref_name = meta_info.loc[j]['dist_name']
            if tmp_ref_name in train_ref_img_names:
                split_info[i + 1]['train'].append(j)
            else:
                split_info[i + 1]['val'].append(j)
        print(meta_info.shape[0], len(split_info[i + 1]['train']), len(split_info[i + 1]['val']))
    with open(save_path, 'wb') as sf:
        pickle.dump(split_info, sf)

if __name__ == '__main__':
    get_meta_info()
    get_random_splits()
