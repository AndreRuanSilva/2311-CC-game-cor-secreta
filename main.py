import random
pontos_pc = 0
pontos_eu = 0
while(True):
  cor_secreta = random.choice(['R', 'G','B'])
  palpite = input("adivinhe a cor (R, G, B): ").upper()
  if palpite not in ['R','G', 'B']:
    print("entrada invalida, escolha R, G e B")
  elif palpite == cor_secreta:
    print("Parabens! Voce acertou")
    pontos_eu = pontos_eu + 1
  else:
    print("errrou")
    pontos_pc = pontos_pc + 1
  print("a cor secreta era", cor_secreta)
  print(f'VOCE:{pontos_eu} X PC:{pontos_pc}')
  