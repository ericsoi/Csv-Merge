INSTRUCTIONS:
1. The script runs on  python2.7+	.
2. Ensure to install pandas python module for the script to work.
3. All the csv files to be combined have to be READABLE.
4. The script by default checks for source files with a .csv extension.
5. Step 4 above can be modified to any excel extension.

PREREQUISITES
	Ubuntu
	For Python3
		1. Install python3-pip
			$ sudo apt-get install python3-pip
		2. Install pandas
			$ pip3 install pandas
	For Python2
		1. Install python-pip
			$ sudo apt-get install python-pip
		2. Install pandas
			$ pip install pandas
	Windows
	For Python2
		Install pandas
			$ pip install pandas
	For Python3
		Install pandas
			$ pip3 install pandas


TESTING
1. How to use Example:
	command:	
		$ ./csv_merge.py -h
	output:	
		usage: csv_merge.py [-h] input output

		Script to marge unique columns from multiple csv files

		positional arguments:
		  input       SOURCE_FOLDER_PATH
		  output      DESTINATION_FOLDER_PATH

		optional arguments:
		  -h, --help  show this help message and exit

2. Running the script without parameters:
	command:
		$ ./csv_merge.py
	output:
		 usage: csv_merge.py [-h] input output
		 csv_merge.py: error: the following arguments are required: input, output


3. For non existing SOURCE_PATH and/or DESTINATION_PATH. The below error is thrown
	command:	
		$ ./csv_merge.py /input output/
	output:	
		Either Path input/ and/or output/ is not existing!

4. For non existing csv files in the source directory, the below error is thrown.
	command:	
		$ ./csv_merge.py input/empty/ output/
	output:	
		No csv files in input/empty/
5. For non-readable csv files, the below error is thrown.
	command:	
		$ ./csv_merge.py input/non_read/ output/
	Output:
		The following files are not accessible
		input/non_read/SOURCE_1.csv
		input/non_read/SOURCE_3.csv


6. For a functional operation, the output is stored in the destination folder specified as:
	command:
		$ ./csv_merge.py input/ output/
		
	Output:
		$ Output file: output/Expected_results.csv
