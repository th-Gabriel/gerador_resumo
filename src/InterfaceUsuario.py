import tkinter as tk
from tkinter import messagebox
from GeradorResumo import GeradorResumo


class InterfaceUsuario():
    def __init__(self):
        self.janela = tk.Tk()

    
    def iniciar_janela(self):
        self.janela.title('GERADOR DE RESUMOS')
        self.janela.geometry('300x120')

        self.definir_widgets()
        self.janela.mainloop()

    
    def definir_widgets(self):
        label_tema = tk.Label(self.janela, text='TEMA')
        label_tema.place(relx=0.5, rely=0.2, anchor='center')

        self.input_box = tk.Entry(self.janela, width=40)
        self.input_box.place(relx=0.5, rely=0.4, anchor='center')

        self.pdf_gerar_pdf = tk.Button(self.janela, text='GERAR PDF', command=self.algoritmo)
        self.pdf_gerar_pdf.place(relx=0.5, rely=0.8, anchor='center')

    
    def algoritmo(self):
        tema_input = self.input_box.get().upper()
        
        self.gerador = GeradorResumo(tema=tema_input)
        self.gerador.pesquisar_wikipedia()
        if self.gerador.resumo is None:
            messagebox.showerror('Página não encontrada', 'Tente ser mais específico ou escolha outro tema')
        else:
            self.gerador.gerar_pdf()
            messagebox.showinfo('STATUS', 'Arquivo criado com sucesso!')