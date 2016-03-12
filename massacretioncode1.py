import sys
import os
import numpy as np
import matplotlib as plt
#import matplotlib.pyplot as plt



#FUNCTIONS
#-------------------------------------

def plotdatatree(treeID, scale1, mass1):
	plot_title="Mass Accretion History Tree " + str(treeID)   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/figureTree' + str(treeID))
	#Choose which type of plot you would like: Commented out.
	plt.plot(scale1, mass1, linestyle="-", marker="o")
	#plt.scatter(scale1, mass1, label="first tree")

	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	plt.savefig(figure_name)

	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	plt.clf()

	clearmass = []
	clearscale = []

	return clearmass, clearscale




#BEGIN MAIN PROGRAM
#-------------------------------------
print "Beginning Program!"
print "Make Certain the startsnap and endsnap are set properly!!!"
#Not used in code. check.
filedir="/zpool0/fs2/shared/new_130_mpc_box/hires/5045/rockstar_halos/so_m200b/trees/"
file_name="tree_0_0_0.dat"
fullfilepath=filedir+file_name
print fullfilepath

"""
SAMPLE DATA LINE NUMBERS (grep -n), SCALE FACTOR, ID,  MASS.
#FROM FUNCTION: grep -n "1.0000" | head ; on data...0.txt
50877:1.00000 9461448043 1.47700e+12
113407:1.00000 9461448327 1.45100e+12
139881:1.00000 9461448697 5.86500e+11
157968:1.00000 9461448330 5.54900e+11
176302:1.00000 9461448672 5.16700e+11
204905:1.00000 9461448686 4.46700e+11
219248:1.00000 9461448875 3.23067e+11
229150:1.00000 9461448909 3.14700e+11
243585:1.00000 9461448935 2.82800e+11
"""




mass1=[]
scale1=[]
hashtrees=0
scale1trees=0 #should be exactly the same as hashtrees
massprev=0
masscurr=0
massdiff=0
icount = 0 #counter set to 
linestoskip=0
trees=0
totaltrees=0 #counter set to 0
treemin=1 #set the value to one for the first tree 
treemax=2 #set value to treemin+1 for two tree.
scale_previous=0 #Declare variable to hold previous line scale measurment
scale1bool=0  #Initiially set to false meaning NOT on starting tree line
hashfound=0
maxiteration1=400000000   #how many data points do you want per tree

with open('datafile0.txt') as fp:
	for line in fp:
		if totaltrees >= treemax:
		    break 
		
		if icount > maxiteration1:
			break
			print "It did not break at max iteration"

		if line.startswith("#"):
			hashtrees += 1
	 		print "Found a, #, thus new tree...Moving to next line"
			if totaltrees == 0:
				totaltrees += 1
				continue
			else:
				#Plot the data and clear the arrays so not to overplot data
		  		mass1, scale1 = plotdatatree(treeID, scale1, mass1)
		  		
		  			
		splitline = line.split()
				    
		if line.startswith("1.00000"):
			print("Line begins with 1.0000")
			treeID = splitline[1]

		scaleID = splitline[0] 
		if scaleID == scale_previous:
			continue
		else:
			scale1.append(splitline[0])
			mass1.append(splitline[2])
			scale_previous = scaleID
		
		icount += 1
		
		continue

		
	print("Finished the FOR loop! Completing the rest of the program.")
