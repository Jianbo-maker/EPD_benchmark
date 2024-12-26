import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from scipy.stats import spearmanr

csv_file_path = './relation.csv'

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    headers = next(csv_reader)

    push = []
    pick = []
    all = []
    for row in csv_reader:
        try:
            push_data = float(row[4])
            pick_data = float(row[5])
            all_data = float(row[3])

            push.append(push_data)
            pick.append(pick_data)
            all.append(all_data)
        except IndexError:
            print(f"Error: Row {row} does not have enough columns.")

srcc, _ = spearmanr(all, push)
srcc1, _ = spearmanr(all, pick)
srcc2, _ = spearmanr(push, pick)

corr_matrix = [[srcc1, srcc2, 1],[srcc, 1, srcc2],[1, srcc, srcc1]]

labels = ['All', 'Push', 'Pick']
labelsy = ['Pick', 'Push', 'All']
plt.figure(figsize=(8, 8))
ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, cbar_kws={'shrink': .8},
                 xticklabels=labels, yticklabels=labelsy, annot_kws={'size': 20})

ax.tick_params(labelsize=20)
ax.set_xticklabels(labels, fontsize=20)
ax.set_yticklabels(labelsy, fontsize=20)

plt.savefig('relation_matrix.pdf', format='pdf')

plt.show()
# plt.close()