from PIL import Image
import os

def limpar_console():
    # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_resolucao_pasta(caminho):
    # Lista de arquivos na pasta
    arquivos = os.listdir(caminho)

    # Verifica se há pelo menos uma imagem na pasta
    imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not imagens:
        print("Nenhuma imagem encontrada na pasta.")
        return

    # Inicializa valores de resolução máxima e mínima
    maior_resolucao_horizontal = menor_resolucao_horizontal = maior_resolucao_vertical = menor_resolucao_vertical = None

    # Verifica a resolução das imagens
    for imagem_nome in imagens:
        imagem_path = os.path.join(caminho, imagem_nome)
        imagem = Image.open(imagem_path)
        largura, altura = imagem.size

        # Atualiza valores de resolução máxima e mínima
        if maior_resolucao_horizontal is None or largura > maior_resolucao_horizontal:
            maior_resolucao_horizontal = largura

        if menor_resolucao_horizontal is None or largura < menor_resolucao_horizontal:
            menor_resolucao_horizontal = largura

        if maior_resolucao_vertical is None or altura > maior_resolucao_vertical:
            maior_resolucao_vertical = altura

        if menor_resolucao_vertical is None or altura < menor_resolucao_vertical:
            menor_resolucao_vertical = altura

    # Verifica se todas as imagens têm a mesma resolução
    if (
        maior_resolucao_horizontal == menor_resolucao_horizontal and
        maior_resolucao_vertical == menor_resolucao_vertical
    ):
        print("Todas as imagens têm a mesma resolução.")
    else:
        print("As imagens não têm a mesma resolução.")
        print(f"Maior resolução horizontal: {maior_resolucao_horizontal}")
        print(f"Menor resolução horizontal: {menor_resolucao_horizontal}")
        print(f"Maior resolução vertical: {maior_resolucao_vertical}")
        print(f"Menor resolução vertical: {menor_resolucao_vertical}")

if __name__ == "__main__":
    limpar_console()

    # Solicita o caminho da pasta
    #caminho_pasta = "Dataset\DogTrue"
    caminho_pasta = "Dataset\DogFalse"

    # Verifica a resolução das imagens na pasta
    verificar_resolucao_pasta(caminho_pasta)
