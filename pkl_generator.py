import pickle
from pathlib import Path

import numpy as np
import xgboost as xgb


class BenignPack:
    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b

    def to_pkl(self, booster: xgb.Booster) -> bytes:
        booster.set_attr(a=self.a, b=self.b)
        return pickle.dumps(booster, protocol=pickle.HIGHEST_PROTOCOL)


def build_dataset():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    return X, y

def train_booster(X, y) -> xgb.Booster:
    dtrain = xgb.DMatrix(X, label=y)
    params = {"objective": "binary:logistic", "eval_metric": "logloss"}
    return xgb.train(params, dtrain, num_boost_round=3)


def main() -> None:
    X, y = build_dataset()
    booster = train_booster(X, y)

    obj = BenignPack("value1", "value2")
    pkl_bytes = obj.to_pkl(booster)

    out = Path("artifacts/model.pkl")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(pkl_bytes)

    print(f"Wrote {out.as_posix()}")


if __name__ == "__main__":
    main()
