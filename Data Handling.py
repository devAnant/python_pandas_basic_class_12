import pandas as pd
def p1():
    s1=pd.Series([3,7,6,8,12,4,1,3])
    print('Max\n',s1.sort_values(ascending=False).head(3))
    print('Min\n',s1.sort_values(ascending=True).head(3))
    

def p2():
    S_marks={'Name':['Rashmi','Harsh','Ganesh','Priya','Vivek','Rajesh','Suresh'],
             'Grade':['A1','A2','B1','A1','B2','A1','B1']}
    df=pd.DataFrame(S_marks,columns=['Name','Grade'])
    print(df)
    print(df.loc[0:5])
    print(df[0:5])
    del df['Grade']
    print(df)
    df.drop([2,4],axis=0,inplace=True)
    df.drop(6,axis=0)
    df.drop([0,1,3,5],axis=0)
    print(df)

def p3():
    Table={'Name':['Sachin','Dhoni','Virat','Rohit','Shikhar'],
           'Age':[26,25,25,24,31],
           'Score':[87,67,89,55,47]}
    df=pd.DataFrame(Table)
    print('Average',df['Score'].mean())
    print('Median',df['Score'].median())
    print('Max',df['Score'].max())
    print('Min',df['Score'].min())
    print('Sum',df['Score'].sum())
    print('Mode',df['Score'].mode())

def p4():# pivot (Youtube Anajai Mam)
    #creating dict
    dict={
        'Name':['Aman','Bahnu','Charu','Aman','Bahnu','Charu',
                'Aman','Bahnu','Charu','Aman','Bahnu','Charu'],
        'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
        'Subject':['Mathematic','Mathematic','Mathematic','Science','Science','Science',
                   'Mathematic','Mathematic','Mathematic','Science','Science','Science'],
        'Score':[62,47,55,74,31,77,85,63,42,78,91,89]}

    #creating DataFrame
    df=pd.DataFrame(dict,columns=['Name','Exam','Subject','Score'])
    print(df)
    
    #pivoting table(first group according to exam then subject)and applying aggregate function
    pv=pd.pivot_table(df,index=['Exam','Subject'],aggfunc='mean')
    print('\npivoting table(first group according to exam then subject)and applying aggregate function\n')
    print(pv)

    #pivoting table(first group according to subject then exam)and applying aggregate function
    pv=pd.pivot_table(df,index=['Subject','Exam'],aggfunc='mean')
    print('\npivoting table(first group according to subject then exam)and applying aggregate function\n')
    print(pv)
    
    #pivoting table(first group according to name then subject)and applying aggregate function
    pv=pd.pivot_table(df,index=['Name','Subject'],aggfunc='mean')
    print('\npivoting table(first group according to name then subject)and applying aggregate function\n')
    print(pv)

    #pivoting table(first group according to exam then subject)and applying aggregate function
    pv=pd.pivot_table(df,index=['Exam','Subject'],aggfunc='count')
    print('\npivoting table(first group according to exam then subject)and applying aggregate function\n')
    print(pv)
    
    #pivoting table(first group according to subject then exam)and applying aggregate function
    pv=pd.pivot_table(df,index=['Exam','Subject'],aggfunc='count')
    print('\npivoting table(first group according to subject then exam)and applying count function\n')
    print(pv)
    
    #pivoting table and applying aggregate function
    pv=pd.pivot_table(df,index=['Exam'],aggfunc='max')
    print('\npivoting table and applying max function\n')
    print(pv)
    
    
