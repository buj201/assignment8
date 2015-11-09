import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from simulate_bets import *


def generate_result_table_and_plots(positions, num_trials):
    daily_ret = get_daily_returns_for_n_days(positions, num_trials)
    
    means = daily_ret.mean(axis=0)
    stds = np.std(daily_ret,axis=0)
    results =dict()
    results['Mean'] = np.round(means,4)
    results['Std Dev'] = np.round(stds,4)
    summary_stats = pd.DataFrame(results, index=positions)
    summary_stats.index.name = 'Position'
    summary_stats.to_csv('results/results.txt',sep=',')
    
    for i in xrange(daily_ret.shape[1]):
        plt.figure()
        title = "Performance for " + str(positions[i]) + " bet(s) of $" + str(1000.0/positions[i])
        plt.xlim(-1,1)
        plt.hist(daily_ret[:,i], bins=100, range=[-1,1])
        plt.title(title)
        plt.ylabel('Frequency (count)')
        plt.xlabel('Daily return (as relative gain/loss)')
        plt.gcf()
        save_name = 'results/histogram_' + str(positions[i]) + '_pos.pdf'
        plt.savefig(save_name, format='pdf')
