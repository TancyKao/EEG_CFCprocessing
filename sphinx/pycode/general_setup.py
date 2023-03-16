# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:30:57 2020

@author: Nathan Cross
General setup script.
This script takes input data (edf file, staging file, noise scores)
and translates them in the correct format for analysis in Wonambi.

Inputs:
    (See the accompanying user guide for more specific details)
<Study-specfic>_tracking_sheet.xlsx = Excel sheet with subject identifiers
<Subject-ID>.edf = file with EEG recording
<Subject-ID>_staging.txt = file with staging information
noise_scores.xls = file with artefact markings/noise scores (in 5s epochs)

Output: 
root_dir/subject/wonambi = new directory for outputs    
<Subject-ID>.xml = annotations file with scored staging, artefacts and arousals

""" 

"""IMPORTS THE REQUIRED DEPENDENCIES"""
"""                                 """

"""
 conda activate base
"""

from logging import root
import sys
from platform import system
if system()=='Windows':
    prefix = 'S:'
else:
    prefix = ''


# tag::path_function[]

mypath = prefix+'\\Sleep\\SleepSoftware\\Coupling_python\\CFC_080920\\py_code'
#print('\n' + mypath)

# tag::path_function[]

sys.path.append(mypath)#<-- change this to path containing scripts
from Woolcock import importit
import pandas as pd


"""             INPUTS             """ 
"""    - these you must edit -     """


# tag::root_function[]
root_dir = 'S:\\Sleep\\SleepSoftware\\Coupling_Python\\CFC_080920\\'
in_dir = root_dir + 'individual\\'

# tag::root_function[]


# tag::ind_function[]
cohort = 'TrackingSheet_HdEEG.xlsx'
# tag::ind_function[]


# tag::chan_function[]
chan = ['E10', 'E20', 'E30']
# tag::chan_function[]

#sys.exit()

rater = 'Anon' # rater name, as it will appear in Annotation files


""" THIS IMPORTS THE DATA """
subj_list = pd.ExcelFile(root_dir + cohort).parse('Sheet1')['ID'].values #import subject list
system_list = pd.ExcelFile(root_dir + cohort).parse('Sheet1')['System'].values


for i, val in enumerate(subj_list):
    subj = str(val)
    if str(subj) != 'nan':
        system = str(system_list[i])
        importit(in_dir, subj, chan, rater, system)

