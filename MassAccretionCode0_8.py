import sys
import os
import numpy as np
import pandas as pd
from scipy import stats  
import matplotlib
matplotlib.use( 'Agg' )
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#FUNCTIONS
#-------------------------------------
def plotMAtree( scale1, mass1, Vmaxarray):
	print("Entered Plot Function")
	plot_title="Mass Accretion History Tree "   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/Jan15TOTALMassAccretionfigure' +'.png')
	#Choose which type of plot you would like: Commented out.
	

	plt.plot(scale1, mass1, linestyle="", marker="o")
	#plt.plot(scale1, Vmaxarray, linestyle="-", marker="o")
	

	#plt.scatter(scale1, mass1, label="first tree")
	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	#plt.savefig(figure_name)
	#print("Saving plot: %s" % figure_name)
	print
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	#plt.clf()

	clearmass  = []
	clearscale = []
	clearVmax  = []
	return clearmass, clearscale, clearVmax

def plotMAtree2( scale1, mass1, Vmaxarray, half_formationscale, plotfunc_count):
	print("Entered Plot Function")
	plot_title="Mass Accretion History Tree "   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/Jan15TOTALMassAccretionfigure' +'.png')
	#Choose which type of plot you would like: Commented out.
	
	#plt.hist2d(scale1, mass1, (100, 100), cmap=plt.cm.jet)

	plt.plot(scale1, mass1, linestyle="", marker="o", markersize=3)
	#plt.plot(scale1, Vmaxarray, linestyle="-", marker="o")
	

	#plt.scatter(scale1, mass1, label="first tree")
	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	#plt.savefig(figure_name)
	#print("Saving plot: %s" % figure_name)
	print
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	#plt.clf()

	clearmass  = []
	clearscale = []
	clearVmax  = []
	plotfunc_count += 1
	return clearmass, clearscale, clearVmax, plotfunc_count

def plotMAtreeFINALhist( scale1, mass1, Vmaxarray, plotfunc_count):
	print("Entered Plot Function")
	plot_title="Mass Accretion History Histogram"   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/Jan15HISTMassAccretionfigure' +'.png')
	#Choose which type of plot you would like: Commented out.
	#yminv = 1000*2.57*10**8.
	yminv = 0 
	ymaxv = 2000*2.57*10**8.
	
	#The following code is to make the histogram appear much neater by eliminating values which are greatly out of range.

	plt.hist2d(scale1, mass1, (100, 500), cmap=plt.cm.jet, norm=matplotlib.colors.LogNorm() )
	plt.ylim([yminv, ymaxv])

	#plt.plot(scale1, mass1, linestyle="", marker="o", markersize=3, edgecolor='none')
	#plt.plot(scale1, Vmaxarray, linestyle="-", marker="o")
	

	#plt.scatter(scale1, mass1, label="first tree")
	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	plt.savefig(figure_name)
	print("Saving plot: %s" % figure_name)
	print
	
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	plt.clf()

	clearmass  = []
	clearscale = []
	clearVmax  = []
	plotfunc_count += 1
	#return clearmass, clearscale, clearVmax, plotfunc_count
	return

def plotMAslopes(HF_scales, beg_slopes, end_slopes, creation_scales, plotfunc_count):
	print("Entered Plot Function")
	plot_title="Mass Accretion History SLOPES v. FORMATION"   #Can code the number in with treemax
	x_axis="Half-Mass FORMATION"
	y_axis="Slope"
	figure_name=os.path.expanduser('~/Jan15MassAccretionSlopesVSformation' +'.png')
	#Choose which type of plot you would like: Commented out.
	#yminv = 1000*2.57*10**8.
	yminv = -0.3
	ymaxv = 0.3
	
	#The following code is to make the histogram appear much neater by eliminating values which are greatly out of range.

	#plt.hist2d(scale1, mass1, (200, 200), cmap=plt.cm.jet, norm=matplotlib.colors.LogNorm() )
	#plt.ylim([yminv, ymaxv])

	#plt.plot(scale1, mass1, linestyle="", marker="o", markersize=3, markeredgecolor='none')
	print("len: HF_scales, beg_slopes, end_slopes, creation_scales")
	print(" %d  %d  %d  %d  " % (len(HF_scales), len(beg_slopes), len(end_slopes), len(creation_scales)) )

	plt.plot(HF_scales, beg_slopes, linestyle="", marker="o")
	plt.plot(HF_scales, end_slopes, linestyle="", marker="o")
	#plt.plot(HF_scales, beg_slopes, color=creation_scales, linestyle="", marker="o")
	#plt.plot(HF_scales, end_slopes, color=creation_scales, linestyle="", marker="o")
	

	plt.plot(HF_scales, np.poly1d(np.polyfit(HF_scales, beg_slopes, 1))(HF_scales))
	plt.plot(HF_scales, np.poly1d(np.polyfit(HF_scales, end_slopes, 1))(HF_scales))
	

	#plt.scatter(scale1, mass1, label="first tree")
	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	plt.savefig(figure_name)
	print("Saving plot: %s" % figure_name)
	print
	
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	plt.clf()

	return


