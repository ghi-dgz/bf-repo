"""
rewriten in python based off https://blogs.sas.com/content/iml/2023/03/08/newton-pi.html
"""
import scipy.integrate as integrate
import math

def SemiCircle(x):
    return math.sqrt(x - x**2)

M, _ = integrate.quad(SemiCircle, 0, 0.25)

AreaTri = 1/2 * (1/4) * (math.sqrt(3) / 4)
piApprox = 24 * (M + AreaTri)

print(f"{piApprox:.14f}")