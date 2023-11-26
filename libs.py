import tkinter as tk
from tkinter import filedialog
import hashlib
import tkinter.scrolledtext as scrolledtext
import pyperclip
import os
import datetime
from moviepy.editor import VideoFileClip
from pydub import AudioSegment


def janela_hash():
    def calcular_hash(nome_arquivo, algoritmo='sha256'):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                conteudo = arquivo.read()
                hash_obj = hashlib.new(algoritmo)
                hash_obj.update(conteudo)
                hash_digest = hash_obj.hexdigest()
                return hash_digest
        except FileNotFoundError:
            return None

    # Função para calcular hashes para vários arquivos
    def calcular_hashes_para_varios_arquivos():
        lista_de_arquivos = filedialog.askopenfilenames(title="Selecionar arquivos")
        for nome_arquivo in lista_de_arquivos:

            hash = calcular_hash(nome_arquivo)
            if hash:

                #Variaveis para obter os metadados dos arquivos
                get_name = os.path.basename(nome_arquivo)
                get_size = os.path.getsize(nome_arquivo)
                get_lastmodified = os.path.getmtime(nome_arquivo)
                get_lastmodified = datetime.datetime.fromtimestamp(get_lastmodified)
                get_lastmodified = get_lastmodified.strftime("%Y-%m-%d %H:%M:%S")

                extensoes_audio = ['mp3', 'wav', 'flac', 'aac', 'm4a', 'ogg', 'wma', 'alac', 'aiff', 'pcm', 'au', 'mid', 'midi', 'mp2', 
                                   'mpa', 'mpc', 'ape', 'mac', 'ra', 'rm', 'sln', 'tta', 'aac', 'ac3', 'dts', 'eac3', 'opus', 'pcm', 'wv']
                
                extensoe_video = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'ogg', 'mpeg', 'mpg', '3gp', 'm4v', 'vob', 'ogv', 'ts', 'mts', 'm2ts', 'asf', '.264']
                #verificar se o arquivo é um vídeo
                if nome_arquivo.lower().endswith(tuple(extensoe_video)):
                    clip = VideoFileClip(nome_arquivo)
                    duracao_segundos = clip.duration
                    duracao_minutos = duracao_segundos / 60

                    resultado_text.config(state=tk.NORMAL)
                    resultado_text.insert(tk.END, f'Nome do arquivo: {get_name}, Tamanho: {get_size/(1024):.0f} KB, Modificado em: {get_lastmodified}, Duração: {duracao_segundos:.2f} segundos ({duracao_minutos:.2f} minutos) e Hash (SHA 256) {hash.upper()}\n')
                    resultado_text.config(state=tk.DISABLED)


                #verificar se o arquvio é um áudio
                elif nome_arquivo.lower().endswith(tuple(extensoes_audio)):
                    audio = AudioSegment.from_file(nome_arquivo)
                    duracao_segundos = len(audio) / 1000  # convertendo de milissegundos para segundos
                    duracao_minutos = duracao_segundos / 60

                    resultado_text.config(state=tk.NORMAL)
                    resultado_text.insert(tk.END, f'Nome do arquivo: {get_name}, Tamanho: {get_size/(1024):.0f} KB, Modificado em: {get_lastmodified}, Duração: {duracao_segundos:.2f} segundos ({duracao_minutos:.2f} minutos) e Hash (SHA 256) {hash.upper()}\n')
                    resultado_text.config(state=tk.DISABLED)
                
                #Se for arquivo ou foto, mostrar o arquivo
                else:
                    resultado_text.config(state=tk.NORMAL)
                    resultado_text.insert(tk.END, f'Nome do arquivo: {get_name}, Tamanho: {get_size/(1024):.0f} KB, Modificado em: {get_lastmodified} e Hash (SHA 256) {hash.upper()}\n')
                    resultado_text.config(state=tk.DISABLED)
                


    # Função para copiar todos os hashes para a área de transferência
    def copiar_hashes():
        texto = resultado_text.get(1.0, tk.END)
        pyperclip.copy(texto)

    # Função para apagar todos os hashes da área de texto
    def apagar_hashes():
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.config(state=tk.DISABLED)

    #função para obter a data da última modificação
    


    # Configuração da janela
    global janela
    janela = tk.Tk()
    janela.title("Calculadora de Hash")
    janela.geometry("400x540")
    

    # Botão para calcular hashes
    calcular_button = tk.Button(janela, text="Calcular Hash para Arquivos", command=calcular_hashes_para_varios_arquivos)
    calcular_button.pack(pady=10)

    # Área de texto para exibir resultados
    resultado_text = scrolledtext.ScrolledText(janela, wrap=tk.WORD, state=tk.DISABLED)
    resultado_text.pack(fill=tk.BOTH, expand=True)

    # Botão para copiar todos os hashes
    copiar_button = tk.Button(janela, text="Copiar Todos os Hashes", command=copiar_hashes)
    copiar_button.pack(pady=10)

    # Botão para apagar todos os hashes
    apagar_button = tk.Button(janela, text="Apagar Todos os Hashes", command=apagar_hashes)
    apagar_button.pack(pady=10)
    # protocolo para quando fechar a janela, conseguir abrir outra
    janela.protocol("WM_DELETE_WINDOW", fechar_janela_hash)





# parametros par a fechar a janela corretamente
janela_hash_aberta = False


# Função para abrir a janela de hash
def abrir_janela_hash():
    global janela_hash_aberta

    # Verificar se a janela já está aberta e não deixar abrir novamente
    if not janela_hash_aberta:
        janela_hash()
        janela_hash_aberta = True
# Função para fechar a janela de hash
def fechar_janela_hash():
    global janela_hash_aberta
    janela_hash_aberta = False
    janela.destroy()
    
if __name__ == "__main__":
    abrir_janela_hash()

