from PIL import Image

def adicionar_bordas(image_path, largura_borda_esquerda, largura_borda_direita):
    # Abre a imagem original
    imagem_original = Image.open(image_path)

    # Obtém as dimensões originais da imagem
    largura_original, altura_original = imagem_original.size

    # Calcula as novas dimensões com as bordas adicionadas
    nova_largura = largura_original + largura_borda_esquerda + largura_borda_direita
    nova_altura = altura_original

    # Cria uma nova imagem preta com as novas dimensões
    imagem_com_bordas = Image.new('RGB', (nova_largura, nova_altura), 'black')

    # Calcula a posição para colar a imagem original no centro
    posicao_colagem = ((largura_borda_esquerda, 0))

    # Cola a imagem original na nova imagem
    imagem_com_bordas.paste(imagem_original, posicao_colagem)

    # Salva a imagem resultante
    imagem_com_bordas.save("test.jpeg")

# Exemplo de uso
imagem_original = "Bcopy.jpeg"
largura_borda_esquerda = 50
largura_borda_direita = 50
adicionar_bordas(imagem_original, largura_borda_esquerda, largura_borda_direita)
