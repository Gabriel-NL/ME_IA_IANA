import os

os.system('cls' if os.name == 'nt' else 'clear')

max_width=3840
max_height=2560

#A imagem ideal tem proporçao 240w e 160h

image_width=200 #236
image_height=160 #332

#Se eu maximizo a largura
#236w x 332h
#3840w x ?h
expectedHeight=(image_height*max_width)/image_width

#Se eu maximizo a altura
#236w x 332h
#?w x 2560h
expectedWidth=(image_width*max_height)/image_height

if (image_height/max_height)>(image_width/max_width):
    print("Barras nas laterais sao melhores")
    print(f"Pois, se maximizar a largura, a altura vira {expectedHeight}pixels , que excede o espaço de {max_height} pixels")
    print(f"Logo, melhor maximizar a altura, gerando uma largura de:{expectedWidth}, que deixa {max_width-expectedWidth} pixels de espaço para barras")
elif((image_height/max_height)<(image_width/max_width)):
    print("Barras Acima e abaixo sao melhores")
    print(f"Pois, se maximizar a altura, a largura vira {expectedWidth}, que excede o espaço de {max_width}")
    print(f"Logo, melhor maximizar a largura, gerando uma altura de: {expectedHeight}, que deixa {max_height-expectedHeight} pixels de espaço para barras")
else:
    print("Pode aumentar a imagem sem necessidade de preenchimento")