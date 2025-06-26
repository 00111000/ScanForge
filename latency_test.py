# latency_test.py
import subprocess
import platform
import time

def teste_latencia():
    destino = input("Digite o IP ou domínio para testar latência: ")
    sistema = platform.system()

    print(f"\nIniciando teste de latência com {destino} (CTRL+C para parar)...\n")

    try:
        while True:
            if sistema == "Windows":
                comando = ["ping", "-n", "1", destino]
            else:
                comando = ["ping", "-c", "1", destino]

            resultado = subprocess.run(comando, capture_output=True, text=True)
            print(resultado.stdout.splitlines()[-2] if sistema != "Windows" else resultado.stdout)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nTeste encerrado pelo usuário.")
