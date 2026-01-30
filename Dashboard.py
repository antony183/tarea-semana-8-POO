import os
import subprocess

class Dashboard:
    """
    Clase Dashboard
    Permite organizar unidades, ejecutar scripts y gestionar tareas personales
    """

    def __init__(self):
        # Ruta base del proyecto
        self.ruta_base = os.path.dirname(__file__)
        self.archivo_tareas = os.path.join(self.ruta_base, "tareas.txt")

        # Diccionario de unidades
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    # ------------------- FUNCIONES DE SCRIPTS -------------------

    def mostrar_codigo(self, ruta_script):
        """Muestra el código fuente de un script"""
        try:
            with open(ruta_script, 'r') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
                print(codigo)
                return codigo
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def ejecutar_codigo(self, ruta_script):
        """Ejecuta un script Python"""
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Linux / Mac
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Error al ejecutar el código: {e}")

    # ------------------- MENÚS -------------------

    def mostrar_menu_principal(self):
        """Menú principal del Dashboard"""
        while True:
            print("\n===== DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS =====")
            for key, value in self.unidades.items():
                print(f"{key} - {value}")
            print("3 - Gestión de tareas")
            print("0 - Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '0':
                print("Saliendo del sistema...")
                break
            elif opcion in self.unidades:
                self.mostrar_sub_menu(os.path.join(self.ruta_base, self.unidades[opcion]))
            elif opcion == '3':
                self.menu_tareas()
            else:
                print("Opción no válida.")

    def mostrar_sub_menu(self, ruta_unidad):
        """Submenú de carpetas"""
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\n--- Submenú de carpetas ---")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Volver")

            opcion = input("Seleccione una carpeta: ")

            if opcion == '0':
                break
            try:
                index = int(opcion) - 1
                if 0 <= index < len(sub_carpetas):
                    self.mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[index]))
                else:
                    print("Opción incorrecta.")
            except ValueError:
                print("Debe ingresar un número.")

    def mostrar_scripts(self, ruta_sub_carpeta):
        """Muestra y ejecuta scripts Python"""
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

        while True:
            print("\n--- Scripts disponibles ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Volver")

            opcion = input("Seleccione un script: ")

            if opcion == '0':
                break
            try:
                index = int(opcion) - 1
                if 0 <= index < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[index])
                    self.mostrar_codigo(ruta_script)
                    ejecutar = input("¿Desea ejecutar el script? (1: Sí / 0: No): ")
                    if ejecutar == '1':
                        self.ejecutar_codigo(ruta_script)
                else:
                    print("Opción incorrecta.")
            except ValueError:
                print("Debe ingresar un número.")

    # ------------------- GESTIÓN DE TAREAS -------------------

    def menu_tareas(self):
        """Menú para gestionar tareas"""
        while True:
            print("\n--- GESTIÓN DE TAREAS ---")
            print("1 - Agregar tarea")
            print("2 - Ver tareas")
            print("0 - Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_tarea()
            elif opcion == '2':
                self.ver_tareas()
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")

    def agregar_tarea(self):
        """Agrega una tarea al archivo"""
        tarea = input("Ingrese la descripción de la tarea: ")
        with open(self.archivo_tareas, 'a') as archivo:
            archivo.write(tarea + "\n")
        print("Tarea guardada correctamente.")

    def ver_tareas(self):
        """Muestra las tareas guardadas"""
        if not os.path.exists(self.archivo_tareas):
            print("No hay tareas registradas.")
            return

        print("\n--- LISTA DE TAREAS ---")
        with open(self.archivo_tareas, 'r') as archivo:
            for i, linea in enumerate(archivo, start=1):
                print(f"{i}. {linea.strip()}")

# ------------------- EJECUCIÓN -------------------

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mostrar_menu_principal()
