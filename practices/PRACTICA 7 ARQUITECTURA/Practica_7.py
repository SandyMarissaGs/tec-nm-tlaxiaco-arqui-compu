import tkinter as tk
from tkinter import messagebox


class AdministracionMemoriaApp:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Simulación de Administración de Memoria")
        self.root.geometry("600x400")  # Dimensiones de la ventana
        self.root.configure(bg="#f0f0f0")  # Color de fondo

        # Inicialización de variables y programa
        # Variables que simulan el espacio de memoria para el programa
        self.variables = [0, 0, 0]
        # Lista que contendrá las instrucciones del programa
        self.instrucciones = []
        # Diccionario que simula un programa en memoria
        self.programa = {
            0: "cargar 5,0",   # Cargar el valor 5 en la posición 0 de las variables
            1: "cargar 3,1",   # Cargar el valor 3 en la posición 1 de las variables
            2: "sumar 0,1,2",  # Sumar las posiciones 0 y 1, guardar en la posición 2
            3: "imprimir 2"    # Imprimir el valor en la posición 2
        }

        # Crear los componentes de la interfaz
        self.crear_componentes()

    def crear_componentes(self):
        """Crea los elementos de la interfaz gráfica."""
        # Título en la parte superior de la ventana
        titulo = tk.Label(self.root, text="Simulación de Administración de Memoria en la CPU",
                          bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), pady=10)
        titulo.pack(fill=tk.X)  # Expandir horizontalmente

        # Frame para contener los botones
        botones_frame = tk.Frame(self.root, bg="#f0f0f0")
        botones_frame.pack(pady=10)  # Separación vertical

        # Botón para cargar el programa en memoria
        btn_cargar_programa = tk.Button(botones_frame, text="Cargar Programa", command=self.cargar_programa,
                                        bg="#2196F3", fg="white", font=("Arial", 12))
        btn_cargar_programa.grid(row=0, column=0, padx=10)

        # Botón para ejecutar el programa
        btn_ejecutar = tk.Button(botones_frame, text="Ejecutar Programa", command=self.ejecutar_programa,
                                 bg="#FF5722", fg="white", font=("Arial", 12))
        btn_ejecutar.grid(row=0, column=1, padx=10)

        # Cuadro de texto donde se mostrarán las operaciones y resultados
        self.texto_resultado = tk.Text(self.root, height=15, width=70, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.texto_resultado.pack(pady=10)

        # Botón para cerrar la aplicación
        btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit,
                              bg="#9E9E9E", fg="white", font=("Arial", 12))
        btn_salir.pack(pady=10)

    def registrar_operacion(self, mensaje):
        """Registra y muestra un mensaje en el cuadro de texto."""
        self.texto_resultado.insert(tk.END, f"{mensaje}\n")  # Agregar mensaje al final
        self.texto_resultado.see(tk.END)  # Auto-scroll al final del cuadro de texto

    def cargar_programa(self):
        """Carga el programa en memoria y lo muestra en la interfaz."""
        self.instrucciones = list(self.programa.values())  # Convertir las instrucciones del diccionario en una lista
        self.registrar_operacion("Programa cargado en memoria:")
        for i, instruccion in enumerate(self.instrucciones):
            self.registrar_operacion(f"{i}: {instruccion}")  # Mostrar cada instrucción con su índice
        self.registrar_operacion("")  # Línea en blanco para separación

    def ejecutar_programa(self):
        """Ejecuta las instrucciones del programa paso a paso."""
        self.registrar_operacion("Iniciando ejecución del programa...")
        try:
            # Recorremos cada instrucción en la lista
            for instruccion in self.instrucciones:
                if not instruccion.strip():  # Ignorar instrucciones vacías
                    continue

                # Dividir la instrucción en operación y argumentos
                partes = instruccion.split()
                operacion = partes[0]  # Nombre de la operación (cargar, sumar, imprimir)
                argumentos = partes[1].split(",")  # Argumentos separados por coma

                # Ejecutar la operación correspondiente
                if operacion == "cargar":
                    # Cargar un valor en una variable
                    valor, destino = map(int, argumentos)  # Convertir argumentos a enteros
                    self.variables[destino] = valor  # Asignar valor a la posición destino
                    self.registrar_operacion(f"Cargado {valor} en Variable {destino}")

                elif operacion == "sumar":
                    # Sumar dos variables y guardar el resultado en otra
                    var1, var2, destino = map(int, argumentos)
                    self.variables[destino] = self.variables[var1] + self.variables[var2]
                    self.registrar_operacion(f"Sumado Variable {var1} y Variable {var2} en Variable {destino}")

                elif operacion == "imprimir":
                    # Imprimir el valor de una variable
                    origen = int(argumentos[0])  # Convertir argumento a entero
                    resultado = self.variables[origen]  # Obtener el valor de la variable
                    self.registrar_operacion(f"Variable {origen}: {resultado}")
                    # Mostrar el resultado en una ventana emergente
                    messagebox.showinfo("Resultado", f"El valor de la Variable {origen} es: {resultado}")

                else:
                    # Error si la operación no es reconocida
                    raise ValueError(f"Operación desconocida: {operacion}")
            
            # Finalizar ejecución y mostrar estado final de las variables
            self.registrar_operacion("\nEjecución completada.")
            self.registrar_operacion(f"Estado final de las variables: {self.variables}")
        except Exception as e:
            # Mostrar un mensaje de error si ocurre un problema durante la ejecución
            messagebox.showerror("Error", f"Error durante la ejecución: {e}")


# Crear la ventana principal e inicializar la aplicación
root = tk.Tk()
app = AdministracionMemoriaApp(root)
root.mainloop()


#INTEGRANTES DEL EQUIPO
#SANDY MARISSA GARCIA SANTIAGO.
#BLANCA ESTELA VALERIO RIVERO.