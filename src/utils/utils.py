import os
import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))
import dill
import pickle4 as pickle


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise str(e)
    
    
def load_object():
    try:
        print("Entered the load_object")
        model_path = "artifacts/nexum_model.pkl"
        print(model_path)
        with open(model_path, "rb") as file_obj:
            print("hii")
            loaded_model = dill.load(file_obj)
            print("Model Loaded")
        return loaded_model
    except FileNotFoundError as e:
        print("Model file not found at path:", model_path)
        return None
    except Exception as e:
        print("Error loading model:", str(e))
        return None