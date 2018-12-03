import matplotlib.pyplot as plt
import time 
import csv 
import numpy
import os
import math 


# A simple events logger that is triggered every time the return key
# is pressed. Optionally displays a plot of the times at which it was
# triggered, and/or a histogram of the number of trigger events within
# a certain interval throughout the period of data collection.


print("\n__________________________________________\n")
fname = input("Enter .csv filename. (e.g., timedata)\n")
showplot = input("Show plot of data after collection? (Y/N)\n").upper()

begin = input("Enter 'START' to begin.\n")
while(begin.upper() != "START"):
	begin = input("Enter 'START' to begin.\n")

start = float(time.time())
print("\n__________________________________________\n")
print("Data collection started!")
print("\n__________________________________________\n")

timedata = [] 
eventdata = []

print("Press enter key every time an event happens. \nEnter 'STOP' to end data collection.\n") 

while(True):
	event = input("") 
	if(event==""):
		now = float(time.time()); 
		timedata.append((now-start)*1000)
		eventdata.append(0)
		print("Event recorded at %.3f s \n Enter 'STOP' to end data collection."%(now-start))
	elif(event.upper()=="STOP"):
		print("\n__________________________________________\n")
		print("Data collection over!")
		print("\n__________________________________________\n")
		break; 
	else:
		print("Event not recorded. \nPress only the enter key every time an event happens.")

if(showplot=="Y"):
	plt.plot(timedata,eventdata,'o')
	plt.show()

if(not(fname.endswith('.csv'))):
	fname+=('.csv')

print("Saving file...\n")
numpy.savetxt(fname,(timedata))

print("Your file is saved as: "+os.getcwd()+'/'+fname)
print("\n__________________________________________\n")

showplot = input("Show histogram of data (Y/N)\n").upper()
interval=0
fname=""
if(showplot=="Y"):
	interval = int(float(input("Generate histogram data for intervals of how many seconds?\n"))*1000)
	fname = input("Enter .csv filename. (e.g., histogramdata)\n")
	b = numpy.arange(0,math.ceil(max(timedata)),interval)
	plt.hist(timedata,bins=b)
	plt.show()
	
print("\n__________________________________________\n")
