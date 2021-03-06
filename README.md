mg_vs_shs
=========

This repo contains materials for an academic paper Mitchell Lee is working on. 
The goal of the paper is to use SharedSolar data in order to compare the cost 
of micro-grids to Solar Home Systems. 

Micro-grid simulations are conducted in HOMER.

Underlying data comes from sharedsolar@data.sharedsolar.org

To learn more about the data synthesis process go to:
https://github.com/modilabs/shared_solar_data_warehouse

Steps taken to convert data on sharedsolar@data.sharedsolar.org
into HOMER readable files are in /mg_vs_shs/python

#### Python ####

clean_homer_output.ipynb
> Script loops through files generated by HOMER and writes them to homer objects.
> Currently the script only handles the sensitivity analysis. All sensitivity analysis results are
> put into a single DataFrame that is multi-indexed on site, circuit, and the maximum 
> capacity storage of the input model.


make_homer_customer_demand.ipynb
> Takes the ouput view of SharedSolar database contained on sharedsolar@data.sharedsolar.org
> and breaks into down into individual text files for each circuit. These text files can be 
> seamlessly imported into HOMER. However, script requires modification to be used for data any
> specifc SharedSolar site. This is because different ranges of dates, or different gap filling
> techniques may want to be used for different customers. This script has been tailored to specifically 
> handle UG01 and UG04 data.


ss_data_stats.py
> A series of functions that can be used toolkit for analyzing SharedSolar timeseries. Has tools for 
> plotting and aggregating data.

#### demand_data ####

> __UG01__

> * ug01_1.txt, ... ,ug01_10.txt are the individual circuit level HOMER readable files
> * ug01_sum.txt is the sum of circuits (without ug01_0) in HOMER readable format 

> __UG04__

> * ug04_1.txt, ug04_3.txt, ... ,ug04_9.txt are the individual circuit level HOMER readable files. 
ug04_2 and ug04_10 are ignored because they contain little to no data.
> * ug04_sum.txt is the sum of circuits (without ug01_0) in HOMER readable format 


> __Data across all sites__
> * drop_00_08_2013DF.csv contains data retrieved from SD cards returned by Mitchell
Lee in September 2013. The data was put into hourly resolution using Alan Pan's method 
using sqlite3 databases. 
> * ug_hourly.csv contains all Uganda energy demand and credit data from data.sharedsolar.org, 
circuit_reading_hourly

