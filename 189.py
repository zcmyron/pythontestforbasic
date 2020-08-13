# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:27:14 2020

@author: Administrator
"""

import datetime

class User:
    """Storing User Information"""
    
    
    def __init__(self, full_name, birthday):
        self.name=full_name
        self.birthday=birthday
        
        name_splits=full_name.split(' ')
        self.first_name=name_splits[0]
        self.last_name=name_splits[-1]
    
    def age(self):
        """Calculate the age"""
        today=datetime.date(2020,8,13)
        
        years=int(self.birthday[0:4])
        months=int(self.birthday[4:6])
        days=int(self.birthday[6:8])
        
        
        birth_data=datetime.date(years,months,days)
        how_old_in_days=(today-birth_data).days
        how_old_in_years=how_old_in_days/365    

        return int(how_old_in_years)





user1=User('Daniel Zhai','19881015')

print(user1.last_name)
print(user1.age())