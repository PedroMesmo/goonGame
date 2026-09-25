class Goon:
    def __init__(self, 
                sanidade,
                energia,
                goonadas,
                genero,
                religiao,
                furry,
                femboy,
                mago,
                virgem
                ):
        
        self.sanidade = sanidade
        self.energia = energia
        self.goonadas = goonadas
        self.religiao = religiao
        self.furry = furry
        self.femboy = femboy
        self.mago = mago
        self.virgem = virgem
        self.mulher = genero
        

    def gozar(self):
        self.goonadas =+ 1
        self.sanidade = self.sanidade - 0.2 * self.sanidade

    def fapear(self):
        self.energia = self.energia - 20
    
    def exibir_status(self):
        print(f'Energia: {self.energia}\n',
              f'Sanidade: {self.sanidade}\n',
              f'Goonadas: {self.goonadas}\n')

