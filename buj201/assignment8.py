'''
Created on Nov 4, 2015

@author: ds-ga-1007
'''
from produce_sim_results import *
import re

if __name__ == '__main__':
    pass

building_pos_list = True
positions = raw_input('Input a list of the number of shares to buy in parallel, e.g. [1, 10, 100, 1000]: ')
while building_pos_list:
    try:
        positions = re.search('\[[^\]]*\]', positions).group(0)
        pos_values = re.split('[\s]*,[\s]*', positions[1:-1])
        for i in range(len(pos_values)):
            pos_values[i] = int(pos_values[i])
    except:
        positions = raw_input('Invalid input- re-input a list of the number of shares to buy in parallel, e.g. [1, 10, 100, 1000]: ')
    else:
        building_pos_list = False
        positions = re.search('\[[^\]]*\]', positions).group(0)
        pos_values = re.split('[\s]*,[\s]*', positions[1:-1])
        for i in range(len(pos_values)):
            pos_values[i] = int(pos_values[i])
        
getting_num_trials = True
num_trials = raw_input('Input an integer number of trials (how many times to randomly repeat the test): ')
while getting_num_trials:
    try:
        num_trials = re.search('[0-9]+', num_trials).group(0)
    except:
        num_trials = raw_input('Invalid input- re-input an integer number of trials (how many times to randomly repeat the test): ')
    else:
        getting_num_trials = False
        num_trials = int(re.search('[0-9]+', num_trials).group(0))
    
generate_result_table_and_plots(pos_values, num_trials)

