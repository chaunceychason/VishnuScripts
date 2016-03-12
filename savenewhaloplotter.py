import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use( 'Agg' )
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
"""
#THIS PROGRAM PLOTS DATA IN FORM 'x, y'
#Code to initialize latex font
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
"""
#FUNCTIONS
#-------------------------------------




#BEGIN MAIN PROGRAM
#-------------------------------------
print "Beginning Program!"
print "Make Certain the startsnap and endsnap are set properly!!!"
#Not used in code. check.
filedir="/zpool0/fs2/shared/new_130_mpc_box/hires/5045/rockstar_halos/so_m200b/trees/"
file_name="tree_0_0_0.dat"  
fullfilepath=filedir+file_name
print fullfilepath
#f = open(fullfilepath, 'r')

"""
SAMPLE DATA LINE NUMBERS (grep -n), SCALE FACTOR, ID,  MASS. 
FROM FUNCTION: grep -n "1.0000" | head ; on data...0.txt
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
#massdata, xdata, ydata, zdata = np.loadtxt(f, usecols=(10,17,18,19), skiprows=50)
#print xdata

mass1=[]
scale1=[]
massevo=0
masspri=0
massdiff=0
icount = 0 #counter set to 0
linestoskip=0
trees=0 #counter set to 0
treemin=2 #set the value to one for the first tree 
treemax=3 #set value to treemin+1 for one tree.
scale_previous=0
maxiteration1=400000000   #how many data points do you want per tree

with open('datafile0.txt') as fp:
	for line in fp:
		if line.startswith("#"):
	 		print "Found a new tree"
			continue
		if line.startswith("1.00000"):
			trees += 1
		if line.startswith("1.00000") and trees>=treemax:
			print "Found a new tree! Breaking loop!"
			break
		
		splitline = line.split()
		
		#3 conditions: Tree must be current,  scale length should be uniq, icount must be below max
		if trees>=treemin and scale_previous!=splitline[0] and (icount<2 or (icount%(linestoskip+1))==0):
			print line
			scale1.append(splitline[0])
			mass1.append(splitline[2])
		
		scale_previous = splitline[0] 
		if icount > maxiteration1:
			break
			print "It did not break"
		icount += 1


				
			

#PLOTTING
#-------------------------------------
plot_title="Mass Accretion History Tree %d" % (treemin)   #Can code the number in with treemax
x_axis="scale time"
y_axis="mass"

#Choose which type of plot you would like: Commented out.
plt.plot(scale1, mass1)
#plt.scatter(scale1, mass1, label="first tree")

plt.title(plot_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
#plt.yscale("log")

plt.savefig("figure.png")

