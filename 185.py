# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd


# x=[1,2,3,4,5,6,7,8,9,10,11,12]
# y=[6,2,3,4,4,5,6,7,8,9,3,2]

# x2=[1,2,3,4,5,6,7,8,9,10,11,12]
# y2=[3,2,3,5,6,8,9,7,2,2,1,6]

# plt.xlabel('month')
# plt.ylabel('Sales')
# plt.title('Sales of the company\nCompany A & B')

# plt.plot(x,y,label='Company A')
# plt.plot(x2,y2,label='Company B')
# plt.legend()
# plt.show()



# x=['C1','C2','C3']
# y=[1,2,3]
# x2=[2,2,3]
# y2=[3,4,5]
# plt.bar(x,y,label='bar1')
# plt.bar(x2,y2,label='bar2')
# plt.legend()
# plt.xlabel('name')
# plt.ylabel('Sales')
# plt.title('Sales of the company\nCompany 1 2 3')

data2=pd.read_csv('C:/Users/Administrator/Desktop/countries.csv')
# print(data2)
China_filter=data2.country=='China'
China_data=data2[China_filter]

US_filter=data2.country=='United States'
US_data=data2[US_filter]]

JP_filter=data2.country=='Japan'
JP_data=data2[JP_filter]

print (China_data,US_data,JP_data)
plt.plot(China_data.year, China_data.population/China_data.population.iloc[0])
plt.plot(US_data.year, US_data.population/US_data.population.iloc[0])
plt.plot(JP_data.year, JP_data.population/JP_data.population.iloc[0])

plt.title('Country Population')
plt.xlabel('Year')
plt.ylabel('Population Growth')
plt.legend(['China','US','JP'])
plt.show()