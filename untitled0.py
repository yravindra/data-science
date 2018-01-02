#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:29:04 2017

@author: ravindrakumar yadav

"""

import pandas as pd
import numpy as np
import matplotlib as pl


df = pd.read_csv("train.csv")
df.head(5)
"""
 Loan_ID Gender Married Dependents     Education Self_Employed  \
0  LP001002   Male      No          0      Graduate            No   
1  LP001003   Male     Yes          1      Graduate            No   
2  LP001005   Male     Yes          0      Graduate           Yes   
3  LP001006   Male     Yes          0  Not Graduate            No   
4  LP001008   Male      No          0      Graduate            No   

   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \
0             5849                0.0         NaN             360.0   
1             4583             1508.0       128.0             360.0   
2             3000                0.0        66.0             360.0   
3             2583             2358.0       120.0             360.0   
4             6000                0.0       141.0             360.0   

   Credit_History Property_Area Loan_Status  
0             1.0         Urban           Y  
1             1.0         Rural           N  
2             1.0         Urban           Y  
3             1.0         Urban           Y  
4             1.0         Urban           Y  
"""
df.columns


"""
Index(['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status'],
      dtype='object')

"""

df.describe()
"""
output -a
       ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \
count       614.000000         614.000000  592.000000         600.00000   
mean       5403.459283        1621.245798  146.412162         342.00000   
std        6109.041673        2926.248369   85.587325          65.12041   
min         150.000000           0.000000    9.000000          12.00000   
25%        2877.500000           0.000000  100.000000         360.00000   
50%        3812.500000        1188.500000  128.000000         360.00000   
75%        5795.000000        2297.250000  168.000000         360.00000   
max       81000.000000       41667.000000  700.000000         480.00000   

       Credit_History  
count      564.000000  
mean         0.842199  
std          0.364878  
min          0.000000  
25%          1.000000  
50%          1.000000  
75%          1.000000  
max          1.000000  

"""

"""
1) loanAmount has 614-592 = 22  missing value 
2)loan_amount has (614-600) 14 missing value 
3)credit_history has (614-564) 50 missing vlue 
4)We can also look that about 84% application have  creadit _history 
how? Mean of the creadit_history is (0.84%) (remember that creadit_histroy has value
1 for that have creadit history otherwise 0)
5) the application distrubution seems to be inline with expectation.
same with coapplication 

Please note that we can get un idea of possible skew in data by comparing the mean by meadian
i.e 50%
)
for the non numeric value(Property_area  creadit_histroy,dependent,etc) we can took frequency distrubation
to understand the whethr they make sence or not frequency table can be printed as 
"""

df['Property_Area'].value_counts()
df['Gender'].value_counts()
￼
df['ApplicantIncome'].hist(bins=50)

￼
"""
here we observ that there are few extream values    this is also  the reson the why the 50 bin 

are required to depicated the distribution clearly 

"""
"""next we look the box plot to understand the distribution box  plot for the fare can be plotaed the blow"""

df.boxplot(column='ApplicantIncome')

df.boxplot(column='ApplicantIncome', by = 'Education')
 
df['LoanAmount'].hist(bins=50)


df['LoanAmount'].value_counts()

df.boxplot(column='LoanAmount')

"""
again there are some extrem value ,clearly Applicantincome and LoanAmount
need some data munging LoanAmount has some extrem value as well missing value also
While applicant has few extrem value which demand deeper understanding,
we will take this in upper section
"""

df.loc[(df["Gender"]=="Female") & (df["Education"]=="Not Graduate") & (df["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]
"""
     Gender     Education Loan_Status
50   Female  Not Graduate           Y
197  Female  Not Graduate           Y
205  Female  Not Graduate           Y
279  Female  Not Graduate           Y
403  Female  Not Graduate           Y
407  Female  Not Graduate           Y
439  Female  Not Graduate           Y
463  Female  Not Graduate           Y
468  Female  Not Graduate           Y
480  Female  Not Graduate           Y
493  Female  Not Graduate           Y
534  Female  Not Graduate           Y
544  Female  Not Graduate           Y
587  Female  Not Graduate           Y


"""
