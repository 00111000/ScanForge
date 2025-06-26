import ipaddress
import socket
from tqdm import tqdm

PORTAS_COMUNS = [21, 22, 23, 80, 443, 3306, 8080]

def portas_comuns():
    rede_input = input("Digite a rede (ex: 192.168.0.0/24): ")

    try:
        rede = ipaddress.ip_network(rede_input, strict=False)
    except ValueError:
        print("[-] Endereço inválido.")
        return

    print(f"\nEscaneando portas comuns em hosts da rede {rede}...\n")

    for ip in tqdm(rede.hosts(), desc="IP"):
        ip_str = str(ip)
        for porta in PORTAS_COMUNS:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    resultado = sock.connect_ex((ip_str, porta))
                    if resultado == 0:
                        print(f"[+] {ip_str}:{porta} está aberto")
            except:
                pass
