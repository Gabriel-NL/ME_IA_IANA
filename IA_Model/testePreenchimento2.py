from PIL import Image, ImageDraw

# Criar duas imagens
imagem1 = Image.new('RGB', (332, 3840), 'red')
imagem2 = Image.new('RGB', (2560, 3840), 'blue')

# Calcular as coordenadas para centralizar imagem1 em imagem2
x = (imagem2.width - imagem1.width) // 2
y = (imagem2.height - imagem1.height) // 2

# Colar imagem1 em imagem2 nas coordenadas centralizadas
imagem2.paste(imagem1, (x, y))

# Salvar ou mostrar a imagem resultante
imagem2.show()
