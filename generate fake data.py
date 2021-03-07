# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:50:19 2020

@author: Admin
"""

#auto generate sql insert codes to generate data for testing
import random
import time
import pandas as pd
import numpy as np
import mysql.connector


#write sql statement to the text file
text_file = open("dummygeneration.sql", "w")

################################ALL THE FIELDS WHICH WILL BE RANDOMLY SELECTED################################
##############################################################################################################

researcher_names = ['Cindy Shaheen', 'Daniel Berard', 'Francis Stabile', 'Kim Metera',
                    'Radin Tahvildari', 'Sabrina Leslie', 'Albert Kamanzi', 'Wendy Ji',
                        'Zach Friedenberger', 'Zhi Zhang']

imaging_descriptions = ['12 mM Tris', '10 mM PBS', '1x TBE' , '5x TBE', '6x TE + 2x TBE', '12mM Tris, Trolox, PCA, PCD', 
                       '1X PBS + 5% 55 kDa PVP + 0.002% Tween 20, with or without PCA/PCD/trolox',
                       'DI water', 'Loading buffer', 'PBS - pH 7.5', '25mM NaOAc/ 1 x PBS']

imaging_notes = ['this one worked a charm', 'ooft better luck next time', 
                       'a bit too cold on my fingers', 'omg who replaced my sample with orange juice',
                       'why on earth did we think of that','good lord it fizzed uncontrollably', 
                       'I have never felt so much loathing for a sample imaging buffer as this one',
                       '21 times I dreamt this would work, and sure enough it did',
                       'this is the million dollar idea I promise you']

storage_buffers = ['TE', 'TBE', 'Tris', 'PBS', 'Water', 'RRB', 'Loading buffer', 'NaOAc',]

storage_locations = ['-20 C Fridge #1', '4 C Fridge #2 (pFLIP-FUSE box)', '-80 C Freezer top shelf', 
                    '4 C fridge', '-80 C Freezer bottom shelf'] 

concentrations = [10, 20, 30, 40, 50]

quoted_concs = [10,20,30,40,50,'received dry']

molecules = ['Cas9', 'sgRNA', 'crRNA', 'Ionis', 'Mirexus', 'Exicure', 'siRNA', 'LNPS']

types = ['Nanoparticle', 'DNA', 'RNA', 'Protein']

dyes = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'cy3', 'Atto 647N', 'Atto 488', 'Alexa647' ]

molar_masses = [1,2.2,3,4.5,6,7.89,8.9]

surface_treatments = ['link1','link2''link3','link4',
                    'None, DDS-Tween', 'PLL-PEG', 'None yet',
                    't-RNA + Tween']  

handling_protocols = ['link1', 'link2', 'link3', 'protect from light', 'very hot ouch']


storage_boxes = ['CRISPR - Keith', 'Dan Ionis -80c', 'Dan Alnylam -80 C', 'Albert -LNPS', 'Albert - RNA -80 C'
               'Cindy - pFLIP-FUSE']

general_notes = ['this sample bites', 'this sample is tame', 'love your socks', 'please just cease']

#fields for when received from external source

origins = ['Lab1', 'Lab2', 'Lab3', 'Lab4']

manufacturer_infos = ['hot', 'cold', 'this one might really do some damage', 'accidentally peed in it',
                      'make sure to greet this sample every time you use it',
                      'this sample once killed a man, take care']

receiving_protocol_links = ['linkA', 'linkB', 'linkC', 'linkD', 'linkE', 'linkF']

##########################################DATABASE CONNECTION############################################
#########################################################################################################
"""
database_name = "testLeslie"

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  passwd="leslie78",
  database=database_name
)

