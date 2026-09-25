from gooner import Goon

gonner = Goon(100, 100, 1)


while gonner.sanidade != 0 :
     gonner.exibir_status()
     print('[F] para fapear')
     g = input()
     if g == 'f':
          gonner.fapear()
     else:
          print('Ação descabível')
          g = input()

     if gonner.energia < 0:
          gonner.gozar()