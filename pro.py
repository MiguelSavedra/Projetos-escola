k, x, campeão, mlm, maior, menor, media, y, z, n, b, c, d = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
a = str(input('Deseja começar o programa? s/n: '))
while a!= 'n' and a!= 's':
    a = str(input('Digitado errado, faça novamente: '))
while True:
  if a == 'n': 
    print('Fim do programa.')          
    break
  elif a == 's':
    x = str(input('Nome do atleta: '))
    y = float(input('Distância do 1º salto: '))
    while y < 0:
        y = float(input('Número não válido, digite a distância do 1º salto: '))
    z = float(input('Distância do 2º salto: '))
    while z < 0:
        z = float(input('Número não válido, digite a distância do 2º salto: '))
    b = float(input('Distância do 3º salto: '))
    while b < 0:
        b = float(input('Número não válido, digite a distância do 3º salto: '))
    c = float(input('Distância do 4º salto: '))
    while c < 0:
        c = float(input('Número não válido, digite a distância do 4º salto: '))
    d = float(input('Distância do 5º salto: '))
    while d < 0:
        d = float(input('Número não válido, digite a distância do 5º salto: '))   
    maior = y
    if maior < z:
        maior = z
    if maior < b:
        maior = b
    if maior < c:
        maior = c
    if maior < d:
        maior = d    
    print('O maior salto é: ', maior) 
    menor = y
    if menor > z:
        menor = z
    if menor > b:
        menor = b
    if menor > c:
        menor = c
    if menor > d:
        menor = d    
    print('O menor salto é: ', menor )
    media = (y + z + b + c + d - maior - menor) / 3                                         
    print('A média dos demais saltos é: ', media)
    print('Resultado final:', x, ':', media)
    if mlm <= media:
        mlm = media
        campeão = x              
    k = str(input('Deseja continuar o programa? s/n '))
    a = k
    if k == 'n':
        campeão = campeão.upper() 
        print('O atleta campeão é: ', campeão)
    if k!= 'n' and k!= 's':
        k = str(input('Digitado errado, faça novamente: '))
        a = k