mycursor = mydb.cursor()
"""

#########################################FILL TABLE WITH INDIVIDUAL NAMES################################
#########################################################################################################
def autoGene_oneAttribute(table_name, data_source, column_name ):
    n = len(data_source)
    for i in range(n):
        insert_stm = f"INSERT IGNORE INTO {table_name} ({column_name}) VALUES('{data_source[i]}');\n"
        text_file.write(insert_stm)

#########################################DATES FUNCTION##################################################
#########################################################################################################
def random_dates(start, end):
    start_u = start.value//10**9
    end_u = end.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u), unit='s')


######################################BETTER DATES FUNCTION##############################################
#########################################################################################################
    
def random_datetimes(start, end):
    
#########################################WORKERS TABLE###################################################
#########################################################################################################
    
autoGene_oneAttribute('workers', researcher_names, 'Name')

start = pd.to_datetime('2019-05-29')
end = pd.to_datetime('2020-05-29')

##########################################OTHER TABLES###################################################
#########################################################################################################

# data items required outside of the repeating function
parent_ids = []
sample_ids = []
creation_dates = []
protocols_id_number = 1
nano = 0
DNA = 0
RNA = 0
Protein = 0
insert_stm_parent_child = "";

#######FUNCTION TO GIVE NULL OR A VALUE################
    
def nullfate (thingtoenter):
    x = random.randint(0,10)
    if x >= 6:
        toReturn = 'NULL'
    else:
        toReturn = f'\'{random.choice(thingtoenter)}\''
        
    return toReturn

#########MAKING THE STATEMENTS############
    
for i in range(200):
    
    #creating the elements which will be added to the table in one statement
    molecule = f'\'{random.choice(molecules)}\''
    typee = f'\'{random.choice(types)}\''
    dye = f'\'{random.choice(dyes)}\''
    molar_mass = nullfate(molar_masses)
    initial_volume = f'\'{random.randint(0,100)}\''
    sample_creation_datee = random_dates(start, end).strftime('%Y-%m-%d')
    sample_creation_date = f'\'{sample_creation_datee}\''
    conc = nullfate(concentrations)
    storage_buffer = f'\'{random.choice(storage_buffers)}\''
    storage_location = f'\'{random.choice(storage_locations)}\''
    storage_box = f'\'{random.choice(storage_locations)}\''
    status_ID = f'\'{random.randint(0,1)}\''
    general_note = f'\'{random.choice(general_notes)}\''
    fridge_retrieval = f'\'{random.randint(0,20)}\''
    
    #now the protocols information
    insert_stm_protocols = ''
    
    surface_treatment = nullfate(surface_treatments)
    handling_protocol = nullfate(handling_protocols)
    
    if surface_treatment == "NULL" and handling_protocol == "NULL":
        protocols_id = "NULL"
    else:
        protocols_id = protocols_id_number
        protocols_id_number = protocols_id_number + 1
        insert_stm_protocols = f"INSERT IGNORE INTO protocol_information VALUES({protocols_id}, \
        {surface_treatment},{handling_protocol});\n"
    
    
    #now we need to update the ID's, I will artificially generate unique sample IDs
    
    sample_id = 'weee'
    parent_id = 'NULL'
    receiving_info_id = 'NULL'
    
    if typee=='\'Nanoparticle\'':
        sample_id = 'N' + str(nano)
        nano=nano+1
    
    if typee=='\'DNA\'':
        sample_id = 'D' + str(DNA)
        DNA=DNA+1
        
    if typee=='\'RNA\'':
        sample_id = 'R' + str(RNA)
        RNA=RNA+1
        
    if typee=='\'Protein\'':
        sample_id = 'P' + str(Protein)
        Protein=Protein+1
        
    #now we need to add the sample to the list of all of them, to potentially create a parent
    #for practicality, I will only do this for the first thirty samples
    #The else statement is trying to go through those first thirty, see if it could be a parent,
    # and if so, add it as a parent ID. Otherwise it will be null
    
    #NOTE the data won't make too much sense since the molecule might be different between parent and sample
    if i < 30:
        #these will become the ones that have receiving information, so they will have receiving_info_id
        parent_ids.append(sample_id)
        sample_ids.append(sample_id)
        creation_dates.append(sample_creation_date)
        newdate='\'2017-09-01\''
        
        #while loop to generate a physically received date that is different and later/equal to the creation date
        while(newdate <= sample_creation_date):
            newdatee = random_dates(start, end).strftime('%Y-%m-%d')
            newdate = f'\'{newdatee}\''
        
        physically_received_date = newdate
        print (physically_received_date)
        origin = nullfate(origins)
        receiver_id = random.randint(1, len(researcher_names))
        manufacturer_info = nullfate(manufacturer_infos)
        receiving_protocol_link = nullfate(receiving_protocol_links)
        
        # the ID will be autogenerated in the actual thing, but for us we need to autogenerate it
        receiving_info_id = i
        insert_stm = f"INSERT IGNORE INTO receiving_info VALUES ({receiving_info_id}, {physically_received_date},\
        {origin}, {receiver_id}, {manufacturer_info}, {receiving_protocol_link});\n"
        text_file.write(insert_stm)
    else:
        #We still need to add the sample ID to our list 
        sample_ids.append(sample_id)
        #we want to go through the parents and their creation dates and find one that always makes sense
        for (parent,date) in zip(parent_ids,creation_dates):
            if parent[0] == sample_id[0]  and date < sample_creation_date:
                parent_id = f'\'{parent}\''
                #insert_stm_parent_child = f"INSERT IGNORE INTO parent_child_info VALUES({parent_id}, '{sample_id}');\n"
                text_file.write(insert_stm_parent_child)
                break
    
    #adding to the imaging_buffer info table
    sample_id_2 = f'\'{random.choice(sample_ids)}\''
    note_date = "function"
    imaging_buffer = f'\'{random.choice(imaging_descriptions)}\''
    imaging_note = f'\'{random.choice(imaging_notes)}\''
    
    
    insert_stm_imaging = ''
    x = random.randint(0,10)
    if x > 7:
        insert_stm_imaging = f"INSERT IGNORE INTO lims_test.general_info VALUES ({sample_id_2},{imaging_description},\
        {imaging_note});\n"
    

    #adding to the main sample table
    
    insert_stm_sample = f"INSERT IGNORE INTO sample VALUES ('{sample_id}',{parent_id}, {molecule},\
    {typee}, {dye}, {molar_mass}, {initial_volume}, {sample_creation_date}, {conc},\
    {storage_buffer}, {storage_location}, {storage_box}, {status_ID}, {protocols_id}, \
    {receiving_info_id}, {general_note} , {fridge_retrieval});\n"
    
    
    text_file.write(insert_stm_sample)
    text_file.write(insert_stm_protocols)
    text_file.write(insert_stm_imaging)


text_file.close();