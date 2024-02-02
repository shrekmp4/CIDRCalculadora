# Calculadora de Redes IP

Esta es una calculadora simple en Python que te permite obtener información relevante sobre una red IP dado un rango de hosts. Puede ser útil para planificar y entender mejor la distribución de direcciones en una red.

## Requisitos

- Python 3.x
- Biblioteca `ipaddress`
- Biblioteca `colorama`

## Uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/shrek.mp4/CIDRAutoPy.git

2. Instala las bibliotecas requeridas:
   ```bash
   pip install ipaddress colorama

3. Ejecuta el script:

   ```bash
   python calculadora_redes.py

4. Sigue las instrucciones para ingresar la dirección IP de la red y el número de hosts.


5. Ejemplo de Salida

   ```bash
   Introduce la IP de red: 192.168.1.0
   Introduce el número de hosts: 25
    
   IP de Red: 192.168.1.0
   Máscara de Red (CIDR): /27
   IP de Broadcast: 192.168.1.31
   Número total de direcciones en la red: 32
   Direcciones utilizables: 30
   Direcciones desperdiciadas: 7

6. Apoya el proyecto presionando ⭐
