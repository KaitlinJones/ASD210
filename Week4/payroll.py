"""
Program: payroll.py
Project 4.12
Print a payroll report.
Input
   A file in which each line has the form
   
   <last name> <hourly wage> <hours worked>
Output
   A report in tabular format.  Each line has the form
   <last name> <hours worked> <total wages>
   
"""
# Take the inputs
fileName = input("Enter the file name: ")
# Open the input file
inputFile = open(fileName, 'r')
# Read the data and print the report
print("%-15s%-15s%-20s%7s%15s" % ("Employee Num","Name","Address", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    emp_num = int(dataList[0])
    name = dataList[1]
    st_num = int(dataList[2])
    st_name = dataList[3]
    st_type = dataList[4]
    hours = int(dataList[5])
    payRate = float(dataList[6])
    totalPay = hours * payRate
    print("%-15s%-15s%-5d%-10s%-3s%6d%15.2f" % (emp_num, name, st_num, st_name, st_type, hours, totalPay))
    