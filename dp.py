import os
import csv
from matplotlib import pyplot as plt

path_name = 'C:/Users/willi/OneDrive/Documents/Github/heckin_darns' #modify based on the machine you're on and the folder you're placing things into

#this convention can be modified. If Shooter is the only thing logging, it will work
x_row = 0
bool_row = 2
y_row = 3
min_spd = 2600 #modify based on the shot you're shooting


def get_all_files(path):
    for cur_path, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename != 'dp.py':
                yield path + '/' + filename

def get_most_recent(path):
    return max(get_all_files(path_name), key = os.path.getmtime)

tsv_file = get_most_recent(path_name)

x_vals = []
y_vals = []

with open(tsv_file) as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter = '\t')
    line_num = 0
    for line in tsvreader:
        if not line_num < 1:
            if bool(line[bool_row]) and float(line[y_row]) > min_spd:   
                x_vals.append(float(line[x_row]) / 1000)
                y_vals.append(float(line[y_row]))
        line_num += 1
        
# create a figure and axis
fig, ax = plt.subplots()

# plot the x and y values 

ax.plot(x_vals, y_vals, linestyle='-')
# set a title and labels
ax.set_title('Shooter Plot')
ax.set_xlabel('Time')
ax.set_ylabel('Speed')

plt.savefig('current_plot')




