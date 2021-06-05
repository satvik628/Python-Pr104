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


n=len(new_data)

# sorting new data
new_data.sort()

if n%2==0:
    #getting the first number
     median1 = float(new_data[n//2])
     
      #getting the second number 
     median2 = float(new_data[n//2 - 1])

      #getting mean of those numbers

     median = (median1 + median2)/2

else:
    median = float(new_data[n//2]) 


# Printing median
print("Median Is : "+str(median))


