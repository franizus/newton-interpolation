import numpy as np
#import matplotlib.pyplot as plt

def coef(x, y, n):
    fdd = np.zeros((n, n))
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])
    coefficients = np.zeros(n)
    for i in range(0, n):
        coefficients[i] = fdd[0][i]
    return coefficients

def eval(fdd, x, xi, n):
    xterm = 1
    yint = np.zeros(n)
    yint[0] = fdd[0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[order] * xterm
        yint[order] = yint2
    return yint[n-1]

def error(x, fx, xi):
    val = 1
    for valx in x:
        val = val * (xi - valx)
    val = val * fx
    return val

def ff(xval, coeff, x):
    values = []
    for i in range(len(xval)):
        aux = 0
        for j in range(len(coeff)):
            val = 1
            for k in range(j):
                val = val * (xval[i] - x[k])
            aux = aux + (coeff[j] * val)
        values.append(aux)
    return values

def fs(coeff, x):
    str_func = ''
    for j in range(len(coeff)):
        if j > 0:
            if coeff[j] >= 0:
                str_func += ' + ' + str(coeff[j])
            else:
                str_func += ' - ' + str(abs(coeff[j]))
        else:
            str_func += str(coeff[j])
        for k in range(j):
            if x[k] >= 0:
                str_func += '(x' + ' - ' + str(x[k]) + ')'
            else:
                str_func += '(x' + ' + ' + str(abs(x[k])) + ')'
    return str_func


n = int(input('Ingrese el grado del polinomio: ')) + 1
print('\nIngrese las coordenadas x,y de los puntos a analizar:\nEjemplo: x1:y1 > 3.5:2.6')
x = []
y = []
for i in range(n):
    aux = input('x' + str(i) + ':y' + str(i) + ' > ').split(':')
    x.append(float(aux[0]))
    y.append(float(aux[1]))

#x = [1, 4, 6, 5]
#y = [0, 1.386294, 1.791759, 1.609438]
xi = float(input('\nIngrese el valor a evaluar: '))

coefficients = coef(x, y, n)
yval = eval(coefficients, x, xi, n)
err = error(x, coefficients[n-1], xi)

print('\nf(x) = ' + fs(coefficients, x))
print('\nf(' + str(xi) + ') = ' + str(yval))
print('\nError = ' + str(err))

'''xt = np.arange(min(x), max(x), 0.1)
yt = ff(xt, coefficients, x)
plt.plot(xt, yt)
plt.plot(xi, yval, 'ro')
plt.axis([min(x), max(x), min(y), max(y)])
plt.show()'''
