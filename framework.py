#!/usr/bin/python3
import platform
import os 
from colorama import Fore, Style, init
import time 
import sys
import subprocess
from modules import wifi_module
from modules import bluetooth_module
import getpass

# variables de formateo y colores
subrayado = '\033[4m'
morado = '\033[38;5;135m'


# sistema operativo y arquitectura
sistema = platform.system()
arquitectura = platform.architecture()[0]

# variables de estética
usuario = getpass.getuser()


# variables de prompt
modules = ""
modulo_especifico = ""
mod = ""

# variable de bucle principal
is_running = True

# variables de arquitectura
clearL = "clear"
clearW = "cls"

# wifi

 




# funcion de inicio: banner e información sobre el sistema
def inicio():
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Aquí pondré el banner.\n")
    print(f"{Fore.YELLOW}[+] Sistema Operativo:{Fore.BLUE} {sistema}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Arquitectura:{Fore.BLUE} {arquitectura}{Style.RESET_ALL}\n")
    if sistema != "Linux":
        print(f"{Fore.RED}[!] Este script está diseñado para linux, puede que algunos modulos no funcionen o algunas funciones no se muestren correctamente!{Style.RESET_ALL}\n")
    elif sistema != "Linux":
        global clear 
        clear = "cls"
    else:
         pass


# lista de módulos
def list_modules():
    print("\n╭────────────────────────────────────╮")
    print("│               Módulos              │")
    print("╰────────────────────────────────────╯")
    print("\nMódulos disponibles:")
    print("  wifi       - Captura de Handshake, Ataques WPS, Desautenticación")
    print("  bluetooth  - BLE, Bluesnarfing, Enumeración de dispositivos")
    print("  cracking   - Aircrack-ng, Hashcat, JohnTheRipper\n")


# funciones de los módulos
def wifi():
    global modulo_especifico
    modulo_especifico = "/wifi"

def bluetooth():
    global modulo_especifico
    modulo_especifico = "/bluetooth"

def cracking():
    global modulo_especifico 
    modulo_especifico = "/cracking"



# función para mostrar el prompt
def prompt(modules):
    return input(f'''{Style.BRIGHT}{Fore.GREEN}╭──({Fore.YELLOW}{usuario}@framework{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT})-[{Style.RESET_ALL}{Fore.MAGENTA}{Style.BRIGHT}/{modules}{Style.RESET_ALL}{Fore.MAGENTA}{modulo_especifico}{Fore.GREEN}{Style.BRIGHT}]{Style.RESET_ALL}{Fore.GREEN}
╰─{Style.BRIGHT}>{Style.RESET_ALL} ''')


# función para mostrar las instrucciones. el 'help' de toda la vida
def instrucciones():
    if modulo_especifico == "/wifi" and modules == "modules":
        print("\n╭────────────────────────────────────╮")
        print("│               Wifi                 │")
        print("╰────────────────────────────────────╯")
        print("\nComandos disponibles:")
        print("  interfaces/i  - Muestra y elecciona una interfaz compatible")
        print("  monitor/m    - Activa el modo monitor en la interfaz seleccionada")
        print("  scan/s     - Escanea las redes cercanas")
        print("  back      - retrocede al directorio anterior\n")



    elif modulo_especifico == "" and modules == "modules":
        print("\n╭────────────────────────────────────╮")
        print(f"│            Sección {Fore.MAGENTA}Módulos{Style.RESET_ALL}         │")
        print("╰────────────────────────────────────╯")
        print("\nComandos disponibles:")
        print("  list        - Listar módulos disponibles")
        print("  go <módulo> - Accede al módulo seleccionado")
        print("  back        - Volver al menú principal\n")
    







    else:
        print("\n╭────────────────────────────────────╮")
        print(f"│         Comandos {Fore.MAGENTA}Básicos{Style.RESET_ALL}           │")
        print("╰────────────────────────────────────╯")
        print("\nComandos disponibles:")
        print("  salir/exit  - Sale del script")
        print("  clear       - Limpia la pantalla")
        print("  modules     - Accede al directorio de módulos")
        print("  x <comando> - Ejecuta un comando a nivel de sistema (ej. 'x whoami')\n")



# función del bucle principal. se gestionan los comandos del usuario
def comandos(comando):
    global modules
    global modulo_especifico
    if comando == "help":
        instrucciones()
    elif comando == "clear":
        if sistema == "Linux":
            os.system(clearL)
        else:
            os.system(clearW)
    elif comando == "salir" or comando == "exit": 
        sys.exit(0)
    elif comando.startswith("x "):
        cmd = comando[2:]
        os.system(cmd)
    elif comando == "x":
        print(f"{Fore.RED} [!] 'x' necesita un comando a ejecutar (ex. 'x whoami')")
    elif comando == "modules" and modules == "": 
        modules = "modules"
        instrucciones()
    elif comando == "modules" and modules == "modules":
        print(f"{Fore.RED}[!] Ya estás en el directorio de módulos!{Style.RESET_ALL}")
    elif comando == "list" and modules == "modules":
        list_modules()
    # retroceder directorio 
    elif comando == "back" and modulo_especifico != "":
        modulo_especifico = ""
    elif comando == "back" and modules == "modules":
        modules = ""
    
    # modulos concretos
    elif comando.startswith("go ") and modules == "modules":
        mod = comando[3:].strip().lower()
        if mod == "wifi":
            wifi()
            instrucciones()
        elif mod == "bluetooth":
            bluetooth()
        elif mod == "cracking":
            cracking()
        else: 
            print(f"{Fore.RED}[!] El módulo '{mod}' no existe. Escribe {Fore.WHITE}list{Fore.RED} para listar los módulos disponibles.{Style.RESET_ALL}")

    # comandos wifi 
    elif modulo_especifico == "/wifi" and comando == "scan":
        pass
    elif modulo_especifico == "/wifi" and comando == "interfaces" or modulo_especifico == "/wifi" and comando == "i":
        try:
            wifi_module.interfaces()
        except KeyboardInterrupt:
            print()
            pass
    elif modulo_especifico == "/wifi" and comando == "monitor" or modulo_especifico == "/wifi" and comando == "m":
        wifi_module.modo_monitor()
    elif modulo_especifico == "/wifi" and comando == "scan" or modulo_especifico == "/wifi" and comando == "s":
        wifi_module.escanear_redes_en_xterm()
    


    else:
        print(f"{Style.BRIGHT}{Fore.RED}[!]{Style.RESET_ALL}{Fore.RED} '{comando}' no es un comando válido, escribe {Fore.WHITE}help{Fore.RED} para listar los comandos disponibles.{Style.RESET_ALL}\n")




try:
    inicio()
    while is_running:
        user_input = prompt(modules)
        comandos(user_input)

except KeyboardInterrupt:
    print(f"\n{Fore.RED}[!] hasta la vista, baby{Style.RESET_ALL}")
