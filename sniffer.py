# sniffer.py
from scapy.all import sniff

def mostrar_pacote(pacote):
    print(pacote.summary())

def sniffer_start():
    interface = input("Digite a interface de rede (ex: eth0, wlan0): ")
    print(f"\nCapturando pacotes na interface {interface}... Pressione CTRL+C para parar.\n")

    try:
        sniff(iface=interface, prn=mostrar_pacote)
    except PermissionError:
        print("[!] Permissão negada. Execute como administrador (sudo).")
    except Exception as e:
        print(f"[!] Erro ao capturar pacotes: {e}")
