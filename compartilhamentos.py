# compartilhamentos.py
import ipaddress
import socket
from tqdm import tqdm

PORTAS_SERVICOS = {
    21: "FTP",
    445: "SMB"
}

def buscar_compartilhamentos():
    rede_input = input("Digite a rede (ex: 192.168.0.0/24): ")

    try:
        rede = ipaddress.ip_network(rede_input, strict=False)
    except ValueError:
        print("[-] Endereço inválido.")
        return

    print(f"\nProcurando compartilhamentos FTP/SMB na rede {rede}...\n")

    for ip in tqdm(rede.hosts(), desc="IP"):
        ip = str(ip)
        for porta, nome_servico in PORTAS_SERVICOS.items():
            try:
                sock = socket.socket()
                sock.settimeout(0.5)
                resultado = sock.connect_ex((ip, porta))
                if resultado == 0:
                    print(f"[+] {nome_servico} aberto em {ip}:{porta}")
                sock.close()
            except:
                pass
