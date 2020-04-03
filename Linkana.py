import requests


class ConverteJSCript:
    def __init__(self, arquivo,imagem):
        self.arquivo = arquivo
        self.imagem = imagem
        self.lido = ''
        self.link = ''
        self.contador = 0
    def grava_arquivo(self):
        self.contador=0
        with open (f'novo_{self.arquivo}.txt','w') as file:
            with open(f'{self.arquivo}','r+') as arq:
                leu = arq.readlines()
            for item in leu:
                if not '#EXTINF' or not 'EXTINF' in item:
                    if 'http' in item:
                        self.lido += "{sources: [{src:'aqui' ,type: 'video/mp4'}],poster: 'imagem'},".replace('aqui', item.strip()).replace('imagem', self.imagem)
            file.write(self.lido)

            
                
    def captura_link(self):
        self.contador = 0
        with open (f'links_{self.arquivo}.txt', 'w') as file:
            with open(f'{self.arquivo}', 'r+') as arq:
                ler_arq = arq.readlines()
            for item in ler_arq:
                self.contador +=1
                if not '#' in item:
                    if 'http' in item:
                        self.link += item.strip() + '\n'
            file.write(self.link)
            print(f'{self.contador} urls')


        
    def download_link(self):
        self.contador=0
        with open(f'{self.arquivo}','r') as file:
            arq = file.readlines()
            for item in arq:
                with open(f'arquivo_{contador}.mp4','wb') as arq:
                    req = requests.get(item.strip())
                    size = int(req.headers['content-length']) /(1000**2)
                    
                    print(req.status_code)
                    print(req.headers['content-type'])
                    print(req.encoding)
                    arq.write(req.content)
                    print(f'arquivo_{contador}.mp4 was saved')
                    print(f'with {size}Mb')
                    contador +=1

    def captura_link_valido(self):
        self.contador = 0
        
        with open (f'links_valido_{self.arquivo}', 'w') as file:
            with open(f'{self.arquivo}', 'r+') as arq:
                ler_arq = arq.readlines()
            for item in ler_arq:
                try:
                    url = requests.head(item.split())
                    print(url.status_code)
                    self.link +=item.strip()
                    print(url.status_code)
                except:
                    print('Server nao funciona')


            file.write(self.link)
                    
        

while True:
    print('####################### L I N K A N A ############################')
    print('#'*50)
    print('Choose a option')
    print('1) Get Only Links into a another File')
    print('2) Download Files from Link')
    print('3) Create a file with only valid link')
    print('4) Get Link to VideoJS PlayList Format')
    print('Press any other button to exit')
    print('#'*50)
    choose_input = input('Pick one of options')
    arquivo = input('Digite o nome do arquivo a ser aberto: \n')
    imagem = input('Digite a url da imagem a ser utilizada: \n')
    file_get = ConverteJSCript(arquivo, imagem)
    if choose_input == '1':
        file_get.captura_link()
    if choose_input == '2':
        file_get.download_link()
    if choose_input == '3':
        file_get.captura_link_valido()
    if choose_input == '4':
        file_get.grava_arquivo()
    else:
         False
    
        
             





