import pandas as pd


#df_rental = pd.read_csv("Rental.csv")
#max_rental_id = df_rental['rental_id'].max()
#print(max_rental_id)

#This function read rental_end_date from Rental data 
def find_rental_end_date(rental_id):
    df_rental = pd.read_csv("Rental.csv")
    end_date= df_rental.loc[df_rental["rental_id"]==rental_id, "rental_end_date"]
    return end_date


#This function update Tenant phone number based on name
def updateTenant(tenant_name, new_phone):
    try:
        #read the tenant data
        df_tenant = pd.read_csv("tenants_data.csv")
        phone = df_tenant.loc[df_tenant["Name"]==tenant_name,"Contact Phone"]
        print("Current Contact number :", phone.values[0])
        row_num = df_tenant[df_tenant["Name"] == tenant_name].index 
        print("Row Number : ", row_num.values[0])
        df_tenant.loc[row_num.values[0],"Contact Phone"] = new_phone
        df_tenant.to_csv("tenants_data.csv")
        print("Record updated successfully...")
        
    except IndexError:
        print("Invalid input, name not found in Database.")
    
    
## Call updateTenant function, get user input and update phone number
name = input("Please Enter Name: ")    
phone = input("Enter correct phone number :")
updateTenant(name, phone)    
