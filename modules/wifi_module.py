# ----------- FUNCIONES WIFI ------------

import platform
from colorama import Fore, Style
import subprocess
sistema = platform.system()

def interfaces_inhalambricas():
    if sistema == "Linux":
        resultado_iwconfig = subprocess.run(["iwconfig"], capture_output=True, text=True)
    
        interfaz_actual = None
        interfaces_modos = []

        for line in resultado_iwconfig.stdout.splitlines():
            if line and not line.startswith(' '):
                interfaz_actual = line.split()[0]

            elif "Mode:" in line and interfaz_actual:
                contenido = line.split(":")[1].strip()
                modo_concreto = contenido.split()[0]
                interfaces_modos.append((interfaz_actual, modo_concreto))


    # si no se encuentra ninguna interfaz:
        if not interfaces_modos:
            print(f"\n{Fore.RED}[!] No se han encontrado interfaces inhalambricas!")
        else:
            cantidad = len(interfaces_modos)
            print(f"{Fore.BLUE}{Style.BRIGHT}[+]{Style.RESET_ALL} {Fore.CYAN}{cantidad}{Style.RESET_ALL} interfaces inhalambricas encontradas:\n")

            for iface, modo in interfaces_modos:
                print(f"{Fore.GREEN}Interfaz:{Style.RESET_ALL} {iface}")
                print(f"{Fore.GREEN}Modo:{Style.RESET_ALL} {modo}\n")
    else:
        print(f"{Fore.RED}[!] Windows no es compatible con el módulo wifi!{Style.RESET_ALL}")
