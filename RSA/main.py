from ucimlrepo import fetch_ucirepo
import math
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler


from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import Adam


from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc, confusion_matrix
import seaborn as sns
from sklearn.metrics import roc_auc_score
import datetime
import tensorflow as tf

TEST_SIZE = 0.3
HIDDEN_LAYERS = [
    40, 40, 50
]

#1 - Carregar dataset
# 1) Load dataset and remove rows with missing vars
#biblioteca que saiu do ar
#breast_cancer_wisconsin_original = fetch_ucirepo(id=15)
#X = breast_cancer_wisconsin_original.data.features
#y = breast_cancer_wisconsin_original.data.targets

#sem biblioteca
def read_data_from_file(file_path):
    X = []
    y = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into components
            components = line.strip().split(',')
            #print('componets{}'.format(components))

            # Extract the relevant parts
            data = components[1:-1]  # Assuming <dados> is between the first and last elements
            classification = components[-1]

            # Check for '?' in data
            if '?' not in data:
                # Append to X and y
                X.append(list(map(float, data)))
                
                if classification == '4':
                    classification = 1#tem cancer
                else:
                    classification = 0#não tem cancer
                y.append(float(classification))

    return np.array(X), np.array(y)

# Replace 'your_file_path.txt' with the actual path to your text file
file_path = 'data/breast-cancer-wisconsin.data'
X, y = read_data_from_file(file_path)



#com skealearn
#data = load_breast_cancer()
#X = data.data
#y = data.target

#2 - Normaliza dataset
scaler = MinMaxScaler(feature_range=(-1, 1))
X = scaler.fit_transform(X)

# 3) Dividir os dados em conjunto treinamento e teste utilizando método holdout
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE)


# 4) Definir a arquitetura de rede neural artificial com Tensorflow
model = Sequential(
    [Dense(len(X), activation='relu')] + # Input
    [Dense(x, activation='relu') for x in HIDDEN_LAYERS] +
    [Dense(1, activation='sigmoid')] # Saida
)

# 5) Definir um otimizador
custom_optimizer = Adam(learning_rate=0.01)
model.compile(optimizer=custom_optimizer,
    loss='binary_crossentropy',
    metrics=['accuracy'])

# 6) Treinar o modelo
history = model.fit(X_train, y_train, epochs=50,
    batch_size=2000,
    validation_split=0.2)

# 7) Avaliar o modelo
results = model.evaluate(X_test, y_test, verbose=0)
y_pred = (model.predict(X_test) > 0.5).astype(int)
y_pred_proba = model.predict(X_test)

#print('test loss, test acc:', results)

#8
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model.fit(x=X_train, 
          y=y_train, 
          epochs=5, 
          validation_data=(X_test, y_test), 
          callbacks=[tensorboard_callback])

history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test), callbacks=[tensorboard_callback])




#graficos
# Acurácia e perda nos dados de treino e validação
train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
train_loss = history.history['loss']
val_loss = history.history['val_loss']

# Gráfico de Acurácia
plt.plot(train_accuracy, label='Train Accuracy')
plt.plot(val_accuracy, label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Gráfico de Perda
plt.plot(train_loss, label='Train Loss')
plt.plot(val_loss, label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Obter as previsões no conjunto de teste
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Curva ROC
fpr, tpr, _ = roc_curve(y_test, y_pred[:, 0])  # Substitua 1 pelo índice da classe desejada
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show()

# Matriz de Confusão
# Calcular a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred_classes)

# Configurar o estilo da matriz de confusão
sns.set(font_scale=1.2)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='g', cmap="Blues", cbar=False, 
            xticklabels=['Não Câncer', 'Câncer'], yticklabels=['Não Câncer', 'Câncer'])

plt.title('Matriz de Confusão')
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()
# Relatório de Classificação
print("Classification Report:\n", classification_report(y_test, y_pred_classes))
