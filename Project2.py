#Program developed by Sam Espana 
#Program enhanced by Nolan Becker 
#Date: 2/20/2025

#Imports datetime API and prints the current date #string format for date showing month, day year. (ENHANCEMENT)
from datetime import date
today = date.today()
todaysdate = today.strftime('%B %d, %Y')
print('Todays Date is', todaysdate)

#INPUTS
print('Vital Signs Program')
strFirst = input('Enter First name: ')
strLast = input('Enter Last name: ')
fltFahrenheit = float(input('Enter temperature in Fahrenheit degrees: '))
intPulse = int(input('Enter pulse/minute: '))
intRespiration = int(input('Enter breaths/minute: '))
strBloodPressure = input('Enter blood pressure (Systolic/Diastolic: ')

#PROCESSING-CLACULATIONS 
print('\n  Calculating Celsius \n')
fltCelsius = (fltFahrenheit - 32)/1.8 #Converting Fahrenheit to Celsius

#OUTPUTS
print('Vital Signs Report\n')
print('Welcome '+strFirst+' '+strLast)
print('Temperature in Fahrenheit degrees = ' ,fltFahrenheit)
print('Temperature in Celsius degrees = %.2f' %fltCelsius)
print('Pulse/Minute = ',intPulse)
print('Respiration/Minute = ',intRespiration)
print('Blood Pressure (Systolic/Diastolic) = ',strBloodPressure) 

#PRINT-NAME (ENHANCEMENT)
print('Nolan Becker')
