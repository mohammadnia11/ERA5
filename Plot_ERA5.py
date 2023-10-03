#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 03:33:44 2023

@author: insar
"""

import xarray as xr  # Handles labeled multi-dimensional arrays
import matplotlib.pyplot as plt  # Plotting library
import os  # Interface with the underlying OS
import numpy as np  # Numerical Python library

# Function to find the index of the nearest value in an array to a given value
def find_nearest_idx(array, value):
    array = np.asarray(array)  # Convert the input array to numpy array
    idx = (np.abs(array - value)).argmin()  # Find the index of the minimum difference
    return idx

nc_dir = './nc_dir'  # Define the directory containing the NetCDF files

# Get user input for geographic coordinates
input_lon = float(input("Enter longitude: "))
input_lat = float(input("Enter latitude: "))

# Initialize lists to store dates and temperature data
dates = []
temperature_data = []

# Loop over all files in the defined directory
for nc_file in sorted(os.listdir(nc_dir)):
    # Only process .nc files
    if nc_file.endswith(".nc"):
        date = nc_file.split('.')[0]  # Extract date from filename
        print(f"Processing {date}...")  

        nc_file_path = os.path.join(nc_dir, nc_file)  # Full path to the .nc file
        
        try:
            # Open the NetCDF file
            with xr.open_dataset(nc_file_path) as ds:
                print(ds.variables)  # Display available variables in the dataset
                print(ds.coords)  # Display available coordinates in the dataset
        
                # Convert temperature from Kelvin to Celsius and create a new data variable
                ds['t_Celsius'] = ds['t'] - 273.15
        
                # Assign units and a long name to the new variable for clarity and reference
                ds['t_Celsius'].attrs['units'] = 'C'
                ds['t_Celsius'].attrs['long_name'] = 'Temperature in Celsius'
        
                # Find the nearest grid point for the input coordinates
                lon_idx = find_nearest_idx(ds['longitude'].values, input_lon)
                lat_idx = find_nearest_idx(ds['latitude'].values, input_lat)
                
                # Extract temperature data for the nearest grid point
                temp_data = ds['t_Celsius'].sel(
                    longitude=ds['longitude'].values[lon_idx],
                    latitude=ds['latitude'].values[lat_idx],
                    level=1000,  # Select the atmospheric level (replace with the desired value)
                    time=ds['time'].values[0],  # Select the first time point
                    method='nearest'
                ).values.item()
                
                # Store the extracted data
                dates.append(date)
                temperature_data.append(temp_data)

                # Visualize the temperature data and the selected point
                plt.figure(figsize=(10, 6))
                plt.pcolormesh(ds['longitude'], ds['latitude'], ds['t_Celsius'].isel(time=0, level=0), shading='auto')
                plt.scatter(input_lon, input_lat, c='red', label='Input Point')
                plt.xlabel('Longitude')
                plt.ylabel('Latitude')
                plt.title(f'Temperature Grid and Input Point for {date}')
                plt.legend()
                plt.colorbar(label='Temperature [°C]')
                plt.savefig(f'temperature_grid_{date}.png')
                plt.show()
                
        # Handle exceptions during file processing
        except Exception as e:
            print(f"Failed to process {date}: {str(e)}")

# Plot temperature trend if data is available
if dates and temperature_data:
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperature_data, marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel(f'Temperature at ({input_lat}, {input_lon})')
    plt.title('Temperature Trend at Input Point')
    plt.tight_layout()
    plt.savefig('temperature_plot.png')
    plt.show()

    # Save the extracted data to a text file
    with open('temperature_data.txt', 'w') as file:
        file.write('Date\tTemperature_at_Point\n')
        for date, temp in zip(dates, temperature_data):
            file.write(f'{date}\t{temp}\n')
else:
    print("No data to plot or save.")