def generate_slope_points(scale1, mass1, Vmaxarray1, half_formationscale, plotfunc_count):
	beg_slopepoint = 1
	end_slopepoint = 1
	creation_scalepoint = 0.5

	num_points = 100

	try:
		beg_slopepoint, interjunk, rjunk, pjunk, errjunk = stats.linregress(scale1[0:100], mass1[0:100])
		end_slopepoint, interjunk, rjunk, pjunk, errjunk = stats.linregress(scale1[-100:], mass1[-100:])
	except:
		print("ERROR IN GENERATE SLOPE POINTS")
		pass

	creation_scalepoint = scale1[-1:]
	return beg_slopepoint, end_slopepoint, creation_scalepoint 

def plotdatatree(treeID, scale1, mass1):
	print("Entered Plot Function")
	plot_title="Mass Accretion History Tree " + str(treeID)   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/MassAccretionfigure' + str(treeID)+'.png')
	#Choose which type of plot you would like: Commented out.
	plt.plot(scale1, mass1, linestyle="-", marker="o")
	
	#plt.scatter(scale1, mass1, label="first tree")

	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	plt.savefig(figure_name)
	print("Saving plot: %s" % figure_name)
	print
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	plt.clf()

	clearmass = []
	clearscale = []

	return clearmass, clearscale

def checktreemax(totaltrees, treemax):
	if totaltrees >= treemax:
        	print("Totaltrees > treemax")
         	return True
	else:
		return False

def checkmaxiteration(icount, maxiteration1):
	if icount > maxiteration1:
                print("maxiterations reached!")
                print("Set iterations higher or reduce data!")
                print("Breaking Loop... ... ...")
                return True
	else:
		return False



#BEGIN MAIN PROGRAM
#-------------------------------------
print "Beginning Program!"
print "This code will read in many files and will creation accretion histories.."
print "From the file, specific masses can be checked."

print
print "Setting Date String"
datestring = "Jan15"

#Not used in code. check.
filedir="/zpool0/fs2/shared/new_130_mpc_box/hires/5045/rockstar_halos/so_m200b/trees/"
file_name="tree_0_0_0.dat"
fullfilepath=filedir+file_name
print fullfilepath
print

