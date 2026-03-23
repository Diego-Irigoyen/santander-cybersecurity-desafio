from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_criptografados = file.read()
    dados_descriptografados = f.decrypt(dados_criptografados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

# Encontrar arquivos para descriptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != 'ransoware.py' and nome != 'descriptografar.py' and not nome.endswith('chave.key') and nome != 'LEIA ISSO.txt':
                lista.append(caminho)
    return lista

# Execução principal
def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Todos os arquivos foram descriptografados.")

if __name__ == "__main__":
    main()