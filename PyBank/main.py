import os
import csv

total_months = 0
net_total = 0
last_month = None
changelist = []
greatest_inc = 0
greatest_dec = 0
greatest_inc_month = ""
greatest_dec_month = ""

pybank_csv = os.path.join('Resources', 'budget_data.csv')

with open(pybank_csv) as csvfile:
    pydatacsv = csv.reader(csvfile, delimiter =',')
    next(pydatacsv)

    for row in pydatacsv:
        total_months += 1
        net_total += int(row[1])
        
        current_month = int(row[1])
        
        if last_month is not None:
            monthly_change = current_month - last_month
            changelist.append(monthly_change)
        
            if monthly_change > greatest_inc:
                greatest_inc = monthly_change
                greatest_inc_month = row[0]

            if monthly_change < greatest_dec:
                greatest_dec = monthly_change
                greatest_dec_month = row[0]

        last_month = current_month

    
    average_change = sum(changelist)/len(changelist)

    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: ${greatest_inc}")
    print(f"Greatest Decrease in Profits: ${greatest_dec}")
    print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")


op_path = os.path.join("analysis","financial_analysis.txt")

with open(op_path, "w") as txt:
    txt.write("Financial Analysis\n")
    txt.write("-----------------------------\n")
    txt.write(f"Total Months: {total_months}\n")
    txt.write(f"Total: ${net_total}\n")
    txt.write(f"Average Change: ${average_change:.2f}\n")
    txt.write(f"Greatest Increase in Profits: ${greatest_inc}\n")
    txt.write(f"Greatest Decrease in Profits: ${greatest_dec}\n")
    txt.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n")
    txt.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n")
