# scanner.py
import ipaddress
import platform
import subprocess
import time
from tqdm import tqdm
from report import salvar_relatorio

def ping_sweep():
    rede_input = input("Digite a rede (ex: 192.168.0.0/24): ")

    try:
        rede = ipaddress.ip_network(rede_input, strict=False)
    except ValueError:
        print("[-] Endereço de rede inválido.")
        return

    print(f"\nEscaneando hosts em {rede}...\n")

    sistema = platform.system()
    if sistema == "Windows":
        ping_cmd = "ping -n 1 -w 1000"
        redirecionar = ">nul"
    else:
        ping_cmd = "ping -c 1 -W 1"
        redirecionar = ">/dev/null 2>&1"

    ativos = []
    ultimo_ativo = time.time()

    for ip in tqdm(rede.hosts(), desc="Escaneando"):
        resposta = subprocess.call(f"{ping_cmd} {ip} {redirecionar}", shell=True)
        if resposta == 0:
            print(f"[+] Host ativo: {ip}")
            ativos.append(str(ip))
            ultimo_ativo = time.time()

        # Verifica se passaram 60s desde o último host ativo
        if time.time() - ultimo_ativo > 60:
            print("\n⏳ Nenhum novo host ativo encontrado nos últimos 60 segundos.")
            break

    print("\n✅ Varredura concluída.")
    if ativos:
        print(f"\nHosts ativos encontrados ({len(ativos)}):")
        for ip in ativos:
            print(f" - {ip}")

        # Gera relatório
        relatorio = "Hosts ativos encontrados:\n"
        relatorio += "\n".join(ativos)
        salvar_relatorio("relatorio_ping.txt", relatorio)
    else:
        print("Nenhum host ativo encontrado.")

    input("\nPressione ENTER para retornar ao menu...")
