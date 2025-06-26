# utils.py

def validar_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or not 0 <= int(parte) <= 255:
            return False
    return True
