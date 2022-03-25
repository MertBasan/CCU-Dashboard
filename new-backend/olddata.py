import csv
import os 

def main(filepath): 
    table_data = []

    with open(filepath) as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            row_data = []
            row_data.append(row)

            if row[16] != "": # If BMI is known 
                if float(row[16]) >= 30 or float(row[16]) <= 18.5 and int(row[17]) == 0:
                    row_data.append(2) # If overweight/underweight FLAG
                else:
                    row_data.append(0)
            else: # Flag to know BMI 
                row_data.append(1)
            table_data.append(row_data) 
    return table_data

