import pandas as pd

n = int(input("Enter number of sheets:"))
li = []
for i in range(n):
    sheet = input("enter the file name:")
    df1 = pd.read_csv(sheet)
    li.append(df1)


# To remove duplicates in file
for i in range(n):
    li[i] = li[i].drop_duplicates(
        subset=['Controller_time'], keep='last').reset_index(drop=True)

# To merge the files
merged = pd.merge(li[0], li[1], on='Controller_time')

for i in range(2, n):
    merged = pd.merge(merged, li[i], on='Controller_time')

merged.to_csv("combined_file.csv", index=False)
print("It is saved")
