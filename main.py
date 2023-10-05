import numpy as np

# matriz_x = np.array([[2, 6, 3, 8, 6], [3, 0, 8, 4, 0], [1, 1, 2, 1, 6]])
# np.savetxt('matriz_x.txt', matriz_x)

# matriz_y = np.array([[9, 6, 3, 1, 7], [5, 3, 0, 7, 6], [2, 9, 0, 4, 7]])
# np.savetxt('matriz_y.txt', matriz_y)

print(' \n # Criar um array bidimensional com dados diferentes dos utilizados em sala;\n')
x = np.loadtxt('matriz_x.txt')

y = np.loadtxt('matriz_y.txt')

print(f'x:\n{x}')
print('\n')
print(f'y:\n{y}')


print('\n # Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis); \n ')

### soma
print("----------- SOMA ----------")
print(' \n ')

sum_x = x.sum()
print(f'a soma de x é: {sum_x}')

sum_y = y.sum()
print(f'a soma de y é: {sum_y}')

sum_x0 = x.sum(axis=0)
print(f'a soma das colunas de x é: {sum_x0}')

sum_y0 = y.sum(axis=0)
print(f'a soma das colunas de y é: {sum_y0}')

sum_x1 = x.sum(axis=1)
print(f'a soma das linhas de x é: {sum_x1}')

sum_y1 = y.sum(axis=1)
print(f'a soma das linhas de y é: {sum_y1}')

### média
print(' \n ')
print("----------- MÉDIA ----------")
print(' \n ')

mean_x = x.mean()
print(f'a média de x é: {mean_x}')

mean_y = y.mean()
print(f'a média de y é: {mean_y}')

mean_x0 = x.mean(axis=0)
print(f'a média das colunas de x é: {mean_x0}')

mean_y0 = y.mean(axis=0)
print(f'a média das colunas de y é: {mean_y0}')

mean_x1 = x.mean(axis=1)
print(f'a média das linhas de x é: {mean_x1}')

mean_y1 = y.mean(axis=1)
print(f'a média das linhas de y é: {mean_y1}')



print('\n # Obter a transposta da matriz e realizar uma operação com ela; \n ')

xT = np.transpose(x)
print(f'Matriz transposta de x é :\n {xT}')

print(' \n ')

yT = np.transpose(y)
print(f'Matriz transposta de y é :\n {yT}')

print(' \n ')

soma_xTyT = xT+yT
print(f'Soma de xT com Yt :\n {soma_xTyT} ')

print(' \n ')

produto_xTyT = xT*yT
print(f'Produto de xT com Yt :\n {produto_xTyT} ')



print('\n # Realizar um produto escalar entre duas matrizes ou de um array com uma matriz; \n ')

escalar_xy = x@yT #np.dot(x,y)

print(f'Produto escalar de x e YT (x@yT) é:\n {escalar_xy}')
print('\n')


z = np.random.randint(10, size=[1, 5])

w = np.random.randint(10, size=[1, 5])

wT = np.transpose(w)

print(f'z:\n{z}')
print('\n')

print(f'w:\n{w}')
print('\n')

print(f'wT:\n{wT}')
print('\n')

escalar_zw1 = z@wT
escalar_zw2 = np.dot(z,wT)

print(f'Produto escalar de z e wT (z@wT) é:\n {escalar_zw1}')
print('\n')
print(f'Produto escalar de z e wT (np.dot(z,wT)) é:\n {escalar_zw2}')
print('\n')




print('\n # Criar um filtro para a sua matriz \n ')
f_soma = [False, True, True]

xf = x[f_soma].sum()
yf = y[f_soma].sum()

print(f'A soma de x com o filtro f_soma é: \n {xf}')
print('\n')

print(f'A soma de y com o filtro f_soma é: \n {yf}')
print('\n')

x_2 = x[x%2==0]

print(f'Os números pares em x são : \n {x_2}')
print('\n')

y_m3 = y[y>3]

print(f'Os números maiores que 3 em ysão : \n {y_m3}')
print('\n')



print('\n # Realizar alguma operação aritmética (número com matriz, array com matriz, etc.); \n ')
x1 = x+1

print(f'x \n {x}')

print('\n')

print(f'x + 1 = x1 --> \n {x1}')

print('\n')

array = np.array([10, 20, 30])

yz = y * z

print(f'y \n {y}')

print('\n')

print(f'z \n {z}')

print('\n')

print(f'y * z = yz --> \n {yz}')





