import pandas as pd
sheet1 = input("enter the file name:")
sheet2 = input("enter the file name:")
df1 = pd.read_csv(sheet1)
df2 = pd.read_csv(sheet2)

# To remove duplicates in file 1
df11 = df1.drop_duplicates(
    subset=['Controller_time'], keep='first').reset_index(drop=True)

# To remove duplicates in file 2
df21 = df2.drop_duplicates(
    subset=['Controller_time'], keep='first').reset_index(drop=True)

# To merge two files with common values
merged = pd.merge(df11, df21, on='Controller_time')
merged.to_csv("combined_file.csv", index=False)
print("It is saved")
