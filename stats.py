from pstats import Stats
import statsmodels
import statsmodels.api as sm
import statsmodels.stats

import statsmodels.stats.multitest as tests
import pickle



with open("/home/thales/deep-knowledge-tracing-plus/p_values.pickle",'rb') as file:
    p_values = pickle.load(file)


p_values_SAKT = p_values['pvalue_SAKT']

p_values_DSAKT = p_values['pvalues_DAKT']


BH_tests = {}

for i in p_values_SAKT.keys():
    BH_tests[i] = tests.multipletests([p_values_SAKT[i],p_values_DSAKT[i]],alpha=0.05,method='fdr_bh')



for i in BH_tests.keys():
    print(i)
    print(BH_tests[i])
