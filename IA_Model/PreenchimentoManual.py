from PIL import Image
import cv2
import os

Target_width=3840
Target_height=2560

def redimensionar_imagem(caminho):
    try:
        imagem = Image.open(caminho)

        # Obtém as dimensões atuais da imagem
        largura_atual, altura_atual = imagem.size

        if (altura_atual/Target_height)>(largura_atual/Target_width):
            print("Adicionando barras horizontais...")
            #nova_imagem=adicionar_bordas(imagem,Target_width,altura_atual )
            return preenchimento_lateral(imagem,Target_width,altura_atual)
            
        elif((altura_atual/Target_height)<(largura_atual/Target_width)):
            print("Adicionando barras acima e abaixo...")
            #nova_imagem=adicionar_bordas(imagem,largura_atual,Target_height )
            #imagem_nova= preenchimento(imagem,borda,largura_atual,Target_height)
            return 0
            
        else:
            print("Pode aumentar a imagem sem necessidade de preenchimento")
            return 0
        
    except Exception as error:
        print(f"Erro ao redimensionar a imagem: {error}")


def preenchimento_lateral(imagem,largura,altura):
    
    #Se eu maximizo a altura
    #236w x 332h
    #?w x 2560h
    Target_width=3840
    Target_height=2560
    nova_largura=round((largura*Target_height)/altura)

    borda_total= nova_largura-Target_width
    #Calcula o tamanho das novas bordas    
    imagem_com_bordas = Image.new('RGB', (Target_width, altura), 'black')

    if (borda_total%2)!=0:
        nova_largura = nova_largura-(borda_total%2)
        borda_total= nova_largura-Target_width
        imagem = imagem.crop((0, 0, largura, altura))
    else:
        imagem = imagem.crop((0, 0, largura, altura))
        
    print(f"Hi {Target_height} {Target_width} / {altura} {largura}")
    imagem_com_bordas.paste(imagem, (int(borda_total/2), 0, int((borda_total/2)-Target_width) , int(altura)))
    return imagem_com_bordas



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello World")
    caminho_imagem="Bcopy.jpeg"

    if os.path.exists(caminho_imagem):
        nova_imagem=redimensionar_imagem(caminho_imagem)
        # Redimensiona a imagem
        cv2.imshow('Imagem Redimensionada', nova_imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Caminho da imagem inválido.")

if __name__ == "__main__":
    main()