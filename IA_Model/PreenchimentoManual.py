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
            return preenchimento_lateral(imagem,largura_atual,altura_atual)
            
        elif((altura_atual/Target_height)<(largura_atual/Target_width)):
            return preenchimento_sanduiche(imagem,largura_atual,altura_atual)
            
        else:
            return expansao((imagem,largura_atual,altura_atual))


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

def preenchimento_sanduiche(imagem,largura,altura):
    
    #Se eu maximizo a largura
    #236w x 332h
    #3840w x ?h
    imagem_com_bordas = Image.new('RGB', (Target_width, Target_height), 'black')
    nova_altura=(altura*Target_width)/largura
    imagem = imagem.resize((Target_height, int(largura) ), Image.BICUBIC)

    x=0
    y = (imagem_com_bordas.height - imagem.height) // 2

    imagem_com_bordas.paste(imagem,(int(x), int(y)) )
    return imagem_com_bordas

def expansao(imagem,largura,altura):
    imagem = imagem.resize((Target_height, Target_width ), Image.BICUBIC)
    return imagem


"""
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #caminho_imagem="Bcopy.jpeg" #De 236x332 a 3840x2560
    caminho_imagem="IsDog (1.2).webp" #De 984x657 a 3840x2560

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


"""