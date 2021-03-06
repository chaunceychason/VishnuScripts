import sys
import os
import numpy as np
#import pickle
#import pandas as pd
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
	

	plt.plot(scale1, mass1, linestyle="", marker="o", markeredgecolor=None, markeredgewidth=0.0)
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

	#yminv = -0.3
	#ymaxv = 0.3
	
	#The following code is to make the histogram appear much neater by eliminating values which are greatly out of range.

	#plt.hist2d(scale1, mass1, (200, 200), cmap=plt.cm.jet, norm=matplotlib.colors.LogNorm() )

	#plt.plot(scale1, mass1, linestyle="", marker="o", markersize=3, markeredgecolor='none')
	print("len: HF_scales, beg_slopes, end_slopes, creation_scales")
	print(" %d  %d  %d  %d  " % (len(HF_scales), len(beg_slopes), len(end_slopes), len(creation_scales)) )

	plt.plot(HF_scales, beg_slopes, 'b', linestyle="", marker="o")
	plt.plot(HF_scales, end_slopes, 'r', linestyle="", marker="o")
	#plt.plot(HF_scales, beg_slopes, color=creation_scales, linestyle="", marker="o")
	#plt.plot(HF_scales, end_slopes, color=creation_scales, linestyle="", marker="o")
	

	plt.plot(HF_scales, np.poly1d(np.polyfit(HF_scales, beg_slopes, 1))(HF_scales), 'b')
	plt.plot(HF_scales, np.poly1d(np.polyfit(HF_scales, end_slopes, 1))(HF_scales), 'r')
	#plt.plot(HF_scales, np.poly1d(np.polyfit( beg_slopes, HF_scales, 1))(beg_slopes), 'b')
	#plt.plot(HF_scales, np.poly1d(np.polyfit( end_slopes, HF_scales, 1))(end_slopes), 'r')
	
	#plt.ylim([yminv, ymaxv])	
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

	num_points = 75

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

mass1      =[]      #Initialized the mass array. Will store a single tree history
scale1     =[]      #Initialized the scale array. Will store a single tree history
Vmaxarray1 =[]
haloIDarray=[]

massTOT      = []
scaleTOT     = []
VmaxarrayTOT = []

beg_slopes = []
end_slopes = []
HF_scales  = []
creation_scales = []

hashtrees=0   #The number of hashes found in file. Set counter to 0
scale1trees=0 # should be exactly the same as hashtrees
stored_counter = 0
unstored_counter = 0

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

fileval2max=6
fileval3max=10

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
						#Sets Good Mass Value to show a proper tree has been found. 
						goodmassvalue = 1
						print line 
						if totaltrees == 0:
							totaltrees += 1
						else:
							pass	
							#mass1, scale1 = plotdatatree(treeID, scale1, mass1)
							#mass1, scale1, Vmaxarray1  =  plotMAtree(scale1, mass1, Vmaxarray1)
							if goodmassvalue ==1:
								#Find slopes of mass histories. 
								#beg_slopepoint, end_slopepoint, creation_scalepoint = generate_slope_points(scale1, mass1, Vmaxarray1, half_formationscale, plotfunc_count)
								#beg_slopes.append(beg_slopepoint)
								#end_slopes.append(end_slopepoint)
								#creation_scales.append(creation_scalepoint)
								#HF_scales.append(half_formationscale)

								#PLOT THE MASS ACCRETION HISTORIES. ALL ON TOP OF EACH OTHER FOR: MAtree2()
								totaltrees += 1	
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
							stored_counter += 1
							goodmassvalue = 1  #A value of one will allow the accretion history to be made
						else:
							print("Bad Mass. %.2e " % initialmassval)
							unstored_counter += 1
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
						
						'''
						DEFINE PRIMARY DATA ARRAYS
						'''
						haloIDarray.append(haloID)
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

figure_name=os.path.expanduser('~/Mar10MAhistorytree' +'.png')
plt.savefig(figure_name)
print("Saving plot: %s" % figure_name)
plt.clf()

#plotMAslopes(HF_scales, beg_slopes, end_slopes, creation_scales, plotfunc_count)

plotMAtreeFINALhist(scaleTOT, massTOT, VmaxarrayTOT, plotfunc_count)
plt.clf()

"""
PARSE RESULTS TO DETERMINE MASSS DISTRIBUTION AT SCALE. 

"""
print("BEGIN PARSE RESULTS:  ....")
print("-----------------------------------------")
print("Length of scale1: %d " % len(scale1))
print("Length of scaleTOT: %d " % len(scaleTOT))
print("Length of mass1: %d " % len(mass1))
print("Length of massTOT: %d " % len(massTOT))
print("Lenth of stored_counter: %d " % stored_counter)
print("Lenth of unstored_counter: %d " % unstored_counter)

#Sort by scale time to find the masses. 
scale_init = 0.1  #Set early. slightly past 0 since trees dont begin at 0 time.
scale_epsilon = 0.000000001  #Set to small non-zero value smaller than smallest scale difference. 
scale_current = scale_init 
scale_final = 1.0
temp_scale = 0
#mass_scale = [][]
mass_scales = []
scales_for_mass_scales = []
halo_id_for_mass_scale = []
median_scales = []
p35_scales = []
p65_scales = []
p95_scales = []
p05_scales = []

