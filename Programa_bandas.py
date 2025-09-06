import tkinter as tk

class Participante:
    def  __init__(self,nombre,institucion):
        self.nombre=nombre
        self.institucion=institucion

    def mostrar_info(self):
        return f"{self.nombre} — {self.institucion}"

class Banda(Participante):
    Lista_Categorias=["Primaria", "Basico", "Diversificado"]
    Lista_Criterios=["Ritmo", "Uniformidad", "Coreografia", "Alineacion", "Puntualidad"]

    def __init__(self,nombre,institucion,categoria):
        super().__init__(nombre,institucion)
        self._categoria=None
        self.puntos={}
        self.set_categoria(categoria)

    def set_categoria(self,categoria):
        cate = categoria
        if cate in Banda.Lista_Categorias:
            self._categoria = cate
            print("Categoria Valida")
        else:
            print("Categoria Invalida")




class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
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
        ventana_inscribir.title("Inscribir Bandaaaa")
        ventana_inscribir.geometry("400x250")

        tk.Label(ventana_inscribir, text="Nombre de la Banda:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_inscribir)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_inscribir, text="Institucion:").pack(pady=5)
        entrada_colegio = tk.Entry(ventana_inscribir)
        entrada_colegio.pack(pady=5)

        tk.Label(ventana_inscribir, text="Categoria:").pack(pady=5)
        entrada_categoria = tk.Entry(ventana_inscribir)
        entrada_categoria.pack(pady=5)



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
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()