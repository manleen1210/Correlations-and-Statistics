# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:01:36 2021

@author: manle
"""

import pandas as pd

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

"""
Looking at a small sample 
"""
diabetes_small = diabetes.sample(100)

"""Getting a list of all variabke names from our small sample"""  
list(diabetes_small)

"""
Questions to be answered
1) Is there a difference between sex (M:F) and the number of days in hospital?
2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?
"""

""" Question 1
1) Is there a difference between sex (M:F) and the number of days in hospital? """

""" Creating new dataframes to align with each level of the sex column """

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

"""T-test"""
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp


ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

""" p-value here is 1.4217299655114968e-21 and t-test statistic = 9.542637042242887
The p-value is << 0.05 which indicates that the data is significant and a high 
statistic value indicates that there is a difference between 
the male and female data for number of days in hospital """






""" Question 2 
 Is there a difference between RACE (Caucasian and African American) 
 and the number of days in hospital? """
 
 """ Creating new dataframes to align with each level of the race column 
 as specified in the question """
 
 Caucasian = diabetes[diabetes['race']=='Caucasian']
 AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
 
 """T-test"""
 ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])
 
 """ p-value here is 4.178330085585203e-07 and t-test statistic = -5.0610017032095325
The p-value is << 0.05 which indicates that the data is significant and 
a high absolute statistic value indicates that the data is significantly different
between the Caucasian and AfricanAmerican data for number of days in hospital
"""
 
 
 
 
 
 
 """ Question 3
 Is there a difference between RACE (Asian and African American) and the number
 of lab procedures performed? """
 
""" Creating one new dataframe to align with each level of the race column 
 as specified in the question since the dataframe for AfricanAmerican 
 individuals has already been created """
 
 Asian =  diabetes[diabetes['race']=='Asian']
  
 """T-test"""
 ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])
 
 """ p-value here is 6.948907528800307e-05 and t-test statistic = -3.9788715315360292 
 The p-value is << 0.05 which indicates that the data is significant and 
 a high absolute statistic value indicates that the data is significantly different
for Asian and AfricanAmerican data for number of lab procedures performed """
 

