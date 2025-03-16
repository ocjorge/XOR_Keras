# Importación de bibliotecas
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Datos de entrada y salida para XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([[0], [1], [1], [0]])  # Salidas esperadas

# Definición del modelo
model = Sequential()

# Capa oculta con 2 neuronas y función de activación sigmoide
model.add(Dense(2, input_dim=2, activation='sigmoid'))

# Capa de salida con 1 neurona y función de activación sigmoide
model.add(Dense(1, activation='sigmoid'))

# Compilación del modelo
# - Función de pérdida: Error cuadrático medio (MSE)
# - Optimizador: Descenso de gradiente estocástico (SGD)
# - Métrica: Precisión (accuracy)
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

# Entrenamiento del modelo
# - epochs: Número de iteraciones sobre el conjunto de datos
# - batch_size: Número de muestras por actualización de pesos
# - verbose: 0 para no mostrar progreso, 1 para mostrar progreso
model.fit(X, y, epochs=10000, batch_size=4, verbose=0)

# Evaluación del modelo
print("Predicciones:")
print(model.predict(X))

# Mostrar los pesos finales
print("\nPesos finales de la capa oculta:")
print(model.layers[0].get_weights()[0])  # Pesos de las conexiones de entrada a oculta
print("\nBiases finales de la capa oculta:")
print(model.layers[0].get_weights()[1])  # Biases de la capa oculta

print("\nPesos finales de la capa de salida:")
print(model.layers[1].get_weights()[0])  # Pesos de las conexiones de oculta a salida
print("\nBiases finales de la capa de salida:")
print(model.layers[1].get_weights()[1])  # Biases de la capa de salida