import numpy as np
import pandas as pd

def p1():
    df=pd.DataFrame()
    print(df)

def p2():
    list=[10,20,30,40,50]
    df=pd.DataFrame(list)
    print(df)

    df.columns=['Age']
    print(df)

def p3():
    data=[['Shreya',20],['Rakshit',22],['Shrijan',18]]
    df=pd.DataFrame(data,columns=['Name','Age'])
    print(df)

def p4():
    studMarks=pd.Series({'Vijay':80,'Rahul':92,'Meghna':67,'Radhika':95,'Shurya':20})
    studAge=pd.Series({'Vijay':30,'Rahul':28,'Meghna':30,'Radhika':25,'Shurya':20})

    stud_df=({'Marks':studMarks,'Age':studAge})
    print(stud_df)

def p5():
    studMarks=pd.Series({'Vijay':80,'Rahul':92,'Meghna':67,'Radhika':95,'Shurya':20})
    studAge=pd.Series({'Vijay':30,'Rahul':28,'Meghna':30,'Radhika':25,'Shurya':20})

    stud_df=pd.DataFrame({'Marks':studMarks,'Age':studAge})
    print(stud_df)
    print()
    print(stud_df.sort_values(by=['Marks']))
    print()
    print(stud_df.sort_values(by=['Marks'],ascending=False))
    
def p6():
    student={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
             'English':[67,78,75,88,92],
             'Economics':[78,67,89,90,56],
             'IP':[77,88,98,90,87],
             'Accounts':[77,70,80,67,86]}

    print("Series generated as ")
    print(student)

    df=pd.DataFrame(student)
    print('DataFrame for Student\n',df)

def p7():
    student=[{'Rinku':67,'Ritu':78,'Ajay':75,'Pankaj':88,'Aditya':92},
             {'Rinku':72,'Ritu':58,'Ajay':87,'Pankaj':65},
             {'Rinku':88,'Ajay':67,'Pankaj':74,'Aditya':70}]
    
    new_df=pd.DataFrame(student)
    print(new_df)

def p8():
    student={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
             'English':[67,78,75,88,92],
             'Economics':[78,67,89,90,56],
             'IP':[77,88,98,90,87],
             'Accounts':[77,70,80,67,86]}

    df=pd.DataFrame(student)
    print('DataFrame for Student\n',df)
    print(df[1:4])

def p9():
    student={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
             'English':[67,78,75,88,92],
             'Economics':[78,67,89,90,56],
             'IP':[77,88,98,90,87],
             'Accounts':[77,70,80,67,86]}

    df=pd.DataFrame(student,index=['Stud_no.1','Stud_no.2','Stud_no.3','Stud_no.4','Stud_no.5'])
    print('DataFrame for Student\n',df)
    
def p10():
    student={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
             'English':[67,78,75,88,92],
             'Economics':[78,67,89,90,56],
             'IP':[77,88,98,90,87],
             'Accounts':[77,70,80,67,86]}

    df=pd.DataFrame(student)
    df.set_index('Name',inplace=True)
    print('DataFrame for Student\n',df)

def p11():
    student={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
             'English':[67,78,75,88,92],
             'Economics':[78,67,89,90,56],
             'IP':[77,88,98,90,87],
             'Accounts':[77,70,80,67,86]}

    df=pd.DataFrame(student)
    df.set_index('Name',inplace=True)
    print('DataFrame for Student\n',df)
    df.reset_index(inplace=True)
    print('DataFrame for Student\n',df)
    
def p12():
    list=[10,20,30,40,50]
    df=pd.DataFrame(list)
    df.columns=['Age']
    print(df)
    df['Age2']=45
    df['Age3']=pd.Series([42,44,50,60,45],index=[0,1,2,3,4])
    df['Total']=df['Age']+df['Age2']+df['Age3']
    print(df)
    df['Total']=df['Total']+10
    df['UpdateAge']=df['Total']
    print(df['UpdateAge'])
    
def p13():
    sMarks={'Name':['Rashmi','Harsh','Priya','Ganesh','Vivek','Rajesh','Suresh'],
            'Grades':['A1','A2','B1','A1','B2','A1','B1']}
    df=pd.DataFrame(sMarks)
    per=pd.Series([92,89,np.NaN,95,68,np.NaN,93])
    df['Percentage']=per
    print(df)
    df=df[['Name','Percentage','Grades']]
    #ndf=[df['Name'],df['Percentage'],df['Grades']]
    #newdf=pd.DataFrame(ndf)
    print(df)
    

def p14():
    data=[['S01','Amy',70],['S02','Bandhi',69],['S04','Cathy',75],['S05','Gundaho',82]]
    df=pd.DataFrame(data,columns=['SerialNo.','Name','Marks'])
    print(df)

def p15():
    data=[[1,2],[3,4],[5,6],[7,8]]
    df=pd.DataFrame(data,columns=['a','b'])
    df.set_index('a',inplace=True)
    print(df)
