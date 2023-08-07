# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:50:44 2023

@author: Rehamath.Unnisa
"""


from Tenant import Tenant
from Payment import Payment
from Property import Property
import csv
import pandas as pd
from utils import display_tenant_data

class Propertymanagementsystem:
    def Payment_to_csv(file_path, data):
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['rental_id', 'address', 'payment_date', 'mode_of_payment', 'total_amount','amount_paid,''amount_pending','status']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            
            for payment in data:
                #writer.writerow({'rental_id': rental.rental_id, 'tenant_id': rental.tenant_id, 'property_id': rental.property_id, 'rental_start_date' : rental.rental_start_date, 'rental_end_date': rental.rental_end_date})
                writer.writerow([
                   payment.get_rental_id(),
                   payment.get_address(),
                   payment.get_payment_date(),
                   payment.get_mode_of_payment(),
                   payment.get_total_amount(),
                   payment.get_amount_paid(),
                   payment.get_amount_pending(),
                   payment.get_status()])

    def save_payment():
       
        payment1 = payment("R786", "T100", "P001", "2023-01-01", "2023-08-01")
        payment2 = payment("R787", "T101", "P002", "2022-01-01", "2023-01-01")
        payment3 = payment("R789", "T102", "P003", "2022-03-01", "2024-09-01")
        
       payment_data = [payment1, payment2, payment3]
        
        try:
            # Writing data to CSV file
            csv_file_path = "payment.csv"
           payment_to_csv(csv_file_path, Payment_data)
            print("Data has been written to 'payment.csv' successfully.")
        
        except:
            print("Error occured")
            raise
    
