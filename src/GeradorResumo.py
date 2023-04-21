import wikipedia
from fpdf import FPDF


class GeradorResumo:
    def __init__(self, tema):
        self.tema = tema
        self.resumo = None

    def pesquisar_wikipedia(self):
        wikipedia.set_lang('pt')
        try:
            pagina = wikipedia.page(self.tema)
            self.resumo = pagina.summary
        except wikipedia.exceptions.DisambiguationError as err:
            print('por favor, seja mais específico')
        except wikipedia.exceptions.PageError as err:
            print('página não encontrada')


    def gerar_pdf(self):
        if self.resumo is None:
            pass
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=12)
            pdf.cell(0, 10, txt=self.tema, align='C')
            pdf.ln()
            pdf.multi_cell(180, 10, txt=self.resumo, align='J')
            pdf.output(f'resumo_{self.tema}.pdf')