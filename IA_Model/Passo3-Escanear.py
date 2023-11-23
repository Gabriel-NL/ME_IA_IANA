import os
from PIL import Image
import numpy as np
import joblib

# Carregar o modelo salvo
knn_model = joblib.load('modelo_oficial.pkl')

# Pasta contendo as imagens a serem avaliadas
pasta_imagens = "Dataset\DogFalse"

# Lista para armazenar os resultados
resultados = []

# Percorrer todas as imagens na pasta
for arquivo in os.listdir(pasta_imagens):
    caminho_arquivo = os.path.join(pasta_imagens, arquivo)

    # Abrir a imagem e converter para escala de cinza
    imagem = Image.open(caminho_arquivo).convert("L")

    # Obter os dados da imagem
    dados_imagem = list(imagem.getdata())

    # Converter os dados da imagem em um array numpy
    imagem_array = np.array(dados_imagem).reshape(1, -1)

    # Fazer a previsão usando o modelo
    predicao = knn_model.predict(imagem_array)

    # Obter a probabilidade associada à classe "Cachorros" (ou rótulo relevante)
    probabilidade_cachorro = knn_model.predict_proba(imagem_array)[:, knn_model.classes_ == 'Cachorros']

    # Armazenar os resultados
    resultados.append({"arquivo": arquivo, "predicao": predicao[0], "probabilidade_cachorro": probabilidade_cachorro[0][0]})

# Exibir os resultados
for resultado in resultados:
    print(f"Arquivo: {resultado['arquivo']}, Predição: {resultado['predicao']}, Probabilidade de Cachorro: {resultado['probabilidade_cachorro']}")
