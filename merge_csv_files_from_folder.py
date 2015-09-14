__author__ = 'vivek maswadkar'

# This program is to process each CSV File in the directory and attach it to the master.csvfile placed in hardcoded directory
# this directory / file is represented as master_file

# the landingzone is the directory which will be checked for .csv files. And if found csv file.. it will be processed and deleted.

import os

landingzone = '/Users/mbp/Python/landingzone'
master_file = '/Users/mbp/Python/done/master.csv'


# this function verifies the number of columns in the master file and the file to be processed are same.
# returns True if the number of fields are same else returns False

def verifylength(masterfile,csvfiles):
    master = open(masterfile,'r')
    each = open(csvfiles,'r')

    x = len(master.readline().split(','))
    y = len(each.readline().split(','))
    master.close()
    each.close()
    if x == y:
        return True
    else:
        return False


# reads file line by line and then writes it to master file.
# Deletes the file ones it is processed

#in case the file cannot be processed returns False, else True

def processcsv(masterfile,csvfiles):

    if os.path.exists(masterfile):
        if verifylength(masterfile,csvfiles) == False :
            print('file %s is not exact length of masterfile. Please verify' %csvfiles)
            return False

    f =open(csvfiles,'r',encoding='utf8')
    d= open(masterfile,'a',encoding='utf8')
    f.readline()

    for row in f:
        d.write(row)
    # d.write('\n')
    f.close()
    d.close()

    print('file %s is processed' %csvfiles)
    os.remove(csvfiles)
    print('file %s removed'%csvfiles)
    return True

# change the path to landing zone
os.chdir(landingzone)

# get the list of all the files in the directory
all_files = os.listdir(landingzone)

# process file by file
for csvfiles in all_files:

    filename,extension = os.path.splitext(csvfiles)
    # proces the file only if it is CSV file else skip it.
    if extension == '.csv':
        processcsv(master_file,csvfiles)