#!/usr/bin/python3
#############################################
#  Script to merge multiple csv files       #
#  Author: DDD Team                         #
#  version 1.1                              #
#############################################

# Arguments for the source and destination folders
# To be specified by the user

import pandas as pd, argparse, glob, os.path, sys
parser = argparse.ArgumentParser(description='Script to marge unique collumns from multiple csv files')
parser.add_argument("input", help='SOURCE_FOLDER_PATH')
parser.add_argument("output", help='DESTINATION_FOLDER_PATH')
args = parser.parse_args()

## Validate the Source & Destination folders exist
## Validate to ensure the files exists and are readable
error_files = []
if os.path.isdir(args.input) and os.path.isdir(args.output):
	files = glob.glob(args.input + "/*.csv")
	if not files:
		sys.exit("No csv files in {}".format(args.input))
	else:
		for file in files:
			try:
				open(file)
			except IOError:
				error_files.append(file)
			except:
				print("Unexpected error:", sys.exc_info()[0])
else:
	sys.exit("Either Path {} and/or {} is not existing".format(args.input, args.output))

## Prints out all the unreadable files and exits.
if error_files:
	print("The following files are not accessible")
	for file in error_files:
		print(file)
	sys.exit()

## Read the raw csv files
## Write the output and the trimmed output into path specified
else:
	csv_list = [pd.read_csv(file, keep_default_na=False, na_values=[""]) for file in files]
	combined_csv = pd.concat(csv_list, axis = 1)
	combined_csv.to_csv(args.output + '/Combined.csv')
	file_with_no_duplicates = combined_csv.T.drop_duplicates().T
	file_with_no_duplicates.to_csv(args.output + '/Expected_results.csv')
print("Output file: " + args.output + 'Expected_results.csv')