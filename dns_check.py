# dns_check.py
import socket

def dns_check():
    dominio = input("Digite um domínio para testar (ex: google.com): ")
    try:
        ip = socket.gethostbyname(dominio)
        print(f"[+] DNS OK - {dominio} resolve para {ip}")
    except:
        print("[-] Falha na resolução DNS.")
