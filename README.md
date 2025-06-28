# ScanForge
Ferramenta para o uso na área de redes. Projeto em desenvolvimento

**ScanForge** é uma ferramenta modular de análise, diagnóstico e segurança de redes, voltada para estudos práticos em laboratórios de redes de computadores. Desenvolvida em Python, oferece várias funções para inspeção de conectividade, identificação de dispositivos, detecção de vulnerabilidades e muito mais.

---

## 💻 Funcionalidades principais

* ✅ Scanner de rede por ping (`ping_sweep`)
* ✅ Verificação de DNS (`dns_check`)
* ✅ Scan de portas (`port_scan`)
* ✅ ARP Scan com Scapy (`arp_scan`)
* ✅ Traceroute (`traceroute`)
* ✅ Scanner de portas comuns em todos os hosts (`portas_comuns`)
* ✅ Sniffer de tráfego de rede (`sniffer`)
* ✅ Detector de ARP Spoofing (`arp_spoof_detect`)
* ✅ Teste de conexão com serviços externos (`conexao_externa`)
* ✅ Busca por compartilhamentos abertos FTP/SMB (`compartilhamentos`)
* ✅ Teste de latência contínua (`latency_test`)

---

## ⚙️ Requisitos

* Python 3.8+
* Permissões de administrador para algumas funções (sniffer, ARP)

### Instalação das dependências:

```bash
pip install -r requirements.txt
```

Dependências principais:

* `scapy`
* `tqdm`

---

## 🗜️ Estrutura do projeto

```
punktool/
├── punkmenu.py              # Menu principal da ferramenta
├── scanner.py              # Varredura de IPs via ping
├── dns_check.py            # Verificação de resolução DNS
├── port_scan.py            # Scanner de portas por IP
├── arp_scan.py             # Varredura ARP
├── traceroute.py           # Traçar rota até um destino
├── portas_comuns.py        # Scan de portas conhecidas em rede
├── sniffer.py              # Captura de pacotes
├── arp_spoof_detect.py     # Detector ARP Spoofing
├── conexao_externa.py      # Teste de conexão com serviços externos
├── compartilhamentos.py    # Busca por FTP/SMB
├── latency_test.py         # Teste de latência
├── utils.py                # Funções auxiliares (opcional)
└── requirements.txt        # Dependências do projeto
```

---

## 💿 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/punktool.git
cd punktool
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o menu principal:

```bash
python main.py
python3 main.py
```

---

## ⚠️ Uso educacional

Essa ferramenta é voltada para fins educacionais e laboratórios controlados. Não use em redes que você não tem autorização.

---

## 🎓 Autor

Desenvolvido por **\[00111000]**

---
