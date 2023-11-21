import cv2
import numpy as np

def redimensionar_e_preencher(image_path, nova_resolucao=(3840, 2560)):
    # Lê a imagem
    imagem = cv2.imread(image_path)

    # Obtém a resolução atual da imagem
    altura, largura = imagem.shape[:2]

    # Calcula as diferenças em altura e largura
    diferenca_altura = nova_resolucao[0] - altura
    diferenca_largura = nova_resolucao[1] - largura

    # Calcula a quantidade de pixels para adicionar em cada lado da imagem
    topo = diferenca_altura // 2
    inferior = diferenca_altura - topo
    esquerda = diferenca_largura // 2
    direita = diferenca_largura - esquerda

    # Adiciona bordas pretas à imagem
    imagem_redimensionada = cv2.copyMakeBorder(imagem, topo, inferior, esquerda, direita, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    # Redimensiona a imagem para a resolução desejada
    imagem_redimensionada = cv2.resize(imagem_redimensionada, nova_resolucao)

    return imagem_redimensionada

# Exemplo de uso
imagem_path = 'Dataset\ImDog\IsDog (1.1).jpg'
nova_imagem = redimensionar_e_preencher(imagem_path)

# Exibir a imagem original e a imagem redimensionada
cv2.imshow('Imagem Original', cv2.imread(imagem_path))
cv2.imshow('Imagem Redimensionada e Preenchida', nova_imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
