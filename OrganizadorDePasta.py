# projeto para organizar os arquivos de um computador em uma pasta

# biblioteca para mexer com pastas e arquivos
import os
#abrir popup para o usuário selecionar uma determinada pasta
from tkinter.filedialog import askdirectory

caminho = askdirectory(title = 'Selecione uma pasta para organizar os arquivos por extensão')
#print(caminho)

#criar lista de arquivos que estão dentro desse caminho
lista_arquivos = os.listdir(caminho)
#print(lista_arquivos)

# criar dicionário para criar as pastas nas chaves e os tipos de arquivos nos valores
locais = {
    'imagens' : ['.png', 'jpg'],
    'planilhas' : ['.xlsx', '.csv'],
    'pdfs' : ['.pdf', '.pug'],
    'logs' : ['.log'],
    'midia' : ['.mp3', '.mp4'],
    'compactados' : ['.rar', '.zip'],
    'outros' : ['.svg'],
    'python' : ['.ipynb','.py'],
    'programas' : ['.exe', '.msi', '.jar'],
    'web' : ['.html']
}

for arquivo in lista_arquivos:
    #usar a variavel splitext pra splitar o nome do arquivo entre nome e extensão
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
   
    for pasta in locais:
     #print(pasta) --> pra checar o que a variavel pasta esta guardando
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):    # --> se a pasta não existir
                os.mkdir(f"{caminho}/{pasta}")  # --> criar a pasta
            os.rename (f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")   # --> pega os arquivos da pasta original e manda para a pasta desejada
            