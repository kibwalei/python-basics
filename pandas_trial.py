import pandas as pd

names=[]
locations=[]
ages=[]
genders=[]
count=1
number=int(input("Enter the number of Data: "))
while count<(number + 1):
    print("\t",count)
    name=input("Enter name:")
    location=input("Enter location:")
    age=int(input("Enter age:"))
    gender=input("Enter gender:")
    count+=1
    names.append(name)
    locations.append(location)
    ages.append(age)
    genders.append(gender)
df=pd.DataFrame({
    "NAME": (i for i in names),
    "LOCATION": (i for i in locations),
    "AGE":(i for i in ages),
    "GENDER":(i for i in genders)
})
df.insert(4,"UNIVERSITY" , "DeKUT")#inserting a third column with static value
df.head()
print(df)