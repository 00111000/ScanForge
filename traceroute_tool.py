import platform
import subprocess

def traceroute():
    destino = input("Digite o domínio ou IP de destino: ")
    sistema = platform.system()

    print(f"\nIniciando traceroute para {destino}...\n")

    try:
        if sistema == "Windows":
            subprocess.run(["tracert", destino])
        else:
            subprocess.run(["traceroute", destino])
    except Exception as e:
        print(f"[!] Erro ao executar traceroute: {e}")
