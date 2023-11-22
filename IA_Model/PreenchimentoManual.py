from PIL import Image
import cv2
import os

Target_width=3840
Target_height=2560






def redimensionar_imagem(caminho):

        imagem = Image.open(caminho)

        # Obtém as dimensões atuais da imagem
        largura_atual, altura_atual = imagem.size

        if (altura_atual/Target_height)>(largura_atual/Target_width):
            print("Adicionando barras horizontais...")
            #nova_imagem=adicionar_bordas(imagem,Target_width,altura_atual )
            print(f"Resolução antes do preenchimento: {largura_atual}x{altura_atual}")
            return preenchimento_lateral(imagem,largura_atual,altura_atual)
            
        elif((altura_atual/Target_height)<(largura_atual/Target_width)):
            print("Adicionando barras acima e abaixo...")
            #nova_imagem=adicionar_bordas(imagem,largura_atual,Target_height )
            #imagem_nova= preenchimento(imagem,borda,largura_atual,Target_height)
            return 0
            
        else:
            print("Pode aumentar a imagem sem necessidade de preenchimento")
            return 0


def preenchimento_lateral(imagem,largura,altura):
    
    #Se eu maximizo a altura
    #236w x 332h
    #?w x 2560h
    imagem_com_bordas = Image.new('RGB', (Target_width, Target_height), 'black')

    nova_largura=(largura*Target_height)/altura

    imagem = imagem.resize((int(nova_largura), Target_height), Image.BICUBIC)
    x = (imagem_com_bordas.width - imagem.width) // 2
    y = 0

    imagem_com_bordas.paste(imagem,(int(x), int(y)) )
    return imagem_com_bordas



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    caminho_imagem="Bcopy.jpeg"

    if os.path.exists(caminho_imagem):
        try:
            nova_imagem=redimensionar_imagem(caminho_imagem)
        except Exception as error:
            print(f"Erro ao redimensionar a imagem: {error}")
        # Redimensiona a imagem
        print(f"Resolução depois do preenchimento: {nova_imagem.width}x{nova_imagem.height}")
        nova_imagem.show()
        
    else:
        print("Caminho da imagem inválido.")

if __name__ == "__main__":
    main()