#!/usr/bin/env python3
import subprocess
import sys
import os

# Colores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""
{CYAN}{BOLD}
╔════════════════════════════════════════════════════╗
║                  MQTT Tool v1.0                    ║
║        Cliente interactivo para Mosquitto          ║
║                  Creado por feer248                ║
╚════════════════════════════════════════════════════╝
{RESET}
""")

def menu():
    print(f"{BOLD}Selecciona un modo de operación:{RESET}")
    print(f"{CYAN}[1]{RESET} Suscribirse a un tópico (mosquitto_sub)")
    print(f"{CYAN}[2]{RESET} Publicar en un tópico (mosquitto_pub)")
    print(f"{CYAN}[0]{RESET} Salir")

def modo_subscripcion():
    clear()
    print(f"{GREEN}{BOLD}=== MODO SUBSCRIPCIÓN ==={RESET}\n")
    servidor = input(f"{BOLD}Servidor MQTT:{RESET} ").strip()
    topico = input(f"{BOLD}Tópico:{RESET} ").strip()

    if not servidor or not topico:
        print(f"\n{RED}[ERROR]{RESET} El servidor y el tópico son obligatorios.\n")
        return

    comando = ["mosquitto_sub", "-h", servidor, "-t", topico]
    print(f"\n{YELLOW}[INFO]{RESET} Ejecutando: {BOLD}{' '.join(comando)}{RESET}\n")

    try:
        subprocess.run(comando)
    except FileNotFoundError:
        print(f"{RED}[ERROR]{RESET} 'mosquitto_sub' no está instalado o no se encuentra en el PATH.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Error al ejecutar mosquitto_sub: {e}")

def modo_publicacion():
    clear()
    print(f"{GREEN}{BOLD}=== MODO PUBLICACIÓN ==={RESET}\n")
    servidor = input(f"{BOLD}Servidor MQTT:{RESET} ").strip()
    puerto = input(f"{BOLD}Puerto (opcional):{RESET} ").strip()
    topico = input(f"{BOLD}Tópico:{RESET} ").strip()
    mensaje = input(f"{BOLD}Mensaje:{RESET} ").strip()

    if not servidor or not topico or not mensaje:
        print(f"\n{RED}[ERROR]{RESET} El servidor, el tópico y el mensaje son obligatorios.\n")
        return

    comando = ["mosquitto_pub", "-h", servidor]
    if puerto:
        comando += ["-p", puerto]
    comando += ["-t", topico, "-m", mensaje]

    print(f"\n{YELLOW}[INFO]{RESET} Ejecutando: {BOLD}{' '.join(comando)}{RESET}\n")

    try:
        subprocess.run(comando)
    except FileNotFoundError:
        print(f"{RED}[ERROR]{RESET} 'mosquitto_pub' no está instalado o no se encuentra en el PATH.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Error al ejecutar mosquitto_pub: {e}")

def main():
    while True:
        clear()
        banner()
        menu()
        opcion = input(f"\n{BOLD}Opción:{RESET} ").strip()

        if opcion == "1":
            modo_subscripcion()
            input(f"\n{CYAN}Presiona Enter para volver al menú...{RESET}")
        elif opcion == "2":
            modo_publicacion()
            input(f"\n{CYAN}Presiona Enter para volver al menú...{RESET}")
        elif opcion == "0":
            print(f"\n{GREEN}¡Hasta pronto!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[ERROR]{RESET} Opción no válida.")
            input(f"{CYAN}Presiona Enter para continuar...{RESET}")

if __name__ == "__main__":
    main()
