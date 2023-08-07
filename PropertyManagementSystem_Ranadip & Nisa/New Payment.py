# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:58:24 2023

@author: Rehamath.Unnisa
"""

class Payment:
    def __init__(self,rental_id,address,payment_date,mode_of_payment,total_amount, amount_paid, amount_pending, status):
        self.rental_id = rental_id
        self.address = address
        self.payment_date = payment_date
        self.total_amount = total_amount
        self.mode_of_payment= mode_of_payment
        self.amount_paid = amount_paid
        self.amount_pending = amount_pending
        self.status = status

    # Getters and Setters
    def get_rental_id(self):
        return self.rental_id

    def set_rental_id(self, rental_id):
        self.rental_id = rental_id

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount

    def get_payment_date(self):
        return self.payment_date

    def set_payment_date(self, payment_date):
        self.payment_date = payment_date

    def get_mode_of_payment(self):
        return self.mode_of_payment

    def set_monthly_rent(self, mode_of_payment):
        self.mode_of_payment = mode_of_payment
        
    def get_amount_paid(self):
        return self.amount_paid
                
    def set_amount_paid(self,amount_paid):
        return self.amount_paid
      
    def get_amount_pending(self):
        return self.amount_pending
        
    def set_amount_pending(self,amount_pending):
        self.amount_pending = amount_pending 

    def set_status(self, status):
        self.status = status
        
    def get_status(self):
        return self.status
    
   
    # Methods for changing the property status
    def _open(self):
        self.status = "_open"

    def close(self):
        self.status = "close"
