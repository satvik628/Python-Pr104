# Python


#importing modules
import csv
from collections import Counter


# reading .csv file by with open only & adding newLine as empty and taking .csv file as ' f '
with open('dataPy/height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)

# Creating new_data variable as array to store data    
new_data=[]


# ranging length of file_data as i
for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(float(num))

n=len(new_data)

data=Counter(new_data)

# mode_data_for_range
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)


# print 
print(f"Mode is -> {mode:2f}")