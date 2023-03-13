# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 5
step = 0.1
step_acr = 0.0001
line_style ='-'
color ='b'

def switch_line():
    global line_style
    if line_style =='-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style

def switch_color():
    global color
    if color =='b':
        color = 'r'
    else:
        color = 'b'
    return color

def func(x):
    f = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 +d*x + e
    return f

x = np.arange(-limit, limit+step, step)
x_change = [(-limit, 'start')]

# pervonachalnoe napravlenie kakoe?
if func(-limit) > func(-limit+step):
    direction = False
else:
    direction = True

#opredelim tochki
for i in range(len(x) - 1):
    if (func(x[i]) > 0 and func(x[i+1]) < 0) or (func(x[i]) < 0 and func(x[i+1]) > 0):
        # potochnee naydem gde peresekaet 0
        x_acr = np.arange(x[i], x[i+1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if func(x_acr[j]) > 0 and func(x_acr[j + 1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j+1]) > 0:
                x_change.append((round(x_acr[j],2), 'root')) 
    if direction:
        # naydem tochki smeni napravleniya
        if func(x[i]) > func(x[i+1]):
            direction = False
            x_change.append((round(x[i],2), 'to down'))
    else:
        if func(x[i]) < func(x[i+1]):
            direction = True
            x_change.append((round(x[i],2), 'to up'))

x_change.append((limit, 'finish'))

# naydem otdelno min i max
max = [0,0]
min = [0,0]
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0], step)
    if x_change[i][1] == 'to down':
        if func(x_change[i][0]) > max[1]:
            max[0] = x_change[i][0]
            max[1] = round(func(x_change[i][0]),2)
    elif x_change[i][1] == 'to up':
        if func(x_change[i][0]) < min[1]:
            min[0] = x_change[i][0]
            min[1] = round(func(x_change[i][0]),2)

# dopishem gde min i max
x_change2 = []
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0], step)
    if x_change[i][0] == max[0]:
        x_change2.append((x_change[i][0], 'max and to down'))
    elif x_change[i][0] == min[0]:
        x_change2.append((x_change[i][0], 'min and to up'))
    else:
        x_change2.append(x_change[i])
print(*x_change2)

# teper grafic!
for i in range(len(x_change2) - 1):
    cur_x = np.arange(x_change2[i][0], x_change2[i + 1][0]+step, step)
    if x_change2[i][1] == 'root':
        plt.plot(x_change2[i][0], func(x_change2[i][0]), 'go') # tochki korney
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    elif x_change2[i][1] == 'max and to down':
        plt.plot(x_change2[i][0], func(x_change2[i][0]), 'go') # dalee tochki min/max i smena cveta
        plt.plot(cur_x, func(cur_x), switch_color())
    elif x_change2[i][1] == 'min and to up':
        plt.plot(x_change2[i][0], func(x_change2[i][0]), 'go') 
        plt.plot(cur_x, func(cur_x), switch_color())
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

plt.grid()
plt.show()
