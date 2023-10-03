#!/usr/bin/env python
# Written By Mohammadnia

# mh.mohammadnia1@gmail.com 
# Oct 2023
# Importing necessary modules

import cdsapi
import os

# Create an instance of the CDS API client
c = cdsapi.Client()

# Try to open a file and handle the potential error if the file is not found
try:
    f = open('Epoch', 'r')  # Open the file 'Epoch' in read mode
except FileNotFoundError:
    print("The file does not exist, check your file name")

# Define a function that counts and prints the number of lines (images) in the input file
def count(filename):
    with open(filename) as fn:
        x = fn.read()  # Read the content of the file
        c = len(x.splitlines())  # Count the number of lines
        print("Number of images will be downloaded: " + f'{filename} : {c}')

# Execute the count function for the 'Epoch' file
count('Epoch')

# Create directory named 'nc_dir' if it does not exist
if not os.path.exists('nc_dir'):
    os.makedirs('nc_dir')

# Open 'Epoch' and loop through each line in the file
with open('Epoch') as fi:
    for line in fi:
        # Extract the year, month, and day from the line
        y = int(line[0:4])  # Year
        m = int(line[4:6])  # Month
        d = int(line[6:8])  # Day

        # Use the CDS API client to retrieve ERA5 data for the extracted date
        c.retrieve(
            'reanalysis-era5-pressure-levels',  # Data product
            {
                'product_type': 'reanalysis',  # Type of product
                # ... [The rest of the data request options are unchanged]
            },
            os.path.join('nc_dir', str(y) + str(m).zfill(2) + str(d).zfill(2) + '.nc')
            # Name of the file to save data to, saved into 'nc_dir' folder
        )

# Print success message to the console
print('                                               ')
print(' ERA5 data request has been done successfully! ')
print('                                               ')
