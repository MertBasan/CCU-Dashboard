import csv
import os 

def main(filepath): 
    table_data = []

    with open(filepath) as f:
        data = csv.DictReader(f)
        next(data)
        for row in data:
            row_data = row

            if row["bmi"] != "": # If BMI is known 
                if row["referral"] == '0.0':
                    if float(row["bmi"]) >= 30 or float(row["bmi"]) <= 18.5 and row["referral"] == '0.0':
                        row_data["flag"] = 2 # If overweight/underweight FLAG
                    else:
                        row_data["flag"] = 0
            else: # Flag to know BMI 
                row_data["flag"] = 1

            if row_data['encounterId'] == "3595":
                print(row_data)
            table_data.append(row_data) 
    return table_data

