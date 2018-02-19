import numpy as np


def spline(x, y, n, xu, results):
    e = np.zeros(n)
    f = np.zeros(n)
    g = np.zeros(n)
    r = np.zeros(n)
    d2x = np.zeros(n)
    tridiag(x, y, n, e, f, g, r)
    decompose(e, f, g, n)
    substitute(e, f, g, r, n, d2x)
    interpol(x, y, n, d2x, xu, results)


def tridiag(x, y, n, e, f, g, r):
    f[1] = 2 * (x[2] - x[0])
    g[1] = (x[2] - x[1])
    r[1] = 6 / (x[2] - x[1]) * (y[2] - y[1])
    r[1] = r[1] + 6 / (x[1] - x[0]) * (y[0] - y[1])
    for i in range(2, n-2):
        e[i] = (x[i] - x[i-1])
        f[i] = 2 * (x[i+1] - x[i-1])
        g[i] = (x[i+1] - x[i])
        r[i] = 6 / (x[i+1] - x[i]) * (y[i+1] - y[i])
        r[i] = r[i] + 6 / (x[i] - x[i-1]) * (y[i-1] - y[i])
    e[n-1] = (x[n-1] - x[n-2])
    f[n-1] = 2 * (x[n] - x[n-2])
    r[n-1] = 6 / (x[n] - x[n-1]) * (y[n] - y[n-1])
    r[n-1] = r[n-1] + 6 / (x[n-1] - x[n-2]) * (y[n-2] - y[n-1])


def decompose(e, f, g, n):
    for k in range(2, n):
        e[k] = e[k] / f[k-1]
        f[k] = f[k] - e[k] * g[k-1]


def substitute(e, f, g, r, n, x):
    for k in range(2, n):
        r[k] = r[k] - e[k] * r[k-1]
    x[n-1] = r[n-1] / f[n-1]
    for k in range(n-2, 0, -1):
        x[k] = (r[k] - g[k] * x[k+1]) / f[k]


def interpol(x, y, n, d2x, xu, results):
    flag = 0
    i = 1
    while(True):
        if xu >= x[i-1] and xu <= x[i]:
            c1 = d2x[i-1] / (6 * (x[i] - x[i-1]))
            c2 = d2x[i] / (6 * (x[i] - x[i-1]))
            c3 = (y[i-1] / (x[i] - x[i-1])) - ((d2x[i-1] * (x[i] - x[i-1])) / 6)
            c4 = (y[i] / (x[i] - x[i-1])) - ((d2x[i] * (x[i] - x[i-1])) / 6)
            t1 = c1 * pow((x[i] - xu), 3)
            t2 = c2 * pow((xu - x[i-1]), 3)
            t3 = c3 * (x[i] - xu)
            t4 = c4 * (xu - x[i-1])
            results[0] = t1 + t2 + t3 + t4
            t1 = -3 * c1 * pow((x[i] - xu), 2)
            t2 = 3 * c2 * pow((xu - x[i-1]), 2)
            t3 = -c3
            t4 = c4
            results[1] = t1 + t2 + t3 + t4
            t1 = 6 * c1 * (x[i] - xu)
            t2 = 6 * c2 * (xu - x[i-1])
            results[2] = t1 + t2
            flag = 1
        else:
            i = i + 1
        if i == n + 1 or flag == 1:
            break
    if flag == 0:
        print('outside range')


'''n = int(input('Ingrese el numero de intervalos: '))
print('\nIngrese las coordenadas x,y de los puntos a analizar:\nEjemplo: x1:y1 > 3.5:2.6')
x = []
y = []
for i in range(n + 1):
    aux = input('x' + str(i) + ':y' + str(i) + ' > ').split(':')
    x.append(float(aux[0]))
    y.append(float(aux[1]))
'''
n = 3
x = [3, 4.5, 7, 9]
y = [2.5, 1, 2.5, 0.5]
xi = 5#float(input('Ingrese el valor a evaluar: '))
results = [0, 0, 0]
spline(x, y, n, xi, results)
print(results[0])
