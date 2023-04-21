import tkinter as tk


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

        self.pdf_gerar_pdf = tk.Button(self.janela, text='GERAR PDF')
        self.pdf_gerar_pdf.place(relx=0.5, rely=0.8, anchor='center')