# PythonDevelopmentTest

###Task #1

Input data is contained in two disk files. Both files contain multiple entries separated by a
newline character. The first file is of the following form:

*<first name> <ID number>*
  
The other file contains entries of the following format:
  
*<last name> <ID number>*
  
Write a program that, based on the information contained in input files, creates an output file
with the format:
  
*<first name> <last name> <ID number>*
  
Example input:
  
Adam 1234
  
John 4321

Anderson 4321

Smith 1234

Expected output:

Adam Smith 1234

John Anderson 4321

Extension #1: sort output entries by the ID number

Extension #2: input data is too big to fit into main memory.
