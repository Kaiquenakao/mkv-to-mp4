import PySimpleGUI as sg
import os
from moviepy.editor import *
from PySimpleGUI import DEFAULT_INPUT_TEXT_COLOR


def converte():
    sg.theme('Reddit')
    layout = [
        [sg.Input(default_text='Insira o arquivo MKV: '), sg.FileBrowse('Seleciona', key='-IN-')],
        [sg.Button('Converter', key='enviar')]
    ]
    return sg.Window('Converter MKV para MP4', layout, finalize=True)

janela = converte()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'enviar' and values['-IN-'] != "":

        # Selecionando o arquivo MKV e armazenando em uma variável (rename) o nome do arquivo
        video = values['-IN-'].split('/').pop()
        rename = video.split('.')[0]

        # Transformando o caminho url em uma lista e pegando o caminho menos o file
        dir = "/".join(values['-IN-'].split('/')[0:-1]) + "/"

        # Mudando o diretório sem contar com o arquivo
        os.chdir(dir)

        # Usando a biblioteca pymovie para selecionar o arquivo
        video = VideoFileClip(video)

        # Convertendo o vídeo para mp4
        video.write_videofile(rename + ".mp4")
        sg.popup("Vídeo convertido")