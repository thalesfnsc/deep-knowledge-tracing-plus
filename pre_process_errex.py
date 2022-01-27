from re import A
import pandas as pd
import csv

with open('/home/thales/deep-knowledge-tracing-plus/data/errex/errex data subproblems.csv','rb') as file:
    df = pd.read_csv(file)





students_data ={}

for student in df['student_id'].unique():
    student_info= {}
    student_info['exercise_number'] = [(len(df[df['student_id']==student]['problem_id'].values))]
    student_info['exercise_id'] = df[df['student_id']==student]['problem_id'].values
    student_info['responses'] = df[df['student_id']==student]['correct'].values
    students_data[student] = student_info


with open('/home/thales/deep-knowledge-tracing-plus/data/errex/preprocessed_errex_data.csv','w') as file:
    writer = csv.writer(file)
    
    for student in df['student_id'].unique():
        for keys in student_info.keys():       
            writer.writerow(students_data[student][keys])
    file.close()





