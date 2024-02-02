import ipaddress
from colorama import Fore, Style

def calcular_mascara_cidr(num_hosts):
    bits_necesarios = num_hosts.bit_length()

    mascara_cidr = 32 - bits_necesarios

    return mascara_cidr

def calcular_info_red(ip, num_hosts):
    mascara_cidr = calcular_mascara_cidr(num_hosts)

    red = ipaddress.IPv4Network(f"{ip}/{mascara_cidr}", strict=False)

    mascara_red = red.netmask

    broadcast = red.broadcast_address

    total_direcciones = 2**(32 - mascara_cidr)

    direcciones_utilizables = total_direcciones - 2

    direcciones_desperdiciadas = max(0, total_direcciones - num_hosts - 2)

    print(f"{Fore.GREEN}IP de Red:{Style.RESET_ALL} {red.network_address}")
    print(f"{Fore.GREEN}Máscara de Red (CIDR):{Style.RESET_ALL} /{mascara_cidr}")
    print(f"{Fore.GREEN}IP de Broadcast:{Style.RESET_ALL} {broadcast}")
    print(f"{Fore.CYAN}Número total de direcciones en la red:{Style.RESET_ALL} {total_direcciones}")
    print(f"{Fore.CYAN}Direcciones utilizables:{Style.RESET_ALL} {direcciones_utilizables}")
    print(f"{Fore.CYAN}Direcciones desperdiciadas:{Style.RESET_ALL} {direcciones_desperdiciadas}")

ip = input(f"{Fore.YELLOW}Introduce la IP de red:{Style.RESET_ALL} ")
num_hosts = int(input(f"{Fore.YELLOW}Introduce el número de hosts:{Style.RESET_ALL} "))

calcular_info_red(ip, num_hosts)
