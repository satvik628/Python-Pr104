# Python

#importing CSV module
import csv

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


# Putting length of new_data in variable 'n'
n=len(new_data)
total=0


# looping for in new_data as i to add data in total variable
for i in new_data:
    total+=i

# Finding mean by '/' dividing total by n and storing it in 'mean' variable
mean=total/n

# Printing mean
print("The mean is -->  "+str(mean))


    