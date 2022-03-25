import csv
import os


def main(filepath):
    table_data = []

    with open(filepath) as f:
        data = csv.DictReader(f)
        next(data)
        for row in data:
            row_data = []
            row_data.append(row)

            if row["bmi"] != "":  # If BMI is known
                if float(row["bmi"]) >= 30 or float(row["bmi"]) <= 18.5 and int(row["referral"]) == 0:
                    row_data.append(2)  # If overweight/underweight FLAG
                else:
                    row_data.append(0)
            else:  # Flag to know BMI
                row_data.append(1)
            table_data.append(row_data)
    print(table_data[0])
    return table_data


UPLOAD_FOLDER = os.getcwd() + '/ccu-dashboard/backend/temp/'

main("/Users/kayleewilliams/Documents/Programming/Websites/ccu-dashboard/new-backend/temp/FeedingDashboarddata.csv")
