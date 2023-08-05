# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 12:57:55 2023

@author: Ranadip.Dey
"""
from Tenant import Tenant
import csv
from utils import get_tenant_input



# List to store Tenant objects
tenants_list = []

# Get user input for tenants
num_tenants = int(input("Enter the number of tenants: "))
for _ in range(num_tenants):
    print(f"\nEnter details for Tenant {_ + 1}:")
    tenant = get_tenant_input()
    tenants_list.append(tenant)

# Appending data to CSV file
csv_file = "tenants_data.csv"

with open(csv_file, mode='a', newline='') as file:
    fieldnames = ["Tenant ID", "Name", "Contact Phone", "Contact Email", "Property ID"]
    writer = csv.writer(file)
    # Write the header row
    #writer.writerow(fieldnames)

    for tenant in tenants_list:
        writer.writerow([
            tenant.get_tenant_id(),
            tenant.get_name(),
            tenant.get_contact_phone(),
            tenant.get_contact_email(),
            tenant.get_property_id(),])
        #writer.writerow(tenant.to_dict())

print(f"\nData has been written to {csv_file}.")
