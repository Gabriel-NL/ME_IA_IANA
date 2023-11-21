from PIL import Image
import os

def limpar_console():
    # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

def redimensionar_imagem(image_path, max_width=3840, max_height=2560):
    try:
        # Abre a imagem
        imagem = Image.open(image_path)

        # Obtém as dimensões atuais da imagem
        largura_atual, altura_atual = imagem.size

        # Verifica se a imagem precisa ser redimensionada
        if largura_atual > max_width and altura_atual < max_height:
            # Redimensiona sem achatar mantendo a proporção
            nova_largura = max_width
            nova_altura = int(altura_atual * (max_width / largura_atual))
            imagem = imagem.resize((nova_largura, nova_altura))

        elif largura_atual < max_width and altura_atual < max_height:
            # Redimensiona aumentando sem esticar mantendo a proporção
            nova_largura = min(max_width, largura_atual * (max_height / altura_atual))
            nova_altura = min(max_height, altura_atual * (max_width / largura_atual))
            imagem = imagem.resize((int(nova_largura), int(nova_altura)))

        # Exibe a resolução atual da imagem
        print(f"Resolução atual da imagem: {imagem.size}")

        # Salva a imagem redimensionada
        imagem.save("imagem_redimensionada.jpg")
        print("Imagem redimensionada com sucesso!")

    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")

def main():
    limpar_console()
    image_path = input("Digite o caminho da imagem: ")
    
    # Verifica se a imagem existe
    if os.path.exists(image_path):
        # Redimensiona a imagem
        redimensionar_imagem(image_path)
    else:
        print("Caminho da imagem inválido.")

if __name__ == "__main__":
    main()
