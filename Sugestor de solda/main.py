import tkinter as tk
from tkinter import ttk

#Diccionario de material
REGRAS_MATERIAIS ={
    "Aço Carbono": (30, 40),
    "Aço Inox": (25, 35),
    "Aluminio": (40,50)
}

def calcular_amperagem():
    try:
        espessura = float(entry_espessura.get())
        material = combo_material.get()
        fator_min, fator_max = REGRAS_MATERIAIS[material]
        
        # Regra de negócio simpl.es: estimativa base de ~30 a 40 Amperes por milímetro de espessura.
        amperagem_min = espessura * fator_min
        amperagem_max = espessura * fator_max
        
        label_resultado.config(
            text=f"Amperagem Sugerida: {amperagem_min:.0f}A - {amperagem_max:.0f}A ({material})",
            foreground="green"
        )
    except ValueError:
        label_resultado.config(
            text="Por favor, insira um valor numérico válido.",
            foreground="red"
        )

# Configuração da Janela Principal
app = tk.Tk()
app.title("Sugestor de Parâmetros de Soldagem")
app.geometry("540x540")
app.resizable(False, False)

# Componentes da Interface
lbl_titulo = ttk.Label(app, text="Calculadora de Amperagem", font=("Helvetica", 14, "bold"))
lbl_titulo.pack(pady=2)

lbl_material = ttk.Label(app, text="Selecione o Material:")
lbl_material.pack(pady=2)

combo_material = ttk.Combobox(app, values=list(REGRAS_MATERIAIS.keys()), state="readonly")
combo_material.set("Aço Carbono")
combo_material.pack(pady=20)

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