"""
NO. longer. accurate. January 15th. -----
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

mass1     =[]      #Initialized the mass array. Will store a single tree history
scale1    =[]      #Initialized the scale array. Will store a single tree history
Vmaxarray1=[]

massTOT      = []
scaleTOT     = []
VmaxarrayTOT = []

beg_slopes = []
end_slopes = []
HF_scales  = []
creation_scales = []

hashtrees=0   #The number of hashes found in file. Set counter to 0
scale1trees=0 # should be exactly the same as hashtrees
massprev=0
masscurr=0
massdiff=0
icount = 0    #counter set to 0 initially.
scalecount = 0
linestoskip=0 #functionality removed. used to skip sone lines/ scale factors.
plotfunc_count=0

trees=0      #How many trees have been evaluated. No trees found so far. 
treemin=1    #set the value to one for the first tree 
treemax=500000    #set value to (n+1) for n trees.
totaltrees=0  #The total trees generated. Set counter to 0

scale_previous=0 #Declare variable to hold previous line scale measurment
scale1bool   =0  #Initiially set to false meaning NOT on starting tree line
hashfound    =0  #Initially set to false meaning NOT on starting hash.
maxiteration1=400000000   #how many data points do you want to iterate over. Sets arbitrarily high. >50000

half_formationscale = 0.5

massbinminval = 10**11.0   #Sets minimum mass. Should eventually be set dependpent on particle number. 
massbinmaxval = 10**11.4   

particlemass = 2.57*(10**8.)
massbinminval = 1000*particlemass   #Sets minimum mass. Should eventually be set dependpent on particle number. 
massbinmaxval = 2000*particlemass   
goodmassvalue = 1 

#I want to add functionality so that you can specify a tree by either treename or number
#Check lines to make sure they are unique and no scales are skipped. 
datafilenamepath = '/scratch/chasonnscr/MassAccretionDataFiles/'

counter1 = 0
counter2 = 0
counter3 = 0

fileval1min=0
fileval1max=1

fileval2max=1
fileval3max=5
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("WARNING NOT USING ALL FILES.")


for counter1 in range(fileval1min, fileval1max):
	print("Counter1 = %d " % counter1)
	for counter2 in range(0, fileval2max):
		print("Counter2 = %d" % counter2)

		for counter3 in range(0, fileval3max):
			#datafilename = '/scratch/chasonnscr/MassAccretionDataFiles/MAdatafile0_0_0.txt'
			#datafilename = 'MAdatafile0_0_0.txt'
			print("Counter3 = %d" % counter3)
			datafilenamestring = 'MAdatafile' + str(counter1) + '_' + str(counter2) + '_' + str(counter3) + '.txt'
			datafilename = datafilenamepath + datafilenamestring

			if os.path.exists(datafilename):
				pass
			else:
				print("FILE DOES NOT EXIST. Continuing.")
				continue

			with open(datafilename) as fp:
				for line in fp:
					#print line
					if checktreemax(totaltrees, treemax):
						#break
						print("Max Trees Reached")
						pass		

					if checkmaxiteration(icount, maxiteration1):
						#break
						print("Max Iterations Reached.")
						pass

					#Determines what to do when encountering a New Tree as determined by HASH.
					if line.startswith("1.00000"):
						goodmassvalue = 1
						print line 
						if totaltrees == 0:
							totaltrees += 1
						else:
							totaltrees += 1		
							#mass1, scale1 = plotdatatree(treeID, scale1, mass1)
							#mass1, scale1, Vmaxarray1  =  plotMAtree(scale1, mass1, Vmaxarray1)
							if goodmassvalue ==1:
								#Find slopes of mass histories. 
								beg_slopepoint, end_slopepoint, creation_scalepoint = generate_slope_points(scale1, mass1, Vmaxarray1, half_formationscale, plotfunc_count)
								beg_slopes.append(beg_slopepoint)
								end_slopes.append(end_slopepoint)
								creation_scales.append(creation_scalepoint)
								HF_scales.append(half_formationscale)

								#PLOT THE MASS ACCRETION HISTORIES. ALL ON TOP OF EACH OTHER FOR: MAtree2()
								mass1, scale1, Vmaxarray1, plotfunc_count  =  plotMAtree2(scale1, mass1, Vmaxarray1, half_formationscale, plotfunc_count)
								print("PLot Function Count: %d" % plotfunc_count)
							
							scalecount = 0 
					if goodmassvalue == 0:
						continue		

					splitline = line.split()  #Divide the non-hashed data into splitline.
					    
					if line.startswith("1.00000"):   #Thus meaning a new halo at scale 1.0
						print("Line begins with 1.0000")
						treeID = splitline[1]    #If scale1.0, Assign halo ID as treeID name.
						initialmassval = float(splitline[2])
						#Checks whether the mass is in the specified bin. 
						if(massbinminval < initialmassval < massbinmaxval):
							print("Mass is in range.")
							goodmassvalue = 1  #A value of one will allow the accretion history to be made
						else:
							print("Bad Mass. %.2e " % initialmassval)
							goodmassvalue = 0  #A value of zero will skip the accretion history.
							continue

					scaleID = float(splitline[0])           #Sets scale ID
					haloID  = float(splitline[1])		#Sets halo ID. If 1.00 scale then same as treeID. 
					massval = float(splitline[2]) 
					Vmaxval = float(splitline[7])
					Pidval  = float(splitline[8])
					

					if massval >= 0.5*initialmassval:
						half_formationscale = scaleID

					if scaleID == 1.000 and Pidval != -1:
						goodmassvalue == 0
						print("scaleID=1.0 BUT Pid is not -1. Sub Halo Detected at Tree.")
						print("Skipping Tree... ")
						continue
					
					if scaleID == scale_previous:  #Only wish to plot one point per scale length!
						"""
						#Only contained continue before. Did not check for masses.
						#---------------
						continue           
						"""
						#Below Checks to see if masses at same scale are less. 
						massdiffval = mass_previous - massval
						if massdiffval > 0:
							#print("massdiffval at (%d) scale %.5f is GREATER than zero: %.2E  as expected! Moving on..." % (scalecount, scaleID, massdiffval))
							continue
						elif massdiffval < 0:
							print("FOUND A LARGER MASS AT SAME SCALE! Leaving Unchanged.")
							#print("Scale %d |  scale_prev |    Mass Previous   |    Mass Current    |    massdiff" % (scalecount))
							#print(" %.5f  |   %.5f   |     %.2E       |     %.2E       |    %.3E" % \
							#	 (scaleID, scale_previous,  mass_previous, massval, massdiffval))  
						elif massdiffval == 0:
							print("At scale (%d) The masses are equal. Thats quite unlikely unless min_mass." % scaleID)
						else:
							print("none executed. Check exemptions!")
							pass
					else:
						scalecount += 1
						scale1.append(scaleID)
						mass1.append(massval)
						Vmaxarray1.append(Vmaxval)

						scaleTOT.append(scaleID)
						massTOT.append(massval)
						VmaxarrayTOT.append(Vmaxval)

						scale_previous = scaleID
						mass_previous  = massval
					

					icount += 1           #Keep track of loop number. icount plus 1. 		
					#continue              #Go to next iteration of the loop. Currently redundant! 

					
				print("Finished the Primary FOR loop! Completing the rest of the program.")
			counter3 += 1
		counter2 += 1
	counter1 += 1


#mass1, scale1 = plotdatatree(treeID, scale1, mass1)
#mass1, scale1  = plotMAtree( scaleTOT, massTOT, VmaxarrayTOT)


figure_name=os.path.expanduser('~/Jan15MAhistorytree' +'.png')
plt.savefig(figure_name)
print("Saving plot: %s" % figure_name)
plt.clf()

plotMAslopes(HF_scales, beg_slopes, end_slopes, creation_scales, plotfunc_count)

plotMAtreeFINALhist(scaleTOT, massTOT, VmaxarrayTOT, plotfunc_count)

print("Program Completed. ")
