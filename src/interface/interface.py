import PySimpleGUI as sg
from google import google
import os
import traceback


class TelaPython:
    def __init__(self):
        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.
        layout = [
            [sg.Text(
                'Preencha os campos abaixos para fazer a pesquisa.\n Os campos que contenham * são obrigatóios.\n')],
            [sg.Text('*Palavras-Chaves (ex: covid-19)'),
             sg.InputText(key='palavrachave')],
            [sg.Text('Sites específicos (ex: g1.com.br)'),
             sg.InputText(key='sites')],
            [sg.Text('*Numero de páginas (ex: 2)'),
             sg.InputText(key='paginas')],
            [sg.Text('*Nome do arquivo (ex: resultado1))'),
             sg.InputText(key='arquivo')],
            [sg.Button('Fazer a pesquisa'), sg.Button('Cancelar')],
<<<<<<< HEAD
=======
            [sg.Output(size=(80, 10))],
>>>>>>> e55f841c6e8ba7948f41b78792c2f387e48603b8
        ]
        # Janela
        self.window = sg.Window('Google Search API', layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.window.Read()
            pesquisa = self.values['palavrachave']
            sites = self.values['sites']
            numeroPag = self.values['paginas']
            arquivo = self.values['arquivo']
<<<<<<< HEAD
            #print(f'Palavras chaves: {pesquisa}')
            #print(f'Sites: {sites}')
            #print(f'Páginas: {numeroPag}')
            #print(f'Arquivo: {arquivo}')
=======
            print(f'Palavras chaves: {pesquisa}')
            print(f'Sites: {sites}')
            print(f'Páginas: {numeroPag}')
            print(f'Arquivo: {arquivo}')
>>>>>>> e55f841c6e8ba7948f41b78792c2f387e48603b8

            return pesquisa, sites, numeroPag, arquivo

''' # Event Loop to process "events" and get the "values" of the inputs
        while True:
            self.event, self.values = window.read()
            if self.event in (None, 'Cancel'):   # if user closes window or clicks cancel
                break
            print(teste)
        window.close()

    '''
