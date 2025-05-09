import pickle

# Simulación de un modelo con parámetros modificados
model = {"intercept": 0.7, "slope": 2.5}

# Almacenamiento del modelo en un archivo
with open("modelo.pkl", "wb") as f:
    pickle.dump(model, f)

print("Nueva versión del modelo entrenada y guardada como modelo.pkl")
