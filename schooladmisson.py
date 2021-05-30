import csv
            
with open("school.csv","r") as f:
    x= f.readlines()
    for line in x[1:]:
        k = line.strip().split()
        print(f"The name of the student is {k[0]} , age is {k[1]} , and they got {k[2]}")
