from PIL import Image
import os

lista_arquivos = os.listdir("imagens")

for arquivo in lista_arquivos:
    # abrir arquivo
    imagem = Image.open(f"imagens/{arquivo}")# quando a conversão for para jpg ou pdf é necessário usar -->.convert("RGB")

    # salvar o arquivo com outro formato
    imagem.save(f'TIFF/{arquivo.replace("png", "tiff")}')# quando necessário usar duas vezes a aspas necessário alternar entre dupla e simples. (não pode usar duas vezes aspas simples ou duas vezes aspas duplas)

