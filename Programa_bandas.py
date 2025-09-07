import tkinter as tk
from tkinter import messagebox, ttk
Lista_Categorias = ["Primaria", "Basico", "Diversificado"]
Lista_Criterios = ["Ritmo", "Uniformidad", "Coreografia", "Alineacion", "Puntualidad"]

class Banda:
    def  __init__(self,nombre,institucion,categoria):
        self.nombre=nombre
        self.institucion=institucion
        self.categoria=categoria
        self.puntajes={
            "ritmo": 0,
            "uniformidad": 0,
            "coreografia": 0,
            "alineacion": 0,
            "puntualidad": 0
        }



    def registar_puntajes(self,puntajes_ingresados):
        if set(puntajes_ingresados.keys())!= set(self.puntajes.keys()):
            return False,"Ingrese los datos completos"

        for criterio, valor in puntajes_ingresados.items():
            try:
               # numero=input("Ingres el valor")
                numero = int(valor)
            except:
                return False, f"El puntaje de {criterio} debe ser un número entero."
            if numero < 0 or numero> 10:
                return False, f"El puntaje de {criterio} debe estar entre 0 y 10."
            self.puntajes[criterio] = numero
        return True, "Puntajes registrados"

    def total(self):
        total=0
        for valor in self.puntajes.values():
            total=total+valor
        return  total

    """def promedio(self):
        suma=0
        contador=0
        for valor in self.puntajes.values():
            suma += valor
            contador += 1
            resultado=suma/contador
        return resultado if contador > 0 else 0"""

    def promedio(self):
        return self.total() / len(self.puntajes)

    def info(self):
        if any(self.puntajes.values()):
            print(f"Nombre: {self.nombre} | Institución: {self.institucion} | Categoría: {self.categoria} | Total: {self.total()} | Promedio: {round(self.promedio(), 2)}")
        else:
            print(f"Nombre: {self.nombre} | Institución: {self.institucion} | Categoría: {self.categoria} | Pendiente de evaluación")


class Concurso:
    def __init__(self):
        self.bandas = {}

    def _clave(self, nombre):
        return nombre

    def inscribir_banda(self, nombre, institucion, categoria):
        if not nombre or not institucion:
            return False,"Nombre e institución son obligatorios."

        clave = self._clave(nombre)
        if clave in self.bandas:
            return False, "Ya existe una banda con ese nombre."
        self.bandas[clave] = Banda(nombre, institucion, categoria)
        print("Se agrego con exito")
        return  True, "Banda inscrita"


    def registrar_evaluacion(self, nombre_banda, nuevos_puntajes):
        clave = self._clave(nombre_banda)
        if clave not in self.bandas:
            return False, "Banda no encontrada."
        return self.bandas[clave].registrar_puntajes(nuevos_puntajes)

    def listar_bandas(self):
        return list(self.bandas.values())

    def ranking(self):
        # Orden: total, ritmo, uniformidad, coreografia, alineacion, puntualidad (desc) y nombre (asc)
        def clave_orden(b):
            p = b.puntajes
            return (
                b.total(),
                p["ritmo"],
                p["uniformidad"],
                p["coreografia"],
                p["alineacion"],
                p["puntualidad"],
                b.nombre
            )

        return sorted(self.bandas.values(), key=clave_orden, reverse=True)


class ConcursoBandasApp:

    def __init__(self):
        self.concurso = Concurso()
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango 2025")
        self.ventana.geometry("500x300")
        self.ventana.configure(bg="grey")
        self.ventana.resizable(False, False)
        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")

        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x250")

        tk.Label(ventana_inscribir, text="Nombre de la Banda:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_inscribir)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_inscribir, text="Institucion:").pack(pady=5)
        entrada_colegio = tk.Entry(ventana_inscribir)
        entrada_colegio.pack(pady=5)

        tk.Label(ventana_inscribir, text="Categoria:").pack(pady=5)
        var_categoria = tk.StringVar(value=Lista_Categorias[0])
        tk.OptionMenu(ventana_inscribir, var_categoria, *Lista_Categorias).pack(pady=5)

        def guardar():
            var, mensaje = self.concurso.inscribir_banda(
                entrada_nombre.get(),
                entrada_colegio.get(),
                var_categoria.get()
            )
            if var:
                messagebox.showinfo("Éxito", mensaje)
                ventana_inscribir.destroy()
            else:
                messagebox.showwarning("Aviso", mensaje)

        tk.Button(ventana_inscribir, text="Guardar", command=guardar).pack(pady=12)



    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")

        ventana_evaluacion= tk.Toplevel(self.ventana)
        ventana_evaluacion.title("Registrar Calificaciones")
        ventana_evaluacion.geometry("400x250")

        tk.Label(ventana_evaluacion, text="Ritmo:").pack(pady=5)
        entrada_ritmo = tk.Entry(ventana_evaluacion)
        entrada_ritmo.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Uniformidad:").pack(pady=5)
        entrada_uniformidad = tk.Entry(ventana_evaluacion)
        entrada_uniformidad.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Coreografia:").pack(pady=5)
        entrada_coreografia = tk.Entry(ventana_evaluacion)
        entrada_coreografia.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Alineacion:").pack(pady=5)
        entrada_alineacion = tk.Entry(ventana_evaluacion)
        entrada_alineacion.pack(pady=5)

        tk.Label(ventana_evaluacion, text="Puntualidad:").pack(pady=5)
        entrada_puntualidad = tk.Entry(ventana_evaluacion)
        entrada_puntualidad.pack(pady=5)

    def listar_bandas(self):
        ventana_listar = tk.Toplevel(self.ventana)
        ventana_listar.title("Listado de Bandas")
        ventana_listar.geometry("400x250")

        bandas = self.concurso.listar_bandas()
        if not bandas:
            tk.Label(ventana_listar, text="No hay bandas registradas.").pack(pady=20)
            return

        columnas = ("Nombre", "Institución", "Categoría", "Total", "Promedio")
        tree = ttk.Treeview(ventana_listar, columns=columnas, show="headings", height=12)
        for c in columnas:
            tree.heading(c, text=c)
        tree.column("Nombre", width=160, anchor="center")
        tree.column("Institución", width=160, anchor="center")
        tree.column("Categoría", width=120, anchor="center")
        tree.column("Total", width=80, anchor="center")
        tree.column("Promedio", width=100, anchor="center")

        for b in bandas:
            hay_puntajes = any(b.puntajes.values())
            total = b.total() if hay_puntajes else "-"
            prom = f"{b.promedio()}" if hay_puntajes else "-"

            tree.insert("", "end", values=(b.nombre, b.institucion, b.categoria, total, prom))

        tree.pack(fill="both", expand=True, padx=10, pady=10)

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()