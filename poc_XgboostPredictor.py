import os
from google.cloud.aiplatform.prediction.xgboost.predictor import XgboostPredictor

# Asumimos que ya tienes un model.pkl válido en el mismo directorio
model_path = "model.pkl"
assert os.path.exists(model_path), f"No se encontró {model_path}"

# Crear carpeta temporal para simular artifacts_uri
artifacts_uri = "local_model"
os.makedirs(artifacts_uri, exist_ok=True)
os.replace(model_path, os.path.join(artifacts_uri, "model.pkl"))

# Instanciar y cargar
predictor = XgboostPredictor()
predictor.load(artifacts_uri)

# Predecir sobre input simple
input_data = {"instances": [[1, 2], [3, 4]]}
dmatrix = predictor.preprocess(input_data)
result = predictor.postprocess(predictor.predict(dmatrix))
print(result)
