# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:47:22 2023

@author: Ranadip.Dey
"""

class Rental:
    def __init__(self, rental_id, tenant_id, property_id, rental_start_date, rental_end_date):
        self._rental_id = rental_id
        self._tenant_id = tenant_id
        self._property_id = property_id
        self._rental_start_date = rental_start_date
        self._rental_end_date = rental_end_date


    # Getter methods
    def get_rental_id(self):
        return self._rental_id

    def get_tenant_id(self):
        return self._tenant_id

    def get_property_id(self):
        return self._property_id

    def get_rental_start_date(self):
        return self._rental_start_date

    def get_rental_end_date(self):
        return self._rental_end_date

    # Setter methods
    def set_rental_id(self, rental_id):
        self._rental_id = rental_id

    def set_tenant_id(self, tenant_id):
        self._tenant_id = tenant_id

    def set_property_id(self, property_id):
        self._property_id = property_id

    def set_rental_start_date(self, rental_start_date):
        self._rental_start_date = rental_start_date

    def set_rental_end_date(self, rental_end_date):
        self._rental_end_date = rental_end_date




        
