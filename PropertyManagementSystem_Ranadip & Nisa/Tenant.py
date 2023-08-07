# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:43:48 2023

@author: Ranadip.Dey
"""


class Tenant:
    def __init__(self, tenant_id, name, contact_phone, contact_email, property_id):
        self._tenant_id = tenant_id
        self._name = name
        self._contact_phone = contact_phone
        self._contact_email = contact_email
        self._property_id = property_id

    # Getter methods
    def get_tenant_id(self):
        return self._tenant_id

    def get_name(self):
        return self._name

    def get_contact_phone(self):
        return self._contact_phone

    def get_contact_email(self):
        return self._contact_email

    def get_property_id(self):
        return self._property_id

    # Setter methods
    def set_tenant_id(self, tenant_id):
        self._tenant_id = tenant_id

    def set_name(self, name):
        self._name = name

    def set_contact_phone(self, contact_phone):
        self._contact_phone = contact_phone

    def set_contact_email(self, contact_email):
        self._contact_email = contact_email

    def set_property_id(self, property_id):
        self._property_id = property_id

    def to_dict(self):
        return {
            "Tenant ID": self._tenant_id,
            "Name": self._name,
            "Contact phone": self._contact_phone,
            "Contact email": self._contact_email,
            "Property ID": self._property_id
        }
    
    

