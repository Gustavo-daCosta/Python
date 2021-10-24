# Organizar diferentes arquivos, dividir os arquivos em pastas filtrando cada um por sua extensão e tipo de arquivo

import os

# Criar pastas: imagens, audios, documentos, videos e outros
# Pegar o nome dos arquivos
# Pegar a extensão do arquivo para determinar o tipo
# Mover arquivos para pastas correspondentes

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf']

def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]

def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    OUTROS_DIR = os.path.join(diretorio, "outros")

    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = (pegar_extensao(arquivo)).lower()
            if extensao in audios_ext:
                nova_pasta = AUDIOS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
        
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print(f'Moveu: {velho} -> {novo}')

if __name__ == '__main__':
    organizar('dowloads')