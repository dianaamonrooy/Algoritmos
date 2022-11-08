# Laboratorio - Redes Neuronales
##  Descripción
Se analiza la implementación del código de Red Neuronal para Clasificación Binaria en Numpy, su complejidad en tiempo y el impacto en el cambio que tiene el cambio de distintas variables en el rendimiento del algoritmo. Además se realiza una comparación entre dos funciones de activación: Sigmoide y Tangencial Hiperbólica 
## Complejidad Big O
```

# Hyperparameters

n_hidden = 2 # --------------------------------------- O(1)

epochs = 10 # ---------------------------------------- O(1)

alpha = 0.01 # --------------------------------------- O(1)

  

ult_costo = None # ----------------------------------- O(1)

  

m,k = features.shape # ------------------------------- O(1)

  

# Inicialización de los pesos

  

entrada_escondida = np.random.normal(scale = 1/k**0.5, size = (k,n_hidden)) # -------- O(1)

escondida_salida = np.random.normal(scale = 1/k**0.5,size = n_hidden) # -------------- O(1)

  

# Entrenamiento

for e in range(epochs): # --------------------------------------- O(e)

# Variables para el gradiente

gradiente_entrada_escondida = np.zeros(entrada_escondida.shape) # ----------------- O(1)

gradiente_escondida_salida = np.zeros(escondida_salida.shape) # ------------------ O(1)

# Itera sobre el conjunto de entrenamiento

for x,y in zip(features.values,targets): # ----------------------- O(90%-d)

# Pasada hacia adelande (forward pass) or forward propagation

# Entrada --> capa 1

z = sigmoide(np.matmul(x, entrada_escondida)) # -------------- O(k^2.8)

# Capa 1 --> salida

y_ =sigmoide(np.matmul(escondida_salida,z)) # predicción # -------------------- O(n_hidden^2.8)

# Pasada hacia atrás (backward pass)

salida_error = (y - y_) * y_ *(1- y_) # --------------------------------------- O(1)

escondida_error = np.dot(salida_error, escondida_salida) * z * (1 -z) # ------- O(n_hidden) --> Complejidad np.dot() = O(n)

  

gradiente_entrada_escondida += escondida_error * x[:,None] # ------------------ O(1)

gradiente_escondida_salida += salida_error * z # ------------------------------ O(1)

# Actualiza los parámetros (pesos)

entrada_escondida += alpha * gradiente_entrada_escondida / m # -------------------- O(1)

escondida_salida += alpha * gradiente_escondida_salida / m # --------------------- O(1)

  

if e % (epochs / 10 ) == 0:

z = sigmoide(np.dot(features.values, entrada_escondida)) # -------------------- O(k)

y_ = sigmoide(np.dot(z, escondida_salida)) # ---------------------------------- O(n_hidden)

  

# Función de costo

costo = np.mean(( y_ - targets)**2 ) # ---------------------------------------- O(1)

  

if ult_costo and ult_costo < costo:

print("Costo de entrenamiento: ", costo,

" ADVERTENCIA - Costo subiendo") # ---------------------------------- O(1)

else:

print("Costo de entrenamiento: ", costo ) # -------------------------------- O(1)

ult_costo = costo # --------------------------------------- O(1)

# Precisión en los datos de prueba
z = sigmoide(np.dot(features_test, entrada_escondida)) # --------------------------- O(k)
y_ = sigmoide(np.dot(z, escondida_salida)) # --------------------------------------- O(n_hidden)
predicciones = y_ > 0.5 # --------------------------------------- O(1)
precision = np.mean(predicciones == targets_test) # -------------- O(1)
print("Precisión: {:.3f}".format(precision)) # ------------------- O(1)
 

```

  

Así, la complejidad estaría dada por:

```
Big O = 7*O(1) + O(e)[2*O(1) + O(90%-d)[O(k^2.8) + 2*O(n_hidden^2.8) + 3*O(1)] + 2*O(1) + O(k) + O(n_hidden) + 4*O(1)] + O(k) + O(n_hidden) + 4*O(1)
= O(e)*O(90%-d)[O(k^2.8) + *O(n_hidden^2.8)] + O(e)*(O(k) + O(n_hidden)) + O(k) + O(n_hidden)
```

Donde:

  
```
*e = Épocas
*90%-d = Datos de entrenamiento
*k = Número de dimensiones en los datos
*n_hidden = Número de unidades en la capa escondida
```
