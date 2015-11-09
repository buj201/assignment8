'''
Created on Nov 5, 2015

@author: ds-ga-1007
'''
import numpy as np

def get_bets_from_positions(positions):
    max_num_bets = np.max(positions)
    bets = np.zeros((max_num_bets,len(positions)))
    for i in range(len(positions)):
        bets[0:positions[i],i] = 1000.0 / positions[i]
    return bets

def get_returns_from_bets(bets):
    rand_vals = np.random.random(bets.shape)
    won_bet = (rand_vals >= 0.49)
    return_multiplier = np.zeros(bets.shape) + 2.0*won_bet
    bet_returns = bets*return_multiplier
    return bet_returns

def get_cumu_return_for_day(positions):
    bets = get_bets_from_positions(positions)
    bet_returns = get_returns_from_bets(bets)
    cumu_return = np.sum(bet_returns,axis=0)
    return cumu_return

def get_daily_returns_for_n_days(positions,num_trials):
    daily_ret = np.zeros((num_trials,len(positions)))
    for trial in xrange(num_trials):
        cumu_return = get_cumu_return_for_day(positions)
        daily_ret[trial] = (cumu_return / 1000.0) - 1.0
    return daily_ret
    

