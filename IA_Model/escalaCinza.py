from PIL import Image

# Carregue a imagem
imagem = Image.open('NotDog (1).jpg')

# Converta a imagem para tons de cinza
imagem_em_tons_de_cinza = imagem.convert('L')

# Salve a nova imagem em tons de cinza
imagem_em_tons_de_cinza.save('Paiton.jpg')

# Para obter os dados da imagem em forma de matriz
dados_imagem = list(imagem_em_tons_de_cinza.getdata())

# Exiba a matriz de dados (opcional)
print(dados_imagem)
