print("Basic python lists")
name_list=[]
location_list=[]
contact_list =[]
name_entry=' '
location_entry=' '
count=1
while True:
    print("\t\t",count)
    condition=input("Enter 0 to exit and 1 to continue:")
    if condition == '0':
        break
    name_entry=input("Enter Name: ").title()
    contact_entry=int((input("Enter contact number: ")))
    location_entry=input("Enter location :").title()
    
    name_list.append(name_entry)
    location_list.append(location_entry)
    contact_list.append(contact_entry)
    count+=1

list=zip(name_list,contact_list,location_list)
for items in enumerate(list,1):
    print(items)