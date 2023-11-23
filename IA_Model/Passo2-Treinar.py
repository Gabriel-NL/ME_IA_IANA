import os
import cv2
import random
import numpy as np
from joblib import dump, load
from sklearn.neighbors import KNeighborsClassifier
 # Módulo antigo, você pode usar `from joblib import dump, load` em versões mais recentes

os.system('cls' if os.name == 'nt' else 'clear')


def corrigir_nomes_de_arquivos(folder):

    id_counter = 1
    
    for filename in os.listdir(folder):
        # Formatar o ID como uma string com 6 dígitos
        new_name = f"isDog{id_counter:06d}"
            
        # Obtenha a extensão do arquivo
        _, file_extension = os.path.splitext(filename)
            
        # Crie o novo nome do arquivo com a extensão
        new_filename = new_name + file_extension
            
        img_path = os.path.join(folder, filename)
        new_img_path = os.path.join(folder, new_filename)
            
        # Renomear o arquivo se necessário
        if filename != new_filename:
            os.rename(img_path, new_img_path)
            
        # Incrementar o contador para o próximo ID
        id_counter += 1

def load_images_from_folder(folder):
    images = []
    labels = []
    
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(folder)
    
    for label, filename in enumerate(arquivos):  # Corrigido para usar enumerate para obter rótulos
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Corrigido para usar o caminho completo da imagem
        if img is not None:
            images.append(img.flatten())
            labels.append(label)
            
    return np.array(images), np.array(labels)


# Defina o caminho para o diretório contendo suas imagens de treinamento
data_dir = "Dataset\DogTrue"

print("Corrigindo os nomes...")
#corrigir_nomes_de_arquivos(data_dir)
print("Corrigidos!!!")

# Carregue imagens e rótulos
images, labels = load_images_from_folder(data_dir)

# Crie o classificador k-NN
knn = KNeighborsClassifier(n_neighbors=3)  # Você pode ajustar o número de vizinhos conforme necessário

# Treine o classificador Dataset\DogTrue\IsDog (1.1).jpg
knn.fit(images, labels)

num_amostras = knn._fit_X.shape[0]
print(f"Número total de amostras no conjunto de treinamento: {num_amostras}")

# Salve o modelo treinado em um arquivo
dump(knn, 'modelo_knn.joblib')
