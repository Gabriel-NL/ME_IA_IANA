from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib
from tqdm import tqdm

# Função para processar um lote de dados
def processar_lote(linhas, dados_imagens, labels):
    for linha in tqdm(linhas, desc='Processando lote', unit='linha'):
        # Extrair os dados da imagem da string
        dados_imagem_str = linha.split(":")[1].strip()

        # Converter a string de dados da imagem de volta para uma lista de inteiros
        valores = [int(valor.strip()) for valor in dados_imagem_str.strip('[]').split(',')]

        # Adicionar os dados à lista
        dados_imagens.append(valores)

        # Adicione um rótulo apropriado para cada linha (ajuste conforme necessário)
        # Substitua 'seu_rotulo' pelo rótulo real que você deseja atribuir a esses dados
        labels.append('Cachorros')

# Carregar os dados do arquivo de texto
with open('dados_imagens.txt', 'r') as file:
    # Ignorar a primeira linha (cabeçalho)
    file.readline()

    # Inicializar listas para armazenar dados e rótulos
    dados_imagens = []
    labels = []

    # Processar os dados em lotes
    batch_size = 50
    while True:
        linhas = file.readlines(batch_size)
        if not linhas:
            break  # Fim do arquivo

        processar_lote(linhas, dados_imagens, labels)

        # Convertendo listas em arrays numpy e liberando memória
        X = np.array(dados_imagens)
        y = np.array(labels)

        # Inicializando o modelo KNN
        knn_model = KNeighborsClassifier(n_neighbors=3)  # Ajuste o número de vizinhos (n_neighbors) conforme necessário

        # Treinando o modelo com os dados do arquivo
        with tqdm(total=100, desc='Treinando modelo', unit='%', position=0) as pbar:
            knn_model.fit(X, y)
            pbar.update(100)

        # Liberar memória
        dados_imagens = []
        labels = []

# Salvando o modelo treinado (fora do loop)
joblib.dump(knn_model, 'modelo_oficial.pkl')
