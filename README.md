🚀 **Navigating Through Atmospheric Data with Precision: Your Guide to ERA5 Data Download and Insightful Plotting!**

Embark on a data-driven journey through the atmospheric realms with our codes, precisely designed for the ERA5 climate dataset – a global climate dataset hosted by the ECMWF (European Centre for Medium-Range Weather Forecasts). 🌎💨

🔍 **Explore Code 1: Dive Deep into the ERA5 Data Retrieval**

Our first code provides a simplified method for downloading ERA5 reanalysis data. 📥🌦️

**Steps:**

1 - **Get API Key:**

Visit this website to create an account and obtain your API key.
Create a text file in your Home directory named .cdsapirc and save the following inside it:

        url: https://cds.climate.copernicus.eu/api/v2
        key: [your API key]

2 - __Install cdsapi:__

        conda install -c conda-forge cdsapi
Or

        pip install cdsapi
        
        
3 - __Modify and Run the Code:__

* Open Download_ERA5.py and adjust the variables, pressure levels, date, and area specifications (lat, lon, lat, lon) = (upper left, lower right) to your requirements.
  
* Create a file with a list of "Epoch" names in one column, including the dates you wish to download (e.g., 20180611), and place it next to Download_ERA5.py.

* Run the Python code in the terminal as follows:
python Download_ERA5.py


📈 __Unlock Code 2: Plotting a Variable__

Explore deeper into the atmospheric layers with our second code, crafted to enable visualization of temperature variations at specific geographical points and pressure levels. 🌡️📍

__Installation Guide__

Prerequisites:

**Using conda:**

        conda install -c conda-forge xarray dask netCDF4 
        conda install -c conda-forge matplotlib
        conda install -c conda-forge numpy
        
**Using pip:**

        pip install xarray matplotlib numpy

Note: Upon opening Plot_ERA5.py, you can modify the pressure level and variable you wish to plot.

__Additionally__, you will obtain a text file output that you can utilize for your purposes, such as comparing it with other data.

🌐**Why ERA5?**

ERA5 provides a unique and extensive atmospheric dataset, offering a wealth of information such as wind patterns 🌬️, temperature profiles 🌡️, humidity levels 💦, and more, covering global data from 1979 to present. The depth and breadth of this dataset facilitate a plethora of research areas, including climate analysis, weather prediction, and environmental modeling, among others.





