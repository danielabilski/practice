from utils import read_csv, iso_date, calculate_cpi, calculate_ctr, convert_to_int
import numpy as np

# read raw data
data = read_csv("dataset.csv")

# change format date to iso format
for i, row in data.iterrows():

    data.loc[i, 'summary_date_iso'] = iso_date(row['summary_date'])

# group data by date and campaign
report = data.groupby(['summary_date_iso','campaign_name'], as_index=False)['impressions', 'clicks', 'installs', 'spend'].sum()

# calculate CTR and CPI
report['CPI'] = calculate_cpi(report['spend'],report['installs'])
report['CTR'] =  calculate_ctr(report['clicks'],report['impressions'])

report[['impressions', 'clicks', 'installs']] = convert_to_int(report[['impressions', 'clicks', 'installs']])

# new report to csv
report = report.round(2) # restrict float nums to 2 decimals
report.to_excel('report.xlsx', index=False)

