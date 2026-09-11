import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Diccionario de material
REGRAS_MATERIAIS = {
    "Aço Carbono": {
        "TIG": {
            "Plana": (30, 40),
            "Vertical": (25, 35),
            "Sobre-Cabeça": (25, 30)
        },
        "MIG": {
            "Plana": (40, 50),
            "Vertical": (35, 45),
            "Sobre-Cabeça": (30, 40)
        },
        
    },
    "Aço Inox": {
        "TIG": {
            "Plana": (25, 35),
            "Vertical": (20, 30),
            "Sobre-Cabeça": (20, 25)
        },
        "MIG": {
            "Plana": (35, 45),
            "Vertical": (30, 40),
            "Sobre-Cabeça": (25, 35)
        }
    },
    "Alumínio": {
        "TIG": {
            "Plana": (40, 55),
            "Vertical": (35, 45),
            "Sobre-Cabeça": (35, 40)
        },
        "MIG": {
            "Plana": (50, 65),
            "Vertical": (45, 55),
            "Sobre-Cabeça": (40, 50)
        }
    }
}

def calcular_amperagem():
    try:
        espessura = float(entry_espessura.get())
        if espessura > 0:
                material = combo_material.get()
                processo = combo_processo.get()
                posição = combo_posições.get()
                fator_min, fator_max = REGRAS_MATERIAIS[material][processo][posição]
        
        # Regra de negócio simpl.es: estimativa base de ~30 a 40 Amperes por milímetro de espessura.
                amperagem_min = espessura * fator_min
                amperagem_max = espessura * fator_max

                label_resultado.config(
                text=f"Amperagem Sugerida: {amperagem_min:.0f}A - {amperagem_max:.0f}A ({material})",
                foreground="green"
                )
        else:
             messagebox.showerror("Erro de entrada, Por favor digitar espessura valida.")
                
    except ValueError:
        label_resultado.config(
            text="Por favor, insira um valor numérico válido.",
            foreground="red"
        )

    except KeyError:
         label_resultado.config(
              text="Por favor, insira um processo de soldagem",
              foreground="red"
            )


# Configuração da Janela Principal
app = tk.Tk()
app.title("Sugestor de Parâmetros de Soldagem")
app.geometry("400x320")
app.resizable(False, False)

# Componentes da Interface
lbl_titulo = ttk.Label(app, text="Calculadora de Amperagem", font=("Helvetica", 14, "bold"))
lbl_titulo.pack(pady=2)

lbl_material = ttk.Label(app, text="Selecione o Material:")
lbl_material.pack(pady=2)

combo_material = ttk.Combobox(app, values=list(REGRAS_MATERIAIS.keys()), state="readonly")
combo_material.set("Aço Carbono")
combo_material.pack(pady=2)

lbl_posições = ttk.Label(app, text="Selecione uma posição de Soldagem")
lbl_posições.pack(pady=2)
combo_posições = ttk.Combobox(app, values=("Plana", "Vertical", "Sobre-Cabeça"), state="readonly")
combo_posições.pack(pady=2)

lbl_processo = ttk.Label(app, text="Selecione o processo de Soldagem:")
lbl_processo.pack(pady=2)

combo_processo = ttk.Combobox(app, values=list(REGRAS_MATERIAIS["Aço Carbono"]), state="readonly" )
combo_processo.pack(pady=2)

lbl_instrucao = ttk.Label(app, text="Espessura da Chapa (mm):")
lbl_instrucao.pack(pady=5)

entry_espessura = ttk.Entry(app)
entry_espessura.pack(pady=5)

btn_calcular = ttk.Button(app, text="Calcular", command=calcular_amperagem)
btn_calcular.pack(pady=10)

label_resultado = ttk.Label(app, text="", font=("Helvetica", 10, "bold"))
label_resultado.pack(pady=10)

# Execução da Aplicação
if __name__ == "__main__":
    app.mainloop()