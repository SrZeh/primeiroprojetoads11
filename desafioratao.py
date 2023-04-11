import random
num=random.randint(1,10)
num2=int(input('Escolha seu número de 1 a 10: '))
numx=[num2]
if num2==num:
    print('você acertou!')
else:
     print('está sem sorte!')
while num2 != num:
    num2=int(input('Escolha seu número de 1 a 10: '))
    numx.append(num2)
print('Você acertou! o numero era {}'.format(num))
print('você tentou todos esses números: {}'.format(numx))
