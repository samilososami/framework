#!/usr/bin/python3
import platform
import os 
from colorama import Fore, Style, init
import time 
import sys
import subprocess

# variables de formateo y colores
subrayado = '\033[4m'
morado = '\033[38;5;135m'



# sistema operativo y arquitectura
sistema = platform.system()
arquitectura = platform.architecture()[0]

# variables de estética
usuario_local = os.environ.get("SUDO_USER", "root")

# variables de prompt
modules = ""

main_prompt = f'''{Style.BRIGHT}{Fore.GREEN}╭──({Fore.YELLOW}{usuario_local}@framework{Style.RESET_ALL}{Fore.GREEN}{Style.BRIGHT})-[{Style.RESET_ALL}{Fore.MAGENTA}/{modules}{Fore.GREEN}{Style.BRIGHT}]{Style.RESET_ALL}{Fore.GREEN}
╰─{Style.BRIGHT}>{Style.RESET_ALL} '''

# variable de bucle principal
is_running = True

# variables de comandos
ip = "hostname -i"



def modules_list():
    print(f"\n{Fore.BLUE}{Style.BRIGHT}[+]{Style.RESET_ALL} Modulos disponibles:\n")
    print(f"\n{Fore.BLUE}[+]{Style.RESET_ALL} ")


def inicio():
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Aquí pondré el banner.\n")
    print(f"{Fore.YELLOW}[+] Sistema Operativo:{Fore.BLUE} {sistema}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] Arquitectura:{Fore.BLUE} {arquitectura}{Style.RESET_ALL}\n")
    if sistema != "Linux":
        print(f"{Fore.RED}[!] Este script está diseñado para linux, puede que algunos modulos no funcionen o algunas funciones no se muestren correctamente!{Style.RESET_ALL}\n")
    else:
         pass


def prompt(scanner_prompt):
    return input(main_prompt)

def instrucciones():
    if modules == "/modules/":
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}[+]{Style.RESET_ALL} Comandos en sección módulos:\n")
        print("list - listar módulos disponibles")
        print("use <modulo> - usar un módulo")
        print("back - volver al menú principal\n")
    else: 
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}[+]{Style.RESET_ALL} Comandos en sección módulos:\n")
        print("iface - lista las interfaces de red")
        print("ip - muestra la ip actual")
        print("salir - sale del script")
        print("clear - limpia la pantalla")
        print("modules - accede al directorio de módulos\n")


def comandos(comando):
    if comando == "help":
        instrucciones()
    elif comando == "ip":
        print(f"{Fore.BLUE}{Style.BRIGHT}[+]{Style.RESET_ALL} IP privada actual:\n")
        os.system(ip)
    elif comando == "clear":
        os.system("clear")
    elif comando == "salir": 
        sys.exit(0)
    elif comando == "modules": 
        global modules
        modules = "/modules/"
    elif comando == "back" and modules == "/modules/":
        modules = ""
    else:
        print(f"{Style.BRIGHT}{Fore.RED}[!]{Style.RESET_ALL}{Fore.RED} '{comando}' no es un comando válido, escribe help para listar los comandos disponibles.{Style.RESET_ALL}\n")

try:
    inicio()
    while is_running:
        user_input = prompt(modules)
        comandos(user_input)

except KeyboardInterrupt:
    print(f"\n\n{Fore.RED}[!] hasta la vista, baby{Style.RESET_ALL}")

