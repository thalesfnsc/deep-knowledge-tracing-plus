from cgi import print_directory
from distutils import errors
from re import A
import pandas as pd
import numpy as np
import pickle
from iteration_utilities import duplicates
from scipy.stats import pearsonr
from sqlalchemy import column
import csv

from torch import int64




with open('/home/thales/deep-knowledge-tracing-plus/skills_scores_estimates.csv','rb') as file:
    df = pd.read_csv(file)


with open('/home/thales/deep-knowledge-tracing-plus/data/errex/ErrEx posttest data.xlsx','rb') as file:
    df_2 = pd.read_excel(file)


df_2 = df_2.drop([0,1], axis=0)
df_2 = df_2.drop(df_2.columns[1:5],axis=1)


with open('/home/thales/deep-knowledge-tracing-plus/data/errex/errex data subproblems.csv','rb') as file:
    df_3 = pd.read_csv(file)



















#GENERATE problems_per_skills

'''
problems_per_skills = {}

for skill in df['skill_name'].unique():
    problems_per_skills[skill] = np.unique(df['problem_id'][df['skill_name']==skill].values)

with open ('problems_per_skills.pickle','wb') as file:
    pickle.dump(problems_per_skills,file)
'''




#GENERATE pre_process_data


'''
attempts_duplicated = []
for student in df_3['student_id'].unique():
     attempts_duplicated.append(df_3[df_3['student_id'] == student]['problem_id'].duplicated().sum())

students = df_3['student_id'].unique()
x = df_3.copy()
for student in students:
    y = x.loc[x.student_id == student].drop_duplicates('problem_id',keep='first').astype({'problem_id':int,'correct':int})
    df_3[df_3.student_id == student] = y
    
#Stu_c8e563df704f18421e9f
    

students_data ={}
for student in df_3['student_id'].unique():
    student_info= {}
    student_info['exercise_number'] = [(len(df_3[df_3['student_id']==student]['problem_id'].values))]
    student_info['exercise_id'] = df_3[df_3['student_id']==student]['problem_id'].values.astype(int)
    student_info['responses'] = df_3[df_3['student_id']==student]['correct'].values.astype(int)
    students_data[student] = student_info


with open('/home/thales/deep-knowledge-tracing-plus/data/errex/preprocessed_errex_data.csv','w') as file:
    writer = csv.writer(file)
    
    for student in df_3['student_id'].unique():
        for keys in student_info.keys():       
            writer.writerow(students_data[student][keys])
    file.close()

with open ('student_data.pickle','wb') as file:

    pickle.dump(students_data,file)
'''

#GENERATE students_interations

'''
students_interations = {}

for student in df_3['student_id'].unique():
    students_interations[student] = [df_3['problem_id'][df_3['student_id'] == student].values.astype(int),df_3['correct'][df_3['student_id'] == student].values.astype(int)]


print(students_interations)

with open ('student_interations.pickle','wb') as file:
    pickle.dump(students_interations,file)
'''





'''
# GENERATE final results

df_post_dropped = df_2.drop_duplicates('Anon Student Id',keep='first')
df_post_dropped = df_post_dropped.drop(df_post_dropped.index[598])

decimal_addition_post = df_post_dropped['Unnamed: 171'].values
ordering_decimals_post=  df_post_dropped['Unnamed: 172'].values 
complete_sequence_post = df_post_dropped['Unnamed: 173'].values 
placement_number_post = df_post_dropped['Unnamed: 174'].values 


decimal_addition_estimate = df['DecimalAddition'].values
placement_number_estimate = df['PlacementOnNumberLine'].values
complete_sequence_estimate = df['CompleteTheSequence'].values
ordering_decimals_estimate = df['OrderingDecimals'].values

print(len(decimal_addition_estimate))

pearson_correlations = {}

pearson_correlations['OrderingDecimals'] = pearsonr(ordering_decimals_estimate,ordering_decimals_post)[0]
pearson_correlations['PlacementOnNumberLine'] = pearsonr(placement_number_estimate,placement_number_post)[0]
pearson_correlations['CompleteTheSequence'] = pearsonr(complete_sequence_estimate,complete_sequence_post)[0]
pearson_correlations['DecimalAddition'] = pearsonr(decimal_addition_estimate,decimal_addition_post)[0]

print(pearson_correlations)

df_results = pd.DataFrame.from_dict(pearson_correlations,orient="index",columns=['Pearson Correlations'])
df_results.to_csv('results_pearson_coeff.csv')

'''
