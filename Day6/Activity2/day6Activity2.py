from GrossSalary import *
from NetSalary import *
from SalaryDeductions import *

name = input("Name: ")
hour = int(input("Hour: "))

grossSalary = computeGrossSalary(hour)
tax = computeTax(grossSalary)

print(f"\nGross Salary: {grossSalary:.2f}")

print(f"\nTax: {tax:.2f}")
loan = float(input("Loan: "))
health_insurance = float(input("Insurance: "))

totalDeduction = computeTotalDeduction(tax, loan, health_insurance)
print(f"\nTotal Deductions: {totalDeduction:.2f}")

netSalary = computeNetSalary(grossSalary, totalDeduction)
print(f"\nNet Salary: {netSalary:.2f}")