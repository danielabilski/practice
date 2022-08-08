import pandas as pd
import csv
from datetime import datetime
from utils import iso_date, percentage, convert_to_int

# read raw data
data = pd.read_csv("dataset.csv")

# change format date to iso format
for i, row in data.iterrows():

    data.loc[i, 'summary_date_iso'] = iso_date(row['summary_date'])

# group data by date and campaign
report = data.groupby(['summary_date_iso','campaign_name'], as_index=False)['impressions', 'clicks', 'installs', 'spend'].sum()

# calculate CTR and CPI
report['CPI'] = percentage(report['spend'],report['installs'])
report['CTR'] =  percentage(report['clicks'],report['impressions'])

report[['impressions', 'clicks', 'installs']] = convert_to_int(report[['impressions', 'clicks', 'installs']])

# report to csv
report.to_csv('report.csv')