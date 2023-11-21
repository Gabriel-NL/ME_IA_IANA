from PIL import Image
import os
import progressbar

def redimensionar_imagem(input_path, output_path, limite_horizontal, limite_vertical):
    imagem = Image.open(input_path)

    largura_original, altura_original = imagem.size

    # Verifica se a imagem precisa ser aumentada
    while altura_original < limite_vertical or largura_original < limite_horizontal:
        if altura_original < limite_vertical:
            altura_original = int(altura_original * 1.1)
        if largura_original < limite_horizontal:
            largura_original = int(largura_original * 1.1)

        imagem = imagem.resize((largura_original, altura_original), Image.BICUBIC)

    # Verifica se a imagem precisa ser reduzida
    while largura_original > limite_horizontal or altura_original > limite_vertical:
        largura_original = int(largura_original * 0.9)
        altura_original = int(altura_original * 0.9)

        imagem = imagem.resize((largura_original, altura_original), Image.BICUBIC)

    # Adiciona bordas se necessário
    if altura_original == limite_vertical and largura_original < limite_horizontal:
        borda = (limite_horizontal - largura_original) // 2
        imagem = Image.new('RGB', (limite_horizontal, limite_vertical), 'black')
        imagem.paste(imagem, (borda, 0))

    elif largura_original == limite_horizontal and altura_original < limite_vertical:
        borda = (limite_vertical - altura_original) // 2
        imagem = Image.new('RGB', (limite_horizontal, limite_vertical), 'black')
        imagem.paste(imagem, (0, borda))

    imagem.save(output_path)

# Defina os caminhos de entrada e saída
caminho_entrada = "Dataset\ImNotDog"
caminho_saida = "Dataset\DogFalse"

# Defina os limites
limite_horizontal = 3840
limite_vertical = 2560

# Lista todas as imagens na pasta de entrada
imagens = [f for f in os.listdir(caminho_entrada) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Cria uma barra de progresso
barra_progresso = progressbar.ProgressBar(max_value=len(imagens))

# Itera sobre cada imagem e realiza o redimensionamento
for i, imagem_nome in enumerate(imagens):
    input_path = os.path.join(caminho_entrada, imagem_nome)
    output_path = os.path.join(caminho_saida, imagem_nome)
    redimensionar_imagem(input_path, output_path, limite_horizontal, limite_vertical)
    barra_progresso.update(i + 1)

barra_progresso.finish()
