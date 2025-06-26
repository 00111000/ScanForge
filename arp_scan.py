# arp_scan.py
from scapy.all import ARP, Ether, srp

def arp_scan():
    alvo = input("Digite a rede para escanear (ex: 192.168.0.0/24): ")

    try:
        pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=alvo)
        print(f"\nEnviando pacotes ARP para {alvo}...\n")
        respostas, _ = srp(pacote, timeout=2, verbose=0)

        print("Dispositivos encontrados:")
        for _, recebido in respostas:
            print(f"IP: {recebido.psrc} \t MAC: {recebido.hwsrc}")

    except Exception as e:
        print(f"[!] Erro durante ARP Scan: {e}")
