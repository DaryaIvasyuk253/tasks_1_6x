import math

#task_1
#---------------------------------------------------
a = 12
b = 21
c = 55
d = a + b * (c/2)
result = "Значение переменной при параметрах %d, %d и %d равно %.1f" % (a, b, c, d)
print(result)

#task_2
#----------------------------------------------------
a = 32
b = 17
d = (a**2 + b**2) % 2
result = "Значение переменной при параметрах %d и %d равно %d" % (a, b, d)
print(result)

#task_3
#----------------------------------------------------
a = 68
b = 23
c = 71
d = (a + b) / 12 * c % 4 + b
result = "Значение переменной при параметрах %d, %d и %d равно %.1f" % (a, b, c, d)
print(result)

#task_4
#-----------------------------------------------------
a = 42
b = 2
c = 3
d = (a - b * c) / (a + b) % c
result = "Значение переменной при параметрах %d, %d и %d равно %.1f" % (a, b, c, d)
print(result)

#task_5
#-----------------------------------------------------
a = 37
b = 25
c = 15
d = abs(a - b) / (a + b)**3 - math.cos(c)
result = "Значение переменной при параметрах %d, %d и %d равно %.1f" % (a, b, c, d)
print(result)

#task_6
#------------------------------------------------------
a = -5
b = 6
c = 7
d = (math.log1p(1 + c) / - b)**4 + abs(a)
result = "Значение переменной при параметрах %d, %d и %d равно %.3f" % (a, b, c, d)
print(result)

