# python

MERGE CSV FILES FROM FOLDER

- This python program loops through the directory
- checks for .CSV files
- for each file performs the tasks if
    - master file already exists, ,if not then merges the first csv file into masterfile.
    - if exists then checks if the number of columns are same for master file and incoming file
    - appends all the rows of new csv file except the first row (Assuming that first row is header) and we do not want to copy headers everytime.

    - If the file is sucessfully processed, deletes the file from the folder. So please make sure that you copy the files from other location than move
    - closes both files
- closes the program.


TIPS:
- Paths for landingZone folder is hardcoded
- Paths for master.csv file is hardcoded.
    - This was done for my comfort level. This can very easily be changed by sending the line argument parameters.
    - The code is ready but I do not want to push it, because it is then difficult to DEBUG and test.

for any suggestions and comments please write me
vivek@maswadkar.com
