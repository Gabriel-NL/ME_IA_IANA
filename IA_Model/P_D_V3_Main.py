# Save this file as main.py

from Passo1_Redimensionar import redimensionar_e_salvar_imagem
import joblib
import os
from Passo3_Avaliar import calcular_probabilidade_unica, display_results, process_images_in_folder
from P_D_V3_scrapper2 import mass_search_for_Links
from P_D_V3_Functions import download_image_from_pinterest
import os
from PIL import Image
import numpy as np


def main():
    knn_model = joblib.load("modelo_knn.joblib")
    tentativas = 4
    links = mass_search_for_Links(tentativas)

    for index, link in enumerate(links):
        imagem_nome = f"img"
        downloaded_path = download_image_from_pinterest(link, imagem_nome)
        print("Redimensionando...")
        redimensionar_e_salvar_imagem(downloaded_path,"p_saved")
        print("Avaliando...")
        resultado = calcular_probabilidade_unica(downloaded_path, knn_model)
        print("Imagem avaliada")
        porcentagem =max(100-resultado['predicao'], 0)
        print(f"A imagem citada possui {porcentagem}% de chance de ser um cachorro")
        
        if porcentagem <70:
            print("A imagem não é de um cachorro")
            print("Tentando novamente...")
            os.remove(downloaded_path)
        else:
            print("A imagem é de um cachorro")
            break


 
    
if __name__ == "__main__":
    main()
    
