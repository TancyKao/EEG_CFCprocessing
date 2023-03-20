#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:45:18 2020

@author: nathancross

Wonambi Heuristic Approach to Locating Elementary Spindles (WHALES)

This script runs a consensus approach to detecting sleep spindles. While we hope
to improve detection, and remove biases that occur based on the use of any one 
swa detector, this is not a perfect solution.
The pipeline runs in three stages:
    1. Detect spindles with pre-determined published algorithms (see Documentation).
    2. Assign 'true' events based upon a pre-set agreement threshold, using a consensus 
       of the events detected independently from step 1. This creates a new event called
       'swa' in the annotations file.
    3. Exports the parameters of these 'swa' events.

Inputs:

    <in_dir>
    <out_dir>
    <rater>
    <times>
    <part>
    <visits>

Output:
    1. A new annotation file per subject, with individual marked spindles labelled by
       the method name (e.g. 'Moelle2011') as well as the consensus events labelled
       'swa'.
    2. A csv output per subject with the swa parameters for that recording.
    3. A group-level summary dataset of swa parameters per subject.

"""

import sys
from platform import system
if system()=='Windows':
    prefix = 'S:'
else:
    prefix = ''

# tag::path_function[]
mypath = prefix+'\\Sleep\\SleepSoftware\\Coupling_python\\CFC_080920\\py_code'
# end::path_function[]


import sys
sys.path.append(mypath)#<-- change this to path containing scripts

from Woolcock import whale_it, whale_farm, slow_it
import pandas as pd
#%% DEFINE GENERAL INPUTS 



#root_dir = prefix + '\\Sleep\\SleepSoftware\\Coupling_python\\CFC_080920\\'
# tag::root_function[]
root_dir = 'S:\\Sleep\\SleepSoftware\\Coupling_Python\\CFC_080920\\'
in_dir = root_dir + 'individual\\'
# end::root_function[]

rater = None # rater name, as it appears in Annotation files (enter 'None' if multiple raters)

# tag::ind_function[]
cohort = 'TrackingSheet_HdEEG.xlsx' # enter filename of cohort file
# end::ind_function[]

# tag::SWA_function[]

### General Parameters
## slow wave
evt_name = 'slowwave'
method = ['Staresina2015']  # Massimini2004; AASM/Massimini2004; Ngo2015;Staresina2015
# end::SWA_function[]

# tag::par_function[]

cycle_idx = None #[1,2,3,4,5] # cycle index(es), starting at 1 ([None] = ignore cycles)
s_freq = 500 # sampling frequency of recordings
stage = ['NREM3'] # stages: NREM1, NREM2, NREM3, REM, Wake
reject_artf=['Arousal'] # if NREM3, remove 'Artefact'

# end::par_function[]



#chan = ['E' + str(i) for i in range(111, 121)]#['E20','E21','E22']   #,'[C4 - A1]','[O1 - A2]', '[O2 - A1]']  # channels e.g. ['F3','C3', etc.]

# tag::chan_function[]

chan = [

    ['E10', 'E20', 'E30']

 ]

# end::chan_function[]



ref_chan = [] # enter [] if no re-referencing needed
grp_name = 'eeg'
#delim = 3 # Number of characters before number in subject ID (e.g. for SDEP01, delim = 4; PB01, delim = 2)
cat = (1, 1, 1, 0) # concatenate within and between stages, cycles separate
""" 0 means no concatenation, 1 means concatenation
    position 1: cycle concatenation
    position 2: stage concatenation
    position 3: discontinuous signal concatenation
    position 4: event type concatenation (does not apply here)
"""
## soa
frequency = (0.1, 4.0) # it's fixed in the main code (no need to change) frequency limits of events, in Hz
duration= None#(0.8, 2) # duration limits of events, in secs


'''
     Preliminary Step 1: Define subjects to process 
     
     Select from one of the following options:
'''
#    Option 1. All subjects in subject directory
#part = 'all' 
#visit = 'all' 
#    Option 2. Select specific subjects
part = list(set(pd.ExcelFile(root_dir + cohort).parse('Sheet1')['ID'].values)) #import subject list from tracking sheet
visit= []
system_list = list(pd.ExcelFile(root_dir + cohort).parse('Sheet1')['System'].values)

'''
     Preliminary Step 2: SET POLARITY OF RECORDINGS
     
     Select from one of the following options:
'''
## 
#1. Import from tracking_sheet
#polar = pd.ExcelFile(root_dir + cohort).parse('Sheet1')['polar'].values 
#2. Set as default
polar = 'normal'



'''
SLOW WAVES
'''
for chan in chan:
    slow_it(in_dir, method, chan, rater, cat, stage, ref_chan, grp_name, reject_artf,
                frequency, duration, polar, part, visit)

    whale_farm(in_dir,system_list, method, chan, grp_name, rater, stage, reject_artf, ref_chan, 
            evt_name, cycle_idx, frequency, part, param_keys=None, exclude_poor=False, 
            epoch_dur=30, n_fft_sec=4)



    
