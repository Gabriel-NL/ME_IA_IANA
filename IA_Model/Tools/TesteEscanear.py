import os
from PIL import Image
import numpy as np
import joblib
from tqdm import tqdm

os.system('cls' if os.name == 'nt' else 'clear')

# Carregar o modelo salvo
print("Carregando modelo...")
knn_model = joblib.load('modelo_knn.joblib')

# Pasta contendo as imagens a serem avaliadas
pasta_imagens_destino = "Dataset\DogFalse"

# Lista para armazenar os resultados
resultados = []

# Obter a quantidade total de arquivos na pasta
total_arquivos = len(os.listdir(pasta_imagens_destino))

# Inicializar a barra de progresso
with tqdm(total=total_arquivos, desc="Processando imagens") as pbar:
    # Percorrer todas as imagens na pasta de destino
    for arquivo in os.listdir(pasta_imagens_destino):
        caminho_arquivo = os.path.join(pasta_imagens_destino, arquivo)

        # Abrir a imagem e converter para escala de cinza
        imagem = Image.open(caminho_arquivo).convert("L")

        # Obter os dados da imagem
        dados_imagem = list(imagem.getdata())

        # Converter os dados da imagem em um array numpy
        imagem_array = np.array(dados_imagem).reshape(1, -1)

        # Fazer a previsão usando o modelo
        predicao = knn_model.predict(imagem_array)

        # Obter as probabilidades associadas a todas as classes
        probabilidades = knn_model.predict_proba(imagem_array)

        # Armazenar os resultados
        resultados.append({"arquivo": arquivo, "predicao": predicao[0], "probabilidades": probabilidades[0]})

        # Atualizar a barra de progresso
        pbar.update(1)

"""
# Exibir os resultados
for resultado in resultados:
    print(f"Arquivo: {resultado['arquivo']}, Predição: {resultado['predicao']}")
    print("Probabilidades:")
    for classe, probabilidade in zip(knn_model.classes_, resultado['probabilidades']):
        print(f"{classe}: {probabilidade:.4f}")
    print("\n")
"""

for resultado in resultados:
    print(f"Arquivo: {resultado['arquivo']}, Probabilidade de ser um cachorro: {resultado['probabilidade_cachorro']:.2%}")
