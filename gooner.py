class Goon:
    def __init__(self, 
                sanidade,
                frigidez,
                energia,
                goonadas,
                genero,
                religiao,
                waifu,
                furry,
                femboy,
                mago,
                virgem
                ):
        
        self.sanidade = sanidade
        self.frigidez = frigidez
        self.energia = energia
        self.goonadas = goonadas
        self.mulher = genero
        self.religiao = religiao
        self.waifu = waifu
        self.furry = furry
        self.femboy = femboy
        self.mago = mago
        self.virgem = virgem        

    def gozar(self):
        self.goonadas =+ 1
        self.sanidade = self.sanidade - 0.2 * self.sanidade


    def fapear(self):
        self.frigidez = self.frigidez - 20
        self.sanidade = self.sanidade - 20
        self.energia = self.energia - 5
    
    def exibir_status(self):
        print(f'Frigidez: {self.frigidez}\n',
              f'Sanidade: {self.sanidade}\n',
              f'Goonadas: {self.goonadas}\n')

        

