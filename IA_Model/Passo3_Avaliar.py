import os
from PIL import Image
import numpy as np
import joblib
from tqdm import tqdm

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_model(model_path):
    print("Carregando modelo...")
    return joblib.load(model_path)

def process_image(image_path, model):
    # Abrir a imagem e converter para escala de cinza
    imagem = Image.open(image_path).convert("L")

    # Obter os dados da imagem
    dados_imagem = list(imagem.getdata())

    # Converter os dados da imagem em um array numpy
    imagem_array = np.array(dados_imagem).reshape(1, -1)

    # Fazer a previsão usando o modelo
    predicao = model.predict(imagem_array)

    # Obter as probabilidades associadas a todas as classes
    probabilidades = model.predict_proba(imagem_array)

    return predicao[0], probabilidades[0]

def process_images_in_folder(folder_path, model):
    resultados = []

    # Obter a quantidade total de arquivos na pasta
    total_arquivos = len(os.listdir(folder_path))

    # Inicializar a barra de progresso
    with tqdm(total=total_arquivos, desc="Processando imagens") as pbar:
        # Percorrer todas as imagens na pasta de destino
        for arquivo in os.listdir(folder_path):
            caminho_arquivo = os.path.join(folder_path, arquivo)

            # Processar cada imagem
            predicao, probabilidades = process_image(caminho_arquivo, model)

            # Armazenar os resultados
            resultados.append({"arquivo": arquivo, "predicao": predicao, "probabilidades": probabilidades})

            # Atualizar a barra de progresso
            pbar.update(1)

    return resultados

def calcular_probabilidade_unica(arquivo_individual, knn_model):
    imagem = Image.open(arquivo_individual).convert("L")
    dados_imagem = list(imagem.getdata())
    imagem_array = np.array(dados_imagem).reshape(1, -1)

    predicao = knn_model.predict(imagem_array)
    probabilidades = knn_model.predict_proba(imagem_array)

    media_probabilidades = np.mean(probabilidades)    
    resultado = {'arquivo': arquivo_individual, 'predicao': predicao[0], 'probabilidades': probabilidades}
    return resultado


def display_results(resultados, model_classes):
    for resultado in resultados:
        print(f"Arquivo: {resultado['arquivo']}, Predição: {resultado['predicao']}")
        print("Probabilidades:")
        for classe, probabilidade in zip(model_classes, resultado['probabilidades']):
            print(f"{classe}: {probabilidade:.4f}")
        print("\n")

def display_results_formatted(resultados):
    for resultado in resultados:
        print(f"A imagem citada possui {max(100-resultado['predicao'], 0)}% de chance de ser um cachorro")
        #print(f"Arquivo: {resultado['arquivo']}, Probabilidade de ser um cachorro: {resultado['probabilidades'][0]:.2%}")

def main():
    clear_screen()

    # Carregar o modelo salvo
    knn_model = load_model('modelo_knn.joblib')

    # Pasta contendo as imagens a serem avaliadas
    pasta_imagens_destino = "Dataset\DogTrue"

    # Processar as imagens na pasta
    #resultados = process_images_in_folder(pasta_imagens_destino, knn_model)
    # Exibir os resultados formatados
    #display_results_formatted(resultados)

    arquivo_individual1= "Dataset\DogFalse\isNotDog (101).jpg"
    arquivo_individual2= "Dataset\DogTrue\isDog000002.jpg"



    resultado1 = calcular_probabilidade_unica(arquivo_individual2, knn_model)
    print(f"Arquivo: {resultado1['arquivo']}, Predição: {resultado1['predicao']}")
    print(f"A imagem citada possui {max(100-resultado1['predicao'], 0)}% de chance de ser um cachorro")
    print("\n")
    """

    resultado2 = calcular_probabilidade_unica(arquivo_individual2, knn_model)
    print(f"Arquivo: {resultado2['arquivo']}, Predição: {resultado2['predicao']}")
    print("Probabilidades:")
    for classe, probabilidade in zip(knn_model.classes_, resultado2['probabilidades'][0]):
            print(f"{classe}: {probabilidade:.4f} ",end="")
    print("\n")
 


    # Exibir os resultados detalhados
    display_results(resultados, knn_model.classes_)
    """



if __name__ == "__main__":
    main()
