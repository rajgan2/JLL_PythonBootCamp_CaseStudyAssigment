# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:48:31 2023

@author: Ranadip.Dey
"""
from datetime import date
from datetime import datetime

class Property:
    
    property_id_counter = 1000
    
    def __init__(self,  address, num_bedrooms, num_bathrooms, monthly_rent, end_date):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.monthly_rent = monthly_rent
        self.property_id= Property.property_id_counter
        Property.property_id_counter += 1 
        self.end_date= end_date
        self.update_status()
        

    # Getters and Setters
    
    def get_property_id(self):
        return "P" + str(self.property_id)

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_num_bedrooms(self):
        return self.num_bedrooms

    def set_num_bedrooms(self, num_bedrooms):
        self.num_bedrooms = num_bedrooms

    def get_num_bathrooms(self):
        return self.num_bathrooms

    def set_num_bathrooms(self, num_bathrooms):
        self.num_bathrooms = num_bathrooms

    def get_monthly_rent(self):
        return self.monthly_rent

    def set_monthly_rent(self, monthly_rent):
        self.monthly_rent = monthly_rent

    def get_status(self):
        return self.status

#    def set_status(self, status):
#        self.status = status

    # Methods for changing the property status
    def update_status(self):
        
        if datetime.strptime(self.end_date,'%Y-%m-%d')> datetime.now():
            self.status = "Occupied"
        else:
            self.status = "Vacant"

