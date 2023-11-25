import tkinter as tk
import vlsm
import subnetting
#ventana vlsm
def abrir_ventana_vlsm():
    ventana_vlsm = tk.Toplevel(ventana)
    ventana_vlsm.title("VLSM - Entrada")
    ventana_vlsm.state('zoomed')  # Maximizar la nueva ventana

    # Función para manejar la configuración de VLSM
    def calcular_vlsm():
        ip = entry_ip.get()
        prefijo = entry_prefijo.get()
        hosts = entry_hosts.get()
        vlsm.mostrar_resultados(ip, prefijo, hosts)

        

    # Crear etiquetas y entradas en la nueva ventana
    label_ip = tk.Label(ventana_vlsm, text="IP:")
    label_prefijo = tk.Label(ventana_vlsm, text="Prefijo:")
    label_hosts = tk.Label(ventana_vlsm, text="Ingrese los host separados por coma:")
    
    entry_ip = tk.Entry(ventana_vlsm)
    entry_prefijo = tk.Entry(ventana_vlsm)
    entry_hosts = tk.Entry(ventana_vlsm)

    # Crear botón para configurar VLSM
    btn_configurar = tk.Button(ventana_vlsm, text="Calcular", command=calcular_vlsm)

    # Ubicar elementos usando place
    label_ip.place(x=50, y=50)
    entry_ip.place(x=200, y=50)
    label_prefijo.place(x=50, y=100)
    entry_prefijo.place(x=200, y=100)
    label_hosts.place(x=50, y=150)
    entry_hosts.place(x=250, y=150)
    btn_configurar.place(x=200, y=200)


#ventana subnetting
def abrir_ventana_subnetting():
    ventana_subnetting = tk.Toplevel(ventana)
    ventana_subnetting.title("subnetting- Entrada")
    ventana_subnetting.state('zoomed')  # Maximizar la nueva ventana

    # Función para manejar la configuración de subnetting
    def calcular_subnetting():
        ip = entry_ip.get()
        prefijo = entry_prefijo.get()
        hosts = entry_hosts.get()
        subnetting.mostrar_resultados_subnetting(ip, prefijo, hosts)

        

    # Crear etiquetas y entradas en la nueva ventana
    label_ip = tk.Label(ventana_subnetting, text="IP:")
    label_prefijo = tk.Label(ventana_subnetting, text="Prefijo:")
    label_hosts = tk.Label(ventana_subnetting, text="Ingrese los host separados por coma:")
    
    entry_ip = tk.Entry(ventana_subnetting)
    entry_prefijo = tk.Entry(ventana_subnetting)
    entry_hosts = tk.Entry(ventana_subnetting)

    # Crear botón para configurar subnetting
    btn_configurar = tk.Button(ventana_subnetting, text="Calcular", command=calcular_subnetting)

    # Ubicar elementos usando place
    label_ip.place(x=50, y=50)
    entry_ip.place(x=200, y=50)
    label_prefijo.place(x=50, y=100)
    entry_prefijo.place(x=200, y=100)
    label_hosts.place(x=50, y=150)
    entry_hosts.place(x=250, y=150)
    btn_configurar.place(x=200, y=200)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Selección de Opción")
ventana.state('zoomed')

# Crear botón para abrir la ventana de VLSM
btn_vlsm = tk.Button(ventana, text="VLSM", command=abrir_ventana_vlsm, height=5, width=20)
btn_subnetting = tk.Button(ventana, text="Subnetting", command=abrir_ventana_subnetting, height=5, width=20)

# Cambiar el color de fondo de la ventana
ventana.configure(background="#15191A")

# Ubicar botones usando place
btn_vlsm.place(relx=0.5, rely=0.4, anchor="center")
btn_subnetting.place(relx=0.5, rely=0.6, anchor="center")

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
