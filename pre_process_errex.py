from cgi import print_directory
from cmath import nan
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



'''
with open('/home/thales/deep-knowledge-tracing-plus/data/errex/ErrEx posttest data.xlsx','rb') as file:
    df_2 = pd.read_excel(file)


df_2 = df_2.drop([0,1], axis=0)
df_2 = df_2.drop(df_2.columns[1:5],axis=1)
'''
#REPLACE IN DATASET

with open('/home/thales/deep-knowledge-tracing-plus/errex_replace_data.csv','rb') as file:
    df_3 = pd.read_csv(file)

'''


students  = df_3['student_id'].unique()

replacing_students_ids = {}

count = 1

for i in range(len(students)):
    replacing_students_ids[students[i]] = count
    count = count +1


df_3 = df_3.replace({'student_id':replacing_students_ids})
df_3 =df_3.replace({'skill_name':{'OrderingDecimals':1,'PlacementOnNumberLine':2,'CompleteTheSequence':3,'DecimalAddition':4}})

print(df_3.head())
with open('/home/thales/deep-knowledge-tracing-plus/errex_replace_data.csv','w') as file:
    df_3.to_csv(file,index=False) 

'''

'''
attempts_duplicated = []
for student in df_3['student_id'].unique():
     attempts_duplicated.append(df_3[df_3['student_id'] == student]['problem_id'].duplicated().sum())
#print(df_3['student_id'].unique()[468])


students = df_3['student_id'].unique()
x = df_3.copy()
for student in students:
    y = x.loc[x.student_id == student].drop_duplicates('problem_id',keep='first').astype({'problem_id':int,'correct':int})
    df_3[df_3.student_id == student] = y


df_3.dropna(subset=['student_id','problem_id','condition','skill_name','correct'],inplace=True)
df_3.reset_index(inplace=True)
df_3.drop('index',axis='columns',inplace= True)
df_3 = df_3.astype({'problem_id':int,'correct':int})
'''

#Stu_c8e563df704f18421e9f



#GENERATE problems_per_skills
'''

problems_per_skills = {}

for skill in df_3['skill_name'].unique():
    problems_per_skills[skill] = np.unique(df_3['problem_id'][df_3['skill_name']==skill].values.astype(int))


with open ('problems_per_skills.pickle','wb') as file:
    pickle.dump(problems_per_skills,file)
'''




# adicionar o uma linha dos conceitos
# gerar um outro só com os conceitos


#GENERATE pre_process_data


students_data ={}

for student in df_3['student_id'].unique():
    
    student_info= {}
    #student_info['id'] = [student,student]

    student_info['exercise_number'] = [(len(df_3[df_3['student_id']==student]['problem_id'].values))]
    #student_info['exercise_id'] = df_3[df_3['student_id']==student]['problem_id'].values.astype(int)
    student_info['skills'] = df_3[df_3['student_id']==student]['skill_name'].values.astype(int)
    student_info['responses'] = df_3[df_3['student_id']==student]['correct'].values.astype(int)
    students_data[student] = student_info




with open('/home/thales/deep-knowledge-tracing-plus/data/errex/errex_data_train1.csv','w') as file:
    writer = csv.writer(file)
    
    for student in df_3['student_id'].unique():

        for keys in student_info.keys():       
            writer.writerow(students_data[student][keys])
    file.close()



'''
with open ('student_data.pickle','wb') as file:
    pickle.dump(students_data,file)

'''
#GENERATE students_interations
'''
students_interations = {}

for student in df_3['student_id'].unique():
    if type(student) == str:
        students_interations[student] = [df_3.loc[df_3.student_id == student,'problem_id'].values.astype(int),df_3.loc[df_3.student_id == student,'correct'].values.astype(int)]

with open ('student_interations.pickle','wb') as file:
    pickle.dump(students_interations,file)
'''



# GENERATE final results
'''


with open ('/home/thales/deep-knowledge-tracing-plus/students_mean.pickle','rb') as file:
        students_mean = pickle.load(file)

ord_decimals = [i['OrderingDecimals'] for i in  list(students_mean.values())]
place_number = [i['PlacementOnNumberLine'] for i in  list(students_mean.values())]
complet_sequence = [i['CompleteTheSequence'] for i in  list(students_mean.values())]
decimal_adition =  [i['DecimalAddition'] for i in  list(students_mean.values())]

skills_score = {
    'OrderingDecimals':ord_decimals,
    'PlacementOnNumberLine':place_number,
    'CompleteTheSequence':complet_sequence,
    'DecimalAddition': decimal_adition
}
#print(skills_score)

df = pd.DataFrame(skills_score,index= list(students_mean.keys()))

df.to_excel('skills_scores_dropped.xlsx')



df_post_dropped = df_2.drop_duplicates('Anon Student Id',keep='last')
df_post_dropped = df_post_dropped.drop(df_post_dropped.index[598])

decimal_addition_post = df_post_dropped['Unnamed: 171'].values
ordering_decimals_post=  df_post_dropped['Unnamed: 172'].values 
complete_sequence_post = df_post_dropped['Unnamed: 173'].values 
placement_number_post = df_post_dropped['Unnamed: 174'].values 


decimal_addition_estimate = df['DecimalAddition'].values
placement_number_estimate = df['PlacementOnNumberLine'].values
complete_sequence_estimate = df['CompleteTheSequence'].values
ordering_decimals_estimate = df['OrderingDecimals'].values


pearson_correlations = {}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

pearson_correlations['OrderingDecimals'] = pearsonr(ordering_decimals_estimate,ordering_decimals_post)[0]
pearson_correlations['PlacementOnNumberLine'] = pearsonr(placement_number_estimate,placement_number_post)[0]
pearson_correlations['CompleteTheSequence'] = pearsonr(complete_sequence_estimate,complete_sequence_post)[0]
pearson_correlations['DecimalAddition'] = pearsonr(decimal_addition_estimate,decimal_addition_post)[0]

print(pearson_correlations)

df_results = pd.DataFrame.from_dict(pearson_correlations,orient="index",columns=['Pearson Correlations'])
df_results.to_csv('results_pearson_coeff_dropped.csv')
'''