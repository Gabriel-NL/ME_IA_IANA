from PIL import Image
import os

def limpar_console():
    # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_bordas(imagem, largura_alvo):
    #Pega a largura e altura atual
    largura_atual, altura_atual = imagem.size
    #Calcula o total a ser adicionado
    borda_total = largura_alvo - largura_atual
    #Calcula o tamanho das novas bordas
    nova_borda_D=(borda_total/2)-0,5
    nova_borda_E=(borda_total/2)+0,5
    #imagem = imagem.crop((0, 0, largura_atual, altura_atual))
    imagem_com_bordas = Image.new('RGB', (largura_alvo, altura_atual), 'black')

    print(borda_total/2)
    imagem_com_bordas.paste(imagem, (nova_borda_E, 0, largura_alvo - nova_borda_D, altura_atual))
    print(f" Tamanho: {imagem_com_bordas.size}")
    return imagem_com_bordas

def redimensionar_imagem(image_path, max_width=3840, max_height=2560):
    try:
        # Abre a imagem
        imagem = Image.open(image_path)

        # Obtém as dimensões atuais da imagem
        largura_atual, altura_atual = imagem.size
        
        # Verifica se a imagem precisa ser redimensionada
        if largura_atual > max_width or altura_atual < max_height:
            # Redimensiona sem achatar mantendo a proporção
            nova_largura = max_width
            nova_altura = int(altura_atual * (max_width / largura_atual))
            imagem = imagem.resize((nova_largura, nova_altura))

        elif largura_atual < max_width and altura_atual < max_height:
            # Redimensiona aumentando sem esticar mantendo a proporção
            nova_largura = min(max_width, largura_atual * (max_height / altura_atual))
            nova_altura = min(max_height, altura_atual * (max_width / largura_atual))
            
            print(f"Altura atual: {nova_altura} Largura atual: {nova_largura} ")
            imagem = imagem.resize((int(nova_largura), int(nova_altura)))
        print(f"Altura atual: {nova_altura} Largura atual: {nova_largura} ")
        # Adiciona bordas se a altura for 2560 e a largura não for 3840
        if nova_altura == 2560 and nova_largura < 3840:
            print("Adicionando Bordas...")
            imagem = adicionar_bordas(imagem, 3840)

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
