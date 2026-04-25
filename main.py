#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import ctypes
import subprocess
import platform

# ====================== BANNER BIEN PASADO DE VERGA ======================
def mostrar_banner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    banner = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  {chr(27)}[91m██████╗ ███████╗██████╗     ██████╗ ██╗{chr(27)}[0m                         ║
║  {chr(27)}[91m██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║{chr(27)}[0m                         ║
║  {chr(27)}[91m██║  ██║█████╗  ██████╔╝    ██║  ██║██║{chr(27)}[0m                         ║
║  {chr(27)}[91m██║  ██║██╔══╝  ██╔══██╗    ██║  ██║██║{chr(27)}[0m                         ║
║  {chr(27)}[91m██████╔╝███████╗██║  ██║    ██████╔╝███████╗{chr(27)}[0m                   ║
║  {chr(27)}[91m╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝{chr(27)}[0m                   ║
║                                                                           ║
║  {chr(27)}[93m██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗{chr(27)}[0m       ║
║  {chr(27)}[93m██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝{chr(27)}[0m       ║
║  {chr(27)}[93m██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗{chr(27)}[0m       ║
║  {chr(27)}[93m██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║{chr(27)}[0m       ║
║  {chr(27)}[93m╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║{chr(27)}[0m       ║
║  {chr(27)}[93m ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝{chr(27)}[0m       ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {chr(27)}[95m🔥  WINDOWS RED PITADORA v1.0  🔥{chr(27)}[0m                                    ║
║                                                                           ║
║  {chr(27)}[91m[!] Solo para pruebas en redes con autorización expresa.{chr(27)}[0m                  ║
║  {chr(27)}[91m[!] El mal uso de esta herramienta puede ser ILEGAL.{chr(27)}[0m                       ║
║  {chr(27)}[91m[!] El autor no se hace responsable por pendejadas ajenas.{chr(27)}[0m                 ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  {chr(27)}[92m[✓] SISTEMA: {platform.system()} {platform.release()}{chr(27)}[0m                                    ║
║  {chr(27)}[92m[✓] PYTHON: {sys.version.split()[0]}{chr(27)}[0m                                                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)

# ====================== VERIFICAR ADMIN ======================
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def verificar_admin():
    if not is_admin():
        print(f"\n{chr(27)}[91m[!] ALV! No tienes permisos de administrador.{chr(27)}[0m")
        print(f"{chr(27)}[93m[!] Esta herramienta requiere ejecutarse como ADMIN.{chr(27)}[0m")
        print(f"{chr(27)}[93m[!] Re-lanzando con privilegios elevados...{chr(27)}[0m\n")
        
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

# ====================== MENÚ PRINCIPAL ======================
def mostrar_menu():
    menu = f"""
{chr(27)}[96m╔════════════════════════════════════════════════════════════╗{chr(27)}[0m}
{chr(27)}[96m║                    MENÚ DE DESMADRE                        ║{chr(27)}[0m}
{chr(27)}[96m╠════════════════════════════════════════════════════════════╣{chr(27)}[0m}
{chr(27)}[96m║                                                            ║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[1]{chr(27)}[0m] Escáner de red (descubre hosts vivos)               {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[2]{chr(27)}[0m Escáner de puertos (TCP/UDP)                       {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[3]{chr(27)}[0m Sniffer de paquetes (captura en vivo)                {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[4]{chr(27)}[0m ARP Spoofer (redirect tráfico)                      {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[5]{chr(27)}[0m MAC Changer (cambia MAC de interfaz)                {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[6]{chr(27)}[0m TCP Flood (ataque de estrés ligero)                 {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[7]{chr(27)}[0m Ping of Death (paquete gigante)                     {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[8]{chr(27)}[0m Información de red (IP, MAC, gateway)               {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║  {chr(27)}[93m[9]{chr(27)}[0m Salir                                             {chr(27)}[96m║{chr(27)}[0m}
{chr(27)}[96m║                                                            ║{chr(27)}[0m}
{chr(27)}[96m╚════════════════════════════════════════════════════════════╝{chr(27)}[0m}
"""
    print(menu)

# ====================== FUNCIONES CHIDAS (SCRIPTS POSTERIORES) ======================
def escaner_red():
    print(f"\n{chr(27)}[92m[+] Iniciando escáner de red...{chr(27)}[0m")
    # TODO: Implementar escaneo ARP/ICMP
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def escaner_puertos():
    print(f"\n{chr(27)}[92m[+] Iniciando escáner de puertos...{chr(27)}[0m")
    # TODO: Implementar escaneo SYN/Connect
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def sniffer():
    print(f"\n{chr(27)}[92m[+] Iniciando sniffer de paquetes...{chr(27)}[0m")
    # TODO: Implementar captura con raw sockets
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def arp_spoof():
    print(f"\n{chr(27)}[92m[+] Iniciando ARP Spoofer...{chr(27)}[0m")
    # TODO: Implementar ARP poisoning
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def mac_changer():
    print(f"\n{chr(27)}[92m[+] Cambiando MAC address...{chr(27)}[0m")
    # TODO: Implementar cambio de MAC por registro
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def tcp_flood():
    print(f"\n{chr(27)}[91m[!] TCP Flood - Solo usar en equipos propios{chr(27)}[0m")
    # TODO: Implementar flood controlado
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def ping_of_death():
    print(f"\n{chr(27)}[91m[!] Ping of Death - Solo usar en equipos propios{chr(27)}[0m")
    # TODO: Implementar ping gigante
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

def info_red():
    print(f"\n{chr(27)}[92m[+] Obteniendo información de red...{chr(27)}[0m")
    # Mostrar ipconfig
    subprocess.run(["ipconfig", "/all"], shell=True)
    input(f"\n{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

# ====================== MAIN ======================
def main():
    verificar_admin()  # Aquí se fuerza el modo admin
    
    while True:
        mostrar_banner()
        mostrar_menu()
        
        opcion = input(f"\n{chr(27)}[96m└─[{chr(27)}[91mFalconmx1@{chr(27)}[93mwindows-red-pitadora{chr(27)}[96m}]─[~]➤ {chr(27)}[0m")
        
        if opcion == "1":
            escaner_red()
        elif opcion == "2":
            escaner_puertos()
        elif opcion == "3":
            sniffer()
        elif opcion == "4":
            arp_spoof()
        elif opcion == "5":
            mac_changer()
        elif opcion == "6":
            tcp_flood()
        elif opcion == "7":
            ping_of_death()
        elif opcion == "8":
            info_red()
        elif opcion == "9":
            print(f"\n{chr(27)}[93m[!] Saliendo... Nos vemos en el infierno, bro{chr(27)}[0m")
            sys.exit()
        else:
            print(f"\n{chr(27)}[91m[!] Opción no válida, pendejo{chr(27)}[0m")
            input(f"{chr(27)}[93mPresiona Enter para continuar...{chr(27)}[0m")

if __name__ == "__main__":
    main()
