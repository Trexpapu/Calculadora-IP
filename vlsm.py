import tkinter as tk
from tkinter import ttk
import ipaddress

def calcular_direccion_red(ip, prefijo):
    direccion_ip = ipaddress.IPv4Address(ip)
    mascara_subred = ipaddress.IPv4Network(ip + '/' + str(prefijo), strict=False).network_address
    return str(mascara_subred)

def calcular_prefijo(ip, hosts):
    # Convertir la dirección IP a un objeto IPv4
    direccion_ip = ipaddress.IPv4Address(ip)
    
    # Convertir la entrada del usuario en una lista de enteros
    lista_hosts = list(map(int, hosts.split()))

    # Calcular el número de bits requeridos para la cantidad de hosts
    bits_necesarios = (max(lista_hosts) + 1).bit_length()  # Sumamos 1 para incluir el número de hosts
    
    # Calcular el prefijo
    prefijo = 32 - bits_necesarios

    return prefijo

def calcular_primera_subred(ip, prefijo, hosts):
    # Convertir la dirección IP a un objeto IPv4
    direccion_ip = ipaddress.IPv4Address(ip)
    
    # Convertir la entrada del usuario en una lista de enteros
    lista_hosts = list(map(int, hosts.split()))

    # Calcular el número de bits requeridos para la cantidad de hosts
    bits_necesarios = (max(lista_hosts) + 1).bit_length()  # Sumamos 1 para incluir el número de hosts
    
    # Calcular el nuevo prefijo
    nuevo_prefijo = 32 - bits_necesarios

    # Calcular las subredes
    subredes = list(ipaddress.IPv4Network(ip + '/' + str(prefijo), strict=False).subnets(new_prefix=nuevo_prefijo))
    cantidad = len(subredes)

    # Devolver la primera subred
    return subredes[0]

def calcular_mascara(prefijo):
    # Calcular la máscara de subred
    mascara_binaria = "1" * prefijo + "0" * (32 - prefijo)
    mascara_decimal = [int(mascara_binaria[i:i+8], 2) for i in range(0, 32, 8)]

    return ".".join(map(str, mascara_decimal))

def calcular_primera_direccion_ip(subred):
    # Obtener la primera dirección IP de la subred
    return subred.network_address + 1

def calcular_broadcast(subred):
    # Obtener la dirección de broadcast de la subred
    return subred.broadcast_address

def calcular_ips_utiles(subred):
    # Obtener la primera dirección IP y la dirección de broadcast
    primera_direccion = subred.network_address + 1
    broadcast = subred.broadcast_address

    # Obtener la lista de direcciones IP útiles
    ips_utiles = list(ipaddress.IPv4Network(subred).hosts())
    
    # Excluir la dirección de red y la dirección de broadcast si están presentes
    if primera_direccion in ips_utiles:
        ips_utiles.remove(primera_direccion)
    if broadcast in ips_utiles:
        ips_utiles.remove(broadcast)

    return ips_utiles

def vlsm_main(ip, prefijo, hosts_input):
    resultados = []

    hosts_nuevos = [int(host.strip()) for host in hosts_input.split(',')]
    C_host = len(hosts_nuevos)

    for i in range(C_host):
        if i == 0:
            prefijo_calculado = calcular_prefijo(ip, str(hosts_nuevos[0]))
            primera_subred_calculada = calcular_primera_subred(ip, prefijo_calculado, str(hosts_nuevos[0]))
            mascara_calculada = calcular_mascara(prefijo_calculado)
            primera_direccion_ip_calculada = calcular_primera_direccion_ip(primera_subred_calculada)
            broadcast_calculado = calcular_broadcast(primera_subred_calculada)
            ips_utiles_calculadas = len(calcular_ips_utiles(primera_subred_calculada)) + 1
        else:
            nueva_ip = str(broadcast_calculado + 1)
            prefijo_calculado = calcular_prefijo(nueva_ip, str(hosts_nuevos[i]))
            primera_subred_calculada = calcular_primera_subred(nueva_ip, prefijo_calculado, str(hosts_nuevos[i]))
            mascara_calculada = calcular_mascara(prefijo_calculado)
            primera_direccion_ip_calculada = calcular_primera_direccion_ip(primera_subred_calculada)
            broadcast_calculado = calcular_broadcast(primera_subred_calculada)
            ips_utiles_calculadas = len(calcular_ips_utiles(primera_subred_calculada)) + 1

        resultados.append((
            str(hosts_nuevos[i]),
            str(prefijo_calculado),
            str(primera_subred_calculada),
            str(mascara_calculada),
            str(primera_direccion_ip_calculada),
            str(broadcast_calculado),
            str(ips_utiles_calculadas)
        ))

    return resultados

def mostrar_resultados(ip, prefijo, hosts_input):
    resultados = vlsm_main(ip, prefijo, hosts_input)

    # Crear una ventana secundaria para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados VLSM")

    # Crear un treeview para mostrar los resultados en forma de tabla
    tree = ttk.Treeview(ventana_resultados)
    tree["columns"] = ("Host", "Prefijo", "Subred", "Máscara", "Primera IP", "Broadcast", "IPs Útiles")
    
    # Configurar las columnas
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Host", anchor=tk.CENTER, width=100)
    tree.column("Prefijo", anchor=tk.CENTER, width=100)
    tree.column("Subred", anchor=tk.CENTER, width=150)
    tree.column("Máscara", anchor=tk.CENTER, width=150)
    tree.column("Primera IP", anchor=tk.CENTER, width=150)
    tree.column("Broadcast", anchor=tk.CENTER, width=150)
    tree.column("IPs Útiles", anchor=tk.CENTER, width=150)

    # Configurar encabezados
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Host", text="Host", anchor=tk.CENTER)
    tree.heading("Prefijo", text="Prefijo", anchor=tk.CENTER)
    tree.heading("Subred", text="Subred", anchor=tk.CENTER)
    tree.heading("Máscara", text="Máscara", anchor=tk.CENTER)
    tree.heading("Primera IP", text="Primera IP", anchor=tk.CENTER)
    tree.heading("Broadcast", text="Broadcast", anchor=tk.CENTER)
    tree.heading("IPs Útiles", text="IPs Útiles", anchor=tk.CENTER)
    # Insertar los resultados en el treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)

    # Empaquetar el treeview
    tree.pack(expand=tk.YES, fill=tk.BOTH)


