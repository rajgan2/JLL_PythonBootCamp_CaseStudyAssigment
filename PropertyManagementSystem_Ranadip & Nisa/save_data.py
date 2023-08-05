# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:51:01 2023

@author: Ranadip.Dey
"""
from Tenant import Tenant
from Rental import Rental 
from Property import Property
import csv
import pandas as pd


#-----Save rental data to CSV
#==============================
def rental_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['rental_id', 'tenant_id', 'property_id', 'rental_start_date', 'rental_end_date']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        
        for rental in data:
            #writer.writerow({'rental_id': rental.rental_id, 'tenant_id': rental.tenant_id, 'property_id': rental.property_id, 'rental_start_date' : rental.rental_start_date, 'rental_end_date': rental.rental_end_date})
            writer.writerow([
                rental.get_rental_id(),
                rental.get_tenant_id(),
                rental.get_property_id(),
                rental.get_rental_start_date(),
                rental.get_rental_end_date(),])

def save_rental():
   
    rental1 = Rental("R123", "T001", "P1000", "2023-08-01", "2023-09-01")
    rental2 = Rental("R124", "T002", "P1001", "2022-01-01", "2023-01-01")
    rental3 = Rental("R125", "T003", "P1002", "2022-03-01", "2024-09-01")
    
    Rental_data = [rental1, rental2, rental3]
    
    try:
        # Writing data to CSV file
        csv_file_path = "Rental.csv"
        rental_to_csv(csv_file_path, Rental_data)
        print("Data has been written to 'Rental.csv' successfully.")
    
    except:
        print("Error occured")
        raise
                

#-----Save tenant data to CSV
#==============================
def tenant_to_csv(csv_file, tenants_list):
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["Tenant ID", "Name", "Contact Phone", "Contact Email", "Property ID"]
        writer = csv.writer(file)
    
        # Write the header row
        writer.writerow(fieldnames)
    
        # Write each Tenant object's data as a row
        for tenant in tenants_list:
            #writer.writerow(tenant.to_dict())
            writer.writerow([
                tenant.get_tenant_id(),
                tenant.get_name(),
                tenant.get_contact_phone(),
                tenant.get_contact_email(),
                tenant.get_property_id(),])
    print(f"Data has been written to {csv_file}.")
 

def find_rental_end_date(rental_id):
    df_rental = pd.read_csv("Rental.csv")
    end_date= df_rental.loc[df_rental["rental_id"]==rental_id, "rental_end_date"]
    return end_date.values[0]

#-----Save property data to CSV
#==============================
def property_to_csv(csv_file, property_list):
        
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["property_id","address", "num_bedrooms", "num_bathrooms", "monthly_rent", "status"]
        writer = csv.writer(file)
    
        # Write the header row
        writer.writerow(fieldnames)
    
        # Write each Tenant object's data as a row
        for prop in property_list:
            #writer.writerow(tenant.to_dict())
            writer.writerow([
                prop.get_property_id(),
                prop.get_address(),
                prop.get_num_bedrooms(),
                prop.get_num_bathrooms(),
                prop.get_monthly_rent(),
                prop.get_status(),])
            
    print(f"Data has been written to {csv_file}.")




if __name__ == "__main__":

    try:
        # Save rental data to CSV    
        save_rental()


        # create instance, prepare tenant data
        tenant1 = Tenant("T123", "John Kennedy", "1234554321", "john@example.com", "P1000")
        tenant2 = Tenant("T456", "Jane Smith", "6758909876", "jane@example.com", "P1001")
        tenant3 = Tenant("T789", "Mike Hall", "6763478792", "Mike@example.com", "P1002")
        # List of Tenant objects
        
        tenants_list = [tenant1, tenant2,  tenant3]
        
        # Writing tenant data to CSV file
        csv_file = "tenants_data.csv"
        tenant_to_csv(csv_file, tenants_list)

        # property data
        # create instance, prepare property data
        end_date=find_rental_end_date("R125")
 
        property1 = Property(" Piedmont Rd NE Georgia", "2","3","12000",end_date)
        property2 = Property("Southfront Rd Livermore	California", "2","2","20000", end_date)
        property3 = Property("Whitefield, Bangalore", "2","3","35000", end_date)

        property_list = [property1,property2,property3]
        # Writing tenant data to CSV file
        p_csv_file = "property_data.csv"
        property_to_csv(p_csv_file,property_list )
        
    except:
        print("Something went wrong.")
        raise
        
    