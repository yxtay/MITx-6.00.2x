# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def generatePatients(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                     mutProb, numTrials):
        patients = []
        for _ in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) \
                        for _ in range(numViruses)]
            patients.append(TreatedPatient(viruses, maxPop))
        return patients
            
    def simulateStepsWithDelay(patients, delay):
        for _ in xrange(delay):
            [patient.update() for patient in patients]
        [patient.addPrescription('guttagonol') for patient in patients]
        for _ in xrange(150):
            [patient.update() for patient in patients]
        return patients
        
    def plotVirusPop(virusPop, delay):
        pylab.hist(virusPop, bins = 10)
        pylab.title('Delay = %d' % delay)
#        pylab.xlabel('Total Virus Population')
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    
    pylab.figure()
    delays = [300, 150, 75, 0]
    for i in xrange(len(delays)):
        patients = generatePatients(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                     mutProb, numTrials)
        patients = simulateStepsWithDelay(patients, delays[i])
        virusPop = [patient.getTotalPop() for patient in patients]
        pylab.subplot(2, 2, i + 1)
        plotVirusPop(virusPop, delays[i])
    pylab.show()



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def generatePatients(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                     mutProb, numTrials):
        patients = []
        for _ in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) \
                        for _ in range(numViruses)]
            patients.append(TreatedPatient(viruses, maxPop))
        return patients
            
    def simulateStepsWithDelay(patients, delay):
        for _ in xrange(150):
            [patient.update() for patient in patients]
        [patient.addPrescription('guttagonol') for patient in patients]
        for _ in xrange(delay):
            [patient.update() for patient in patients]
        [patient.addPrescription('grimpex') for patient in patients]
        for _ in xrange(150):
            [patient.update() for patient in patients]
        return patients
        
    def plotVirusPop(virusPop, delay):
        pylab.hist(virusPop, bins = 10)
        pylab.title('Delay = %d' % delay)
#        pylab.xlabel('Total Virus Population')
        
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    
    pylab.figure()
    delays = [300, 150, 75, 0]
    for i in xrange(len(delays)):
        patients = generatePatients(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                     mutProb, numTrials)
        patients = simulateStepsWithDelay(patients, delays[i])
        virusPop = [patient.getTotalPop() for patient in patients]
        pylab.subplot(2, 2, i + 1)
        plotVirusPop(virusPop, delays[i])
    pylab.show()
