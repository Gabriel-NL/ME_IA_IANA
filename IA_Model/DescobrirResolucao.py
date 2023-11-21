from PIL import Image
import os

# Defina o limite horizontal e vertical desejado
limite_horizontal = 3840
limite_vertical = 2560

def obter_resolucao(imagem):
    largura, altura = imagem.size
    return largura, altura

# Função para excluir imagens com resolução superior ao limite
def excluir_imagens_com_resolucao_superior(pasta, limite_horizontal, limite_vertical):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            caminho_completo = os.path.join(pasta, arquivo)
            try:
                with Image.open(caminho_completo) as imagem:
                    largura, altura = obter_resolucao(imagem)

                    if largura > limite_horizontal or altura > limite_vertical:
                        os.remove(caminho_completo)
                    
            except PermissionError as e:
                print(f"Não foi possível excluir {caminho_completo}: {e}")
            finally:
                if 'imagem' in locals():
                    imagem.close()

# Função para encontrar as maiores resoluções
def encontrar_maior_resolucao(pasta):
    maior_resolucao_vertical = 0
    maior_resolucao_horizontal = 0
    imagem_maior_vertical = None
    imagem_maior_horizontal = None

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            caminho_completo = os.path.join(pasta, arquivo)
            try:
                with Image.open(caminho_completo) as imagem:
                    largura, altura = obter_resolucao(imagem)

                    if altura > maior_resolucao_vertical:
                        maior_resolucao_vertical = altura
                        imagem_maior_vertical = (caminho_completo, largura, altura)

                    if largura > maior_resolucao_horizontal:
                        maior_resolucao_horizontal = largura
                        imagem_maior_horizontal = (caminho_completo, largura, altura)
                    
            except PermissionError as e:
                print(f"Não foi possível processar {caminho_completo}: {e}")
            finally:
                if 'imagem' in locals():
                    imagem.close()

    return imagem_maior_vertical, imagem_maior_horizontal

# Substitua 'caminho_da_sua_pasta' pelo caminho da pasta contendo suas imagens
#pasta_imagens = 'Dataset\Dog'     #Maior resolução é 2560x2560
pasta_imagens = 'Dataset\DogFalse' #Maior resolução é 3840x2160

# Excluir imagens com resolução superior ao limite horizontal e vertical
excluir_imagens_com_resolucao_superior(pasta_imagens, limite_horizontal, limite_vertical)

# Encontrar maiores resoluções após a exclusão
imagem_maior_vertical, imagem_maior_horizontal = encontrar_maior_resolucao(pasta_imagens)

print(f'A imagem com maior resolução vertical é: {imagem_maior_vertical[0]} com resolução {imagem_maior_vertical[1]}x{imagem_maior_vertical[2]} pixels')
print(f'A imagem com maior resolução horizontal é: {imagem_maior_horizontal[0]} com resolução {imagem_maior_horizontal[1]}x{imagem_maior_horizontal[2]} pixels')
