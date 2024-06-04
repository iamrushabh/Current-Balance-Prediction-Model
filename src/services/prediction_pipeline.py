# import os
import sys
# # import uuid
from pathlib import Path  # Corrected import
import pandas as pd
sys.path.append(str(Path(__file__).parent.parent))
from src.db.conn import getData,writeToDatabase,DeleteData
from src.utils.utils import load_object
from decimal import Decimal

def predict(features):
    try:
        xgb_model = load_object()
        if xgb_model is None:
            print("Model not loaded, returning None")
            return None
        else:
            print("hii123")
            # data_scaled =preprocessor.fit_transform(features)
            print("hii")
            # print(data_scaled)
            prediction = xgb_model.predict(features)
            print("predict")
            return prediction
    except Exception as e:
        return str(e)
# Define the predictionPerform function
def predictionPerform(id):
    try:
        print("hii")
        df = getData(id)
        print(df.head(1))
        stat=DeleteData(id)
        print(stat)
        # Collected Data go for Preprocessing
        X = df[['Current Workflow', 'Current Workstep', 'DaysSinceLastInvoice', 'Workstep Desc', 'Last Inv Amount', 'Tot Inv', 'Tot Paid']]
        y = df['Curr Balance']
        # print(X.head())
        prediction=predict(X)
        # Append predictions to the DataFrame
        df['PredictedCurrentBalance'] = prediction
        print(df.head(5))
        print(df.info()) 
        print(prediction)
         # Replace NaT values with None
        # Select specific columns
        selected_columns = ["NEXUM_TENNANT", "Acc Number", "PredictedCurrentBalance"]
        df_selected = df[selected_columns]
        
        # Convert selected columns to dictionary
        df_dict = df_selected.to_dict(orient='records')

        
        # df.to_csv('data.csv', index=False)
        status=writeToDatabase(df)
        print(status)
        print("data save Sucessfully!!")

        return df_dict 
    except Exception as e:
        return str(e)