import sys
sys.path.append('.')

import pandas as pd
import numpy as np

from src import soporte as sp
from src import variables as va

print('Opening flight activity data set')
df_flights = pd.read_csv('../Data/Customer Flight Activity.csv')

print('Dropping duplicated rows before merging with second data set.')
df_flights = df_flights.drop_duplicates()

print('Opening customer loyalty history data set')
df_loyalty = pd.read_csv('../Data/Customer Loyalty History.csv')

print('Mergin both data sets')
merged_df = pd.merge(df_flights, df_loyalty, on='Loyalty Number', how='left')

print('Exploring merged data set')
exploring_dataframe(merged_df)

print('Changing Nulls in merged data set for Active')
merged_df[['Cancellation Year', 'Cancellation Month']] =  merged_df[['Cancellation Year', 'Cancellation Month']].fillna('Active')

print('Converting negative salary values to absolute values')
merged_df['Salary'] = merged_df['Salary'].abs()

print('Changing columns Points Accumulated and CLV from float to integer')
change_floats_to_int(merged_df, columns_to_convert)