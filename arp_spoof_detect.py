# arp_spoof_detect.py
from scapy.all import ARP, sniff

def detectar_arp_spoofing():
    print("\nMonitorando rede para detectar ARP Spoofing... Pressione CTRL+C para sair.\n")
    try:
        sniff(filter="arp", store=False, prn=verificar_arp)
    except Exception as e:
        print(f"[!] Erro na captura: {e}")

tabela_arp = {}

def verificar_arp(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:  # is-at
        ip = pacote[ARP].psrc
        mac = pacote[ARP].hwsrc

        if ip in tabela_arp:
            if tabela_arp[ip] != mac:
                print(f"[!] POSSÍVEL ARP SPOOFING DETECTADO: IP {ip} mudou de {tabela_arp[ip]} para {mac}")
        else:
            tabela_arp[ip] = mac
