#  Exibir a tabuada do número cinco no intervalo de um a dez.

print('Tabuada do 5 com FOR')

num = 5

for i in range(5, 11, 1):
    r = num * i
    print(f'{num} X {i} = {r}')