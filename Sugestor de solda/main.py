import tkinter as tk
from tkinter import ttk

def calcular_amperagem():
    try:
        espessura = float(entry_espessura.get())
        
        # Regra de negócio simpl.es: estimativa base de ~30 a 40 Amperes por milímetro de espessura.
        amperagem_min = espessura * 30
        amperagem_max = espessura * 40
        
        label_resultado.config(
            text=f"Amperagem Sugerida: {amperagem_min:.0f}A - {amperagem_max:.0f}A",
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
app.geometry("400x250")
app.resizable(False, False)

# Componentes da Interface
lbl_titulo = ttk.Label(app, text="Calculadora de Amperagem", font=("Helvetica", 14, "bold"))
lbl_titulo.pack(pady=10)

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