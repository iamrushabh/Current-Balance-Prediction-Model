import os
import pyodbc
import sys
# # import uuid
from pathlib import Path 
# sys.path.append(str(Path(__file__).parent.parent))
import pandas as pd
# import uuid
import numpy as np
from sqlalchemy import create_engine
# from sqlalchemy import event
def getData(id): 
    try:
        # print("hii")
        server = "nexumuat.database.windows.net"
        database = 'nexum_base_demo_3_6_etl'
        username = 'nexum'
        password = r'ff=E(;A85u7oJK+4'
        
        # Connection string
        connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={{{password}}};'
        )
        # Establishing a connection to the SQL Server
        conn = pyodbc.connect(connection_string)
    
        # Instantiate a cursor
        cursor = conn.cursor()
    
        # Execute a SELECT query on the ALLOC_ETL table
        cursor.execute('SELECT * FROM UTILITYCOLLECTION_ETL where NEXUM_TENNANT = ?',id)
    
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        df = pd.DataFrame([tuple(row) for row in rows], columns=[col[0] for col in cursor.description])
        # Display the retrieved data
        # for row in rows:
        #     print(row)
        
        return df
    
    except pyodbc.Error as ex:
        print(f"Error: {ex}")
    finally:
        # Close the cursor in a finally block if it is still open
        if cursor:
            cursor.close()


def DeleteData(id): 
    try:
        # print("hii")
        server = "nexumuat.database.windows.net"
        database = 'nexum_base_demo_3_6_etl'
        username = 'nexum'
        password = r'ff=E(;A85u7oJK+4'
        
        # Connection string
        connection_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={{{password}}};'
        )
        # Establishing a connection to the SQL Server
        conn = pyodbc.connect(connection_string)
    
        # Instantiate a cursor
        cursor = conn.cursor()
    
        # Execute a SELECT query on the ALLOC_ETL table
        cursor.execute('DELETE FROM Nexum_Utility_Prediction WHERE Nexum_Tennant = ?',id)

        cursor.commit()
        conn.commit()
        # Fetch all rows from the result set
        # df = pd.DataFrame([tuple(row) for row in rows], columns=[col[0] for col in cursor.description])
        # Display the retrieved data
        # for row in rows:
        #     print(row)
        
        return "Record Deleted"
    
    except pyodbc.Error as ex:
        print(f"Error: {ex}")
    finally:
        # Close the cursor in a finally block if it is still open
        if cursor:
            cursor.close()



def writeToDatabase(df):
    try:
        print("hii")
        server = "nexumuat.database.windows.net"
        database = "nexum_base_demo_3_6_etl"
        username = "nexum"
        password = "ff=E(;A85u7oJK+4"
        driver = "ODBC+Driver+17+for+SQL+Server"
        print(df.head())
        # Create the engine
        engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
        df.to_sql(name="Nexum_Utility_Prediction" ,con=engine, index=False, if_exists='append')
        return "Processed successfully"

    except pyodbc.Error as e:
        print(e)
