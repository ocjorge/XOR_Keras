# Red Neuronal en Python: Resolución del Problema XOR con Keras

Este proyecto implementa una red neuronal utilizando la biblioteca **Keras** (parte de TensorFlow) para resolver el problema XOR. El código es simple, eficiente y demuestra cómo construir, entrenar y evaluar una red neuronal básica.

---

## **Contenido**
1. [Requisitos](#requisitos)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Cómo Ejecutar](#cómo-ejecutar)
4. [Explicación del Código](#explicación-del-código)
5. [Resultados Esperados](#resultados-esperados)
6. [Contribución](#contribución)
7. [Licencia](#licencia)

---

## **Requisitos**
- **Python 3.7 o superior**: Asegúrate de tener Python instalado.
- **Bibliotecas necesarias**:
  - TensorFlow (incluye Keras).
  - NumPy.

Puedes instalar las dependencias con el siguiente comando:
```bash
pip install tensorflow numpy
```

---

## **Estructura del Proyecto**
El proyecto consiste en un único archivo Python:
- **xor_keras.py**: Contiene la implementación completa de la red neuronal, incluyendo la definición del modelo, el entrenamiento y la evaluación.

---

## **Cómo Ejecutar**
1. Clona este repositorio o descarga el archivo `xor_keras.py`.
2. Abre una terminal o línea de comandos y navega hasta la carpeta donde se encuentra el archivo.
3. Ejecuta el archivo Python:
   ```bash
   python xor_keras.py
   ```

---

## **Explicación del Código**

### **Importación de Bibliotecas**
Se importan las bibliotecas necesarias:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
```

### **Datos de Entrada y Salida**
Se definen los datos de entrada (`X`) y las salidas esperadas (`y`) para el problema XOR:
```python
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
```

### **Definición del Modelo**
Se crea un modelo secuencial con una capa oculta y una capa de salida:
```python
model = Sequential()
model.add(Dense(2, input_dim=2, activation='sigmoid'))  # Capa oculta con 2 neuronas
model.add(Dense(1, activation='sigmoid'))  # Capa de salida con 1 neurona
```

### **Compilación del Modelo**
Se compila el modelo especificando la función de pérdida, el optimizador y las métricas:
```python
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
```

### **Entrenamiento del Modelo**
El modelo se entrena con los datos de entrada y salida:
```python
model.fit(X, y, epochs=10000, batch_size=4, verbose=0)
```

### **Evaluación del Modelo**
Se evalúa el modelo y se muestran las predicciones:
```python
print("Predicciones:", model.predict(X))
```

---

## **Resultados Esperados**
Al ejecutar el programa, deberías ver una salida similar a la siguiente:
```
Predicciones: [[0.01]
               [0.99]
               [0.98]
               [0.02]]
```
Esto indica que la red neuronal ha aprendido correctamente la función XOR.

---

## **Contribución**
Si deseas contribuir a este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama con tu contribución (`git checkout -b mi-contribucion`).
3. Realiza tus cambios y haz commit (`git commit -m "Añadí X funcionalidad"`).
4. Haz push a la rama (`git push origin mi-contribucion`).
5. Abre un Pull Request.

---

## **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## **Contacto**
Si tienes preguntas o sugerencias, no dudes en contactarme:
- **Nombre**: [Jorge Ortiz]
- **GitHub**: [jorgeoc](https://github.com/jorgeoc)

---

¡Gracias por visitar este proyecto! 😊

---

### **Notas Adicionales**
- Este código es ideal para principiantes que quieren aprender a usar Keras para problemas simples.
- Si deseas extender el proyecto, puedes agregar más capas, cambiar las funciones de activación o probar diferentes optimizadores.

