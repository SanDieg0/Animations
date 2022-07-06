def ecuacionCuadratica(a, b, c):
  discriminante=(b**2-(4*a*c))
  if discriminante>0:
    x1=(-b+(discriminante**(1/2)))/(2*a)
    x2=(-b-(discriminante**(1/2)))/(2*a)
    print(x1, " ", x2)
    
  elif discriminante<0:
    print("Las raíces son imaginarias")

  elif discriminante==0:
    x=-b/(2*a)
    print(x)

m = float(input("#1 "))
n = float(input("#2 "))
o = float(input("#3 "))

ecuacionCuadratica(m, n, o)
