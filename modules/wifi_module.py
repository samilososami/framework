#-------------------MÓDULO-WIFI-------------------------------

from colorama import Fore, Style
import subprocess
import platform
import time

sistema = platform.system()

def interfaces():
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
            print(f"\n{Fore.RED}[!] No se han encontrado interfaces inhalambricas!\n")
            return

        cantidad = len(interfaces_modos)
        if cantidad > 1:
            print(f"\n{Fore.BLUE}{Style.BRIGHT}[+]{Style.RESET_ALL} {Fore.CYAN}{cantidad}{Style.RESET_ALL} interfaces inhalambricas encontradas:")
        else:
            print(f"\n{Fore.BLUE}{Style.BRIGHT}[+]{Style.RESET_ALL} {Fore.CYAN}{cantidad}{Style.RESET_ALL} interfaz inhalámbrica encontrada:")

        # cálculo dinámico de las interfaces
        max_iface_len = max(len(iface) for iface, _ in interfaces_modos)
        max_mode_len = max(len(modo) for _, modo in interfaces_modos)

        # padding adicional para mejorar visualización
        iface_col_width = max_iface_len + 10
        mode_col_width = max_mode_len + 10

        # línea separadora
        linea = "+" + "-" * iface_col_width + "+" + "-" * mode_col_width + "+"

        # Encabezado
        print(linea)
        print(f" {Fore.YELLOW}{'Interfaz'.ljust(iface_col_width)} {'Modo'.ljust(mode_col_width)} {Style.RESET_ALL}")
        print(linea)

        # filas de datos
        for iface, modo in interfaces_modos:
            # Aplicar ljust() y color al modo
            modo_sin_formato = modo.strip()
            modo_formateado = modo.ljust(mode_col_width)
            if modo_formateado == "Managed".ljust(mode_col_width):
                modo_formateado = f"{Fore.MAGENTA}{modo_formateado}{Style.RESET_ALL}"
            elif modo_formateado == "Monitor".ljust(mode_col_width):
                modo_formateado = f"{Fore.GREEN}{Style.BRIGHT}{modo_formateado}{Style.RESET_ALL}"

            print(f" {Fore.CYAN}{iface.ljust(iface_col_width)}{Style.RESET_ALL} {modo_formateado} ")
            print(linea)
            print()
            
            nombres_interfaces = [iface for iface, _ in interfaces_modos]
            interfaz_principal = ""
            while interfaz_principal not in nombres_interfaces:
                interfaz_principal = input(f"{Fore.GREEN}[+]{Style.RESET_ALL} Escoge una interfaz: ")
                if interfaz_principal not in nombres_interfaces:
                    print(f"{Fore.RED}[!] La interfaz no se encuentra entre las detectadas!{Style.RESET_ALL}")

                
            if modo_sin_formato == "Monitor":
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Modo monitor activado previamente.")
            else:
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Activando modo monitor...")
                time.sleep(0.5)
                subprocess.run(["airmon-ng", "start", interfaz_principal])

    else:
        print(f"{Fore.RED}[!] {sistema} no es compatible con el módulo wifi!{Style.RESET_ALL}")

  
