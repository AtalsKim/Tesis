import numpy
import scipy
import scipy.signal
import pylab
import csv


dbvls=numpy.genfromtxt("verticalloadsense.csv", delimiter=',')


theta=[]
VB1=[]
VB2=[]
VB3=[]
VB4=[]


for row in dbvls:
	theta.append(row[0])
	VB1.append(row[1])
	VB2.append(row[2])
	VB3.append(row[3])
	VB4.append(row[4])
	print row

#factor de conversion

theta=numpy.pi*numpy.array(theta)/180
VB1=40.*numpy.array(VB1)/1000000.
VB2=40.*numpy.array(VB2)/1000000.
VB3=40.*numpy.array(VB3)/1000000.
VB4=40.*numpy.array(VB4)/1000000.



pylab.polar(theta,VB1,theta,VB2,theta,VB3,theta,VB4)
pylab.show()


