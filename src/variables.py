columns_to_convert = ['Points Accumulated', 'CLV']

merged_df_grouped = merged_df.groupby(['Year', 'Month'])['Flights Booked'].sum().reset_index() 