median_mass_scales = []
temp_scale_masses = []

#scale_ListSorted = np.unique(np.sort(scaleTOT)) 
#Read in File or sort scale times to make file. 
if os.path.isfile( 'scale_list.txt' ):
	#with open('scale_list.txt' , 'r') as the_file: 
	print("Reading in file with all scales for scale_list.")
		#scale_ListSorted = the_file.read().splitlines()
	scale_ListSorted = np.loadtxt('scale_list.txt')
		#for item in scale_ListSorted:
		#	print>>the_file , item
else:
	print("Creating a file using scale list...")
	print("Sorting List to store....")
	scale_ListSorted = np.sort(np.unique(scaleTOT), kind= 'mergesort') 
	with open('scale_list.txt' , 'w') as the_file: 
		#for item in scale_ListSorted:
			#printf >> the_file , item
		#pickle.dump(np.ndarray.dump(scale_ListSorted), the_file)
		#for item in scale_ListSorted:
		np.savetxt('scale_list.txt', scale_ListSorted)

print("Computing statistics about the mass accretion histories by scales. ")

#Loops through all the represented scales to create list of elements in proper order. 
"""
for idx1, scale_ticker in enumerate(scale_ListSorted):
	#Loops through all scales to find the distribution of masses by scale. 
	for idx2, scaleval in enumerate(scaleTOT):
		if scaleval == scale_ticker:
			halo_id_for_mass_scale.append(haloIDarray[idx2])
			mass_scales.append(massTOT[idx2])
			temp_scale_masses.append(massTOT[idx2])
			scales_for_mass_scales.append(scale_ticker)
			#mass_scale[idx1].append(massTOT[idx2])

	print("Computing Stats for scale: %f" % scale_ticker)
	p65_scales.append( np.percentile(temp_scale_masses, 65.  ) )
	p35_scales.append( np.percentile(temp_scale_masses, 35. ) )
	p95_scales.append( np.percentile(temp_scale_masses, 95.  ) )
	p05_scales.append( np.percentile(temp_scale_masses, 05. ) )
	median_scales.append( np.ma.median( temp_scale_masses ) )

	temp_scale_masses[:] = []
"""

"""
SORTS SCALES AND FINDS MEDIAN MASS ACCRETION HISTORY AND STATS. 
"""
p25bool = 0
p50bool = 0
p75bool = 0
#Define numpy array np_MassTOT so it can recieve multiple indexes. 
np_MassTOT = np.array(massTOT)
for idx1, scale_ticker in enumerate(scale_ListSorted):
	np_scale_idxs = np.where( scaleTOT == scale_ticker )[0]
	temp_scale_masses = np_MassTOT[[np_scale_idxs]]
	p65_scales.append( np.percentile(temp_scale_masses, 65.  ) )
	p35_scales.append( np.percentile(temp_scale_masses, 35. ) )
	p95_scales.append( np.percentile(temp_scale_masses, 95.  ) )
	p05_scales.append( np.percentile(temp_scale_masses, 05. ) )
	median_scales.append( np.ma.median( temp_scale_masses ) )


	if (float(idx1) >= (0.25*float(len(scale_ListSorted))) and p25bool==0):
		print("Reached 25% ...")
		p25bool = 1
	if (float(idx1) >= (0.50*float(len(scale_ListSorted))) and p50bool == 0):
		print("Reached 50% ...")
		p50bool = 1
	if (float(idx1) >= (0.75*float(len(scale_ListSorted))) and p75bool==0):
		print("Reached 75% ...")
		p75bool = 1
	#temp_scale_masses[:] = []


print("Length of scalesformassscales: %d " % len(scales_for_mass_scales))
print("Length of mass_scales: %d " % len(mass_scales))
print("Length of median_scales: %d " % len(median_scales))
print("Length of p65_scales:  %d " % len(p65_scales))


#plt.scatter(scales_for_mass_scales, mass_scales)

plt.scatter( scale_ListSorted, p95_scales,  c='g' , s=3, alpha=0.5 , lw = 0 , label = '95th % ')
plt.scatter( scale_ListSorted, p65_scales,  c='b' , s=3, alpha=0.75, lw = 0 , label = '65th % ')

plt.scatter( scale_ListSorted, median_scales ,  c='r', s=7, lw = 0, label='median' )

plt.scatter( scale_ListSorted, p35_scales , c='b' , s=3, alpha=0.75, lw = 0 , label = '35th % ')
plt.scatter( scale_ListSorted, p05_scales , c='g' , s=3, alpha=0.5 , lw = 0 , label = ' 5th % ')
plt.legend(loc='best')







figure_name=os.path.expanduser('~/Mar10MAmedianNew' +'.png')
plt.savefig(figure_name)
print("Saving plot: %s" % figure_name)
plt.clf()


print("Program Completed. ")
