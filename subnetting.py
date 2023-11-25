import tkinter as tk
from tkinter import ttk
import ipaddress

def subnetting(ip, prefijo, hosts_input):
    hosts = [int(host.strip()) for host in hosts_input.split(',')]
    C_host = len(hosts)
    red_original = ipaddress.IPv4Network(f"{ip}/{prefijo}", strict=False)

    # Calcular bits necesarios para hosts
    bits_hosts = max(hosts).bit_length()

    # Convertir prefijo a entero
    prefijo = int(prefijo)

    # Calcular nuevo prefijo para subredes
    nuevo_prefijo = prefijo + bits_hosts

    # Calcular nueva máscara de subred
    nueva_mascara = ipaddress.IPv4Network(f"{ip}/{nuevo_prefijo}", strict=False).netmask

    resultados = []

    for i, num_hosts in enumerate(hosts):
        # Calcular nueva dirección de subred
        nueva_ip = red_original.network_address + i * (2 ** bits_hosts)
        nueva_subred = ipaddress.IPv4Network(f"{nueva_ip}/{nuevo_prefijo}", strict=False)

        # Calcular cantidad de hosts utilizables
        cantidad_ips_usables = 2 ** bits_hosts - 2

        resultados.append((
            i + 1,
            str(nueva_subred.network_address),
            str(nuevo_prefijo),
            str(nueva_mascara),
            str(nueva_subred.network_address + 1),
            str(nueva_subred.broadcast_address),
            str(cantidad_ips_usables)
        ))

    return resultados

def mostrar_resultados_subnetting(ip, prefijo, hosts):
    resultados = subnetting(ip, prefijo, hosts)

    # Crear una ventana secundaria para mostrar los resultados
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados Subnetting")

    # Crear un treeview para mostrar los resultados en forma de tabla
    tree = ttk.Treeview(ventana_resultados)
    tree["columns"] = ("Subred", "Dirección de Subred", "Prefijo", "Máscara", "Primera IP", "Broadcast", "Cantidad IPs Usables")
    
    # Configurar las columnas
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Subred", anchor=tk.CENTER, width=100)
    tree.column("Dirección de Subred", anchor=tk.CENTER, width=150)
    tree.column("Prefijo", anchor=tk.CENTER, width=100)
    tree.column("Máscara", anchor=tk.CENTER, width=150)
    tree.column("Primera IP", anchor=tk.CENTER, width=150)
    tree.column("Broadcast", anchor=tk.CENTER, width=150)
    tree.column("Cantidad IPs Usables", anchor=tk.CENTER, width=150)

    # Configurar encabezados
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Subred", text="Subred", anchor=tk.CENTER)
    tree.heading("Dirección de Subred", text="Dirección de Subred", anchor=tk.CENTER)
    tree.heading("Prefijo", text="Prefijo", anchor=tk.CENTER)
    tree.heading("Máscara", text="Máscara", anchor=tk.CENTER)
    tree.heading("Primera IP", text="Primera IP", anchor=tk.CENTER)
    tree.heading("Broadcast", text="Broadcast", anchor=tk.CENTER)
    tree.heading("Cantidad IPs Usables", text="Cantidad IPs Usables", anchor=tk.CENTER)

    # Insertar los resultados en el treeview
    for resultado in resultados:
        tree.insert("", tk.END, values=resultado)

    # Empaquetar el treeview
    tree.pack(expand=tk.YES, fill=tk.BOTH)


