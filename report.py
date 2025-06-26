# report.py

def salvar_relatorio(nome_arquivo, conteudo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)
    print(f"[+] Relatório salvo em: {nome_arquivo}")
