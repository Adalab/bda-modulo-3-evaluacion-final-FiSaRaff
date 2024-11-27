import pandas as pd
import numpy as np
from datetime import datetime
from IPython.display import display

def exploring_dataframe(dataframe):

    print(f"Duplicates in dataset: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    print("Nulls in dataset:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["Null_%"])
    display(df_nulos[df_nulos["Null_%"] > 0])
    print("\n ..................... \n")
    print(f"Column types:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["Data_type"]))
    print("\n ..................... \n")
    print("Values of object columns: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    for col in dataframe_categoricas.columns:
        print(f"Column {col.upper()} has the following unique values:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())

def change_floats_to_int(dataframe, columns):
    for column in columns:
        if column in dataframe.columns and dataframe[column].dtype == 'float64':
            dataframe[column] = dataframe[column].apply(lambda x: int(x) if pd.notnull(x) else np.nan)
    return dataframe

