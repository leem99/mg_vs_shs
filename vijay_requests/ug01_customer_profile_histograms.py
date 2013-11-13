# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Charts for Edwin for SharedSolar Presentation in PNG ##
# November 11, 2013

# <markdowncell>

# #### Import Libraries ####

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import string

# <markdowncell>

# #### Open Data Analysis Tools ####

# <codecell>

execfile('C:\Users\Mitchell\Documents\Shared_Solar\mg_shs\python\sd_data_stats.py')

# <markdowncell>

# #### Open data and convert to hierarchical DataFrame ####

# <codecell>

# open data
ug = pd.read_csv('C:\Users\Mitchell\Documents\Shared_Solar\mg_shs\demand_data\ug_hourly.csv', parse_dates = True)

# create hierarchical DataFrame
ug = pd.pivot_table(ug, values = ['watt_hours_delta','max_credit','min_credit'], rows = 'time_stamp', cols = ['site_id','ip_addr'])

# convert index to timeseries
ug.index = ug.index.to_datetime()

# <markdowncell>

# #### Basic Filtering ####

# <codecell>

# Remove junk dates
ug = ug['2010':'2015']

# remove obvious outliers (Values greater than inverter limit
inv_lim = 750
ug[ ug >= inv_lim] = np.nan

# <markdowncell>

# #### Site Specific Filtering ####

# <codecell>

enter_name = 'ug01'
site = ug['watt_hours_delta'][enter_name][list(ug['watt_hours_delta'][enter_name].columns)]

# Remove mains from site data
if ('192_168_1_200' in list(site.columns))== 1:
    del site['192_168_1_200']

# Make sum of circuits pandas series
site_sum = site.sum(axis = 1)    

# Remove Hours where inverter limit is passed
site.ix[site.sum(axis=1) >= inv_lim] =  0
site_sum[site_sum >= inv_lim] = np.nan

# <markdowncell>

# #### UG01 Plot of Total Consumption ####

# <codecell>


# <codecell>

# Plot and add lables
site_sum.resample('D',how = 'sum')['2011-09-01':].plot()
plt.xlabel('Date',fontsize = '20')
plt.ylabel('Daily Energy Use (Wh)', fontsize = '20')
plt.title(str.upper(enter_name) + ': Daily Energy Consumption (' + str(int(np.shape(site.columns)[0])) + ' Customers)',fontsize = '20')
plt.show()

# <markdowncell>

# #### UG01: Per customer monthly energy expenditure ####

# <codecell>

# find daytime and nightime energy consumption
site_d, site_n = sort_daynight(site)

# aggregate by month
site_d = pd.DataFrame(site_d.sum(axis = 1).resample('m',how = 'sum'))
site_n = pd.DataFrame(site_n.sum(axis = 1).resample('m',how = 'sum'))

day_price = pd.DataFrame(index = site_d.index, columns = ['day_price'])
day_price[:'2012-07-01'] = 8
day_price['2012-07-01':'2013-04-01'] = 3
day_price['2013-04-01':] = 3


night_price = pd.DataFrame(index = site_d.index, columns =['night_price'])
night_price[:'2012-07-01'] = 10
night_price['2012-07-01':'2013-04-01'] = 8
night_price['2013-04-01':] = 5

# create revenue DF and convert to USD
revenue = (pd.DataFrame(site_d.values*day_price.values + site_n.values*night_price.values, index = site_d.index, columns = ['Revenue'] ,dtype = float)['2011-10':'2013-08'])/2520.00
x_tick_lab = [x.strftime('%Y-%m') for x in revenue.index]


fig = plt.figure()
revenue_plot = fig.add_subplot(1,1,1)
revenue_plot.set_xticks(range(0,np.shape(x_tick_lab)[0]))
revenue_plot.set_xticklabels(x_tick_lab,rotation = 90)
revenue_plot.bar(range(0,np.shape(revenue)[0]),revenue.values.ravel(),align = 'center')
plt.title(str.upper(enter_name) + ': Monthly Revenue Collection ('+ str(int(np.shape(site.columns)[0])) + ' Customers)',fontsize = '20')
plt.xlabel('Month',fontsize = '20')
plt.ylabel('Total Revenue Collected (USD)',fontsize = '20')
plt.show()
# <markdowncell>

# #### UG04 Plot of Total Consumption ####

# <codecell>

str(int(np.shape(site.columns)[0]))

# <codecell>

site.columns

# <codecell>


# <codecell>

