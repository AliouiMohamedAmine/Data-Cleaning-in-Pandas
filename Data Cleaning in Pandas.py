import pandas as pd
#importing our data
df = pd.read_excel(r"C:\Users\MOHAMED\Downloads\Customer
Call List.xlsx")

#First we need to delete duplicates from our table
df = df.drop_duplicates()

#Then drop the columns that we are not gonna use
df = df.drop(columns = "Not_Useful_Column")

#We are going to clean the names from other caracters
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

#And the number column also
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','', regex=True)

#After that creating sort of model for numbers
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

#Spliting the adress to 3 other columns
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n=2, expand=True)

#More cleaning
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df = df.replace('N/a','')
df = df.replace('NaN','')
df=df.fillna('')

#Here we are going to deltee the customers that they do not want contact
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)



#Another way to drop null values
#df = df.dropna(subset="Phone_Number"), inplace=True)
df = df.reset_index(drop=True)

