import progressbar
from PreenchimentoManual import redimensionar_imagem
from PIL import Image
import os

def redimensionar_e_salvar_imagem(caminho_imagem, pasta_destino):
    try:
        nova_imagem = redimensionar_imagem(caminho_imagem)
        nome_arquivo = os.path.basename(caminho_imagem)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        nova_imagem.save(caminho_destino)
        #print(f"Imagem {nome_arquivo} redimensionada e salva em {pasta_destino}")
    except Exception as error:
        print(f"Erro ao processar a imagem {caminho_imagem}: {error}")

def redimensionar_todas_as_imagens(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    imagens = [arquivo for arquivo in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, arquivo))]

    with progressbar.ProgressBar(max_value=len(imagens)) as bar:
        for i, arquivo in enumerate(imagens):
            caminho_imagem = os.path.join(pasta_origem, arquivo)
            if redimensionar_e_salvar_imagem(caminho_imagem, pasta_destino):
                bar.update(i + 1)
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    pasta_origem = "Dataset\ImNotDog"
    pasta_destino = "Dataset\DogFalse"

    if os.path.exists(pasta_origem):
        redimensionar_todas_as_imagens(pasta_origem, pasta_destino)
    else:
        print("Caminho da pasta de origem inválido.")

if __name__ == "__main__":
    main()
