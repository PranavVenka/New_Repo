#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect',skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list
# Initialising employee list from the csv file.
employee_list = read_employees('C:\\Users\\Meena Natarajan\\Documents\\Python\\employees.csv')

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
               department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)

#Defining method to write report to a separate text file
def write_report(dictionary, report_file):
        with open(report_file, "w+") as file:
                for k in sorted(dictionary):
                        file.write(str(k)+' : '+str(dictionary[k])+'\n')
                file.close()
        
write_report(dictionary,'C:\\Users\\Meena Natarajan\\Documents\\Python\\report.txt')

