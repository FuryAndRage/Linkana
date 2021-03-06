import requests, os, sys, time


if sys.platform == 'linux':
    clear = lambda: os.system('clear')
if sys.platform == 'windows':
    clear = lambda: os.system('cls')


class LinkanaMain:
    def __init__(self, arquivo,imagem,servidor,entrada):
        self.servidor = servidor
        self.entrada = entrada
        self.arquivo = arquivo
        self.imagem = imagem
        self.link = ''
        self.contador = 0

    def video_js_py(self):
        self.link = ''
        self.contador=0
        with open (f'VideoJs_{self.arquivo}','w') as file:
            with open(f'{self.arquivo}','r+') as arq:
                leu = arq.readlines()
            for item in leu:
                if 'http' in item:
                    self.link += "{sources: [{src:'url' ,type: 'video/mp4'}],poster: 'image'},".replace('url', item.strip()).replace('image', self.imagem)
            file.write(self.link)
        clear()
        print('File was created successfully')
        time.sleep(2)
            
                
    def captura_link(self):
        self.contador = 0
        with open (f'LINK_{self.arquivo}', 'w') as file:
            with open(f'{self.arquivo}', 'r+') as arq:
                ler_arq = arq.readlines()
            for item in ler_arq:
                self.contador +=1
                if not '#' in item:
                    if 'http' in item:
                        self.link += item.strip() + '\n'
            file.write(self.link)
            print(f'{self.contador} urls')
        clear()
        print('File was created successfully')
        time.sleep(2)

        
    def download_link(self):
        self.contador=0
        with open(f'{self.arquivo}','r') as file:
            lines = file.readlines()
            for item in lines:
                with open(f'file_{self.contador}.mp4','wb') as arq: 
                    print(f'Downloading file_{self.contador}')
                    req = requests.get(item.strip())
                    size = int(req.headers['content-length']) /(1000**2)
                    print(req.status_code)
                    print(req.headers['content-type'])
                    print(req.encoding)
                    arq.write(req.content)
                    print(f'file_{self.contador}.mp4 was saved')
                    print(f'with {size}Mb')
                    self.contador +=1
                    print('')
                    print('')
                    print('')

    def captura_link_valido(self):
        self.contador = 0
        self.link = ''
        with open (f'VALID_{self.arquivo}', 'w+') as file:
            with open(f'{self.arquivo}', 'r+') as arq:
                ler_arq = arq.readlines()
            for item in ler_arq:
                try:
                    url = requests.head(item.strip())
                    print(url.status_code)
                    if url.status_code < 400:
                        self.link +=item.strip() + '\n'
                    
                except:
                    print('This server does not work')


            file.write(self.link)
        clear()
        print('File was created successfully')
        time.sleep(2)
                            
    def video_js_py_folder(self):
        self.link = ''
        for raiz, pastas, arquivos in os.walk(self.entrada):
            with open('lista.txt', 'w+') as file:
                for arquivo in arquivos:
                    self.link += "{sources: [{src:'url' ,type: 'video/mp4'}],poster: 'image'},".replace('url', self.servidor+arquivo).replace('image', self.imagem)
                    print(arquivo)
                            
                file.write(self.link)  

        clear()
        print('File was created successfully')
        time.sleep(2)


while True:
    print('###########################################################################')
    print('#                                                                         #')
    print('#                                                                         #')
    print('#                                                                         #')
    print('#  .____    .___ _______   ____  __.  _____    _______      _____         #')    
    print('#  |    |   |   |\\      \\ |    |/ _| /  _  \\   \\      \\    /  _  \\        #')
    print('#  |    |   |   |/   |   \\|      <  /  /_\\  \\  /   |   \\  /  /_\\  \\       #')
    print("#  |    |___|   /    |    \\    |  \\/    |    \\/    |    \\/    |    \"      #")
    print('#  |_______ \\___\\____|__  /____|__ \\____|__  /\\____|__  /\\____|__  /      #')
    print('#          \\/           \\/        \\/       \\/         \\/         \\/       #')
    print('#                                                                         #')
    print('#                                                                         #')
    print('#                                                                         #')
    print('###########################################################################')
    print('############################### OPTIONS ###################################')
    print('###########################################################################')
    print('# 1) GET LINKS ************* New file with link list from a .M3U or .M3U8 #')
    print('# 2) GET VALID LINKS ********* New list with valid links from a link list #')
    print('# 3) DOWNLOAD ********************* Download Files from a valid link list #')
    print('# 4) VIDEOJSPY ******************Generate a playlist for VideoJs Playlist #')
    print('# 5) VIDEOJSPY v2 *** Playlist for VideoJs Playlist from files on folder  #')
    print('# 6) *************************** EXIT *********************************** #')
    print('###########################################################################')
    choose_input = input('Choose a option: \n')
    
    if choose_input == '1':
        arquivo = input('Choose your file: \n')
        imagem = ''
        end_server = ''
        pasta_entrada = ''
        file_get = LinkanaMain(arquivo, imagem,end_server, pasta_entrada)
        file_get.captura_link()
        clear()

    if choose_input == '2':
        arquivo = input('Choose your file: \n')
        imagem = ''
        end_server = ''
        pasta_entrada = ''
        file_get = LinkanaMain(arquivo, imagem,end_server, pasta_entrada)
        file_get.captura_link_valido()
        clear()

    if choose_input == '3':
        arquivo = input('Choose your file: \n')
        imagem = ''
        end_server = ''
        pasta_entrada = ''
        file_get = LinkanaMain(arquivo, imagem,end_server, pasta_entrada)
        clear()
        file_get.download_link()

    if choose_input == '4':
        arquivo = input('Choose your file: \n')
        imagem = input('Choose the image file or url to use: \n')
        end_server = ''
        pasta_entrada = ''
        file_get = LinkanaMain(arquivo, imagem,end_server, pasta_entrada)
        file_get.video_js_py()
        clear()
    if choose_input == '5':
        arquivo = ''
        imagem = input('Choose the image file or url to use: \n')
        end_server = input('Url of your server and folder: \n')
        pasta_entrada = input('Path where are your files to create a lista: \n')
        file_get = LinkanaMain(arquivo, imagem,end_server, pasta_entrada)
        file_get.video_js_py_folder()
    if choose_input == '6':
        break

    else:
        print('Choose a valid option')

    
        
             





