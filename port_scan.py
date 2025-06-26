# port_scan.py
import socket

def port_scan():
    host = input("Digite o IP do host para escanear: ")
    portas = input("Digite as portas (ex: 22,80,443): ").split(',')

    print(f"\nEscaneando {host} nas portas {portas}...\n")
    for porta in portas:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, int(porta)))
            if resultado == 0:
                print(f"[+] Porta {porta} aberta")
            else:
                print(f"[-] Porta {porta} fechada")
            sock.close()
        except:
            print(f"[!] Erro ao escanear porta {porta}")
