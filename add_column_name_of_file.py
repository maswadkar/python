__author__ = 'Vivek Maswadkar'

import os
import sys
import shutil
# hardcoded value for landingzone
landingzone = '/Users/mbp/Python/WIKIPEDIA'
ftemp = 'temp.csv'
inputs =[]

# this function adds column in csv file.
# the value of column = name of the file.

#  This is useful when each file is generated per day and name of the file is the date.
# But when you want to merge the files you want to have additional column 'DateCreated'

def add_column_from_file_name(filename):
    f = open(filename,'r')
    temp = open(ftemp,'w')

    headerline= f.readline()
    temp.write(inputs[3]+','+headerline)
    fname,fext = os.path.splitext(filename)

    for row in f:
        temp.write(fname + ',' + row)
    f.close()
    temp.close()

    print('Processed the file %s' %filename)
    shutil.copy(ftemp,filename)
    os.remove(ftemp)


def get_list_of_files(dirpath,extension):
    l_files = []
    x = os.listdir(dirpath)
    for eachfile in x:
        try:
            fname,fext = os.path.splitext(eachfile)
            if fext == extension:
                l_files.append(eachfile)

        except Exception as e :
            print(e)
            input()
    return l_files



# add_column_from_file_name('jj.csv')
def main(argvinput):
    if len(argvinput) != 4:
        print('3 Arguments are required.')
        exit()

    for x in argvinput:
        inputs.append(x)
    file_list = get_list_of_files(inputs[1],inputs[2])
    for each_file in file_list :
        add_column_from_file_name(each_file)


# main function takes 3 arguments.
# 1 folder name i.e. Landing Zone
# 2 extensions of the file that you want to process e.g. .csv or .txt
# 3 the column header name you want to specify for the new column

if __name__ == '__main__':
    main(sys.argv)
