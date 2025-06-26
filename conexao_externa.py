# conexao_externa.py
import socket

def testar_conexao_externa():
    alvos = {
        "DNS Google": ("8.8.8.8", 53),
        "HTTP Google": ("google.com", 80),
        "HTTPS Google": ("google.com", 443),
        "FTP Debian": ("ftp.debian.org", 21),
    }

    print("\nTestando conexões com serviços externos...\n")

    for nome, (host, porta) in alvos.items():
        try:
            sock = socket.create_connection((host, porta), timeout=3)
            print(f"[+] {nome} OK ({host}:{porta})")
            sock.close()
        except Exception:
            print(f"[-] {nome} FALHOU ({host}:{porta})")
