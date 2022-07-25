a = 3
b = 6
c = - 5

d1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
d2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

tup_a = (round(d1, 4), round(d2, 4))
print(tup_a)