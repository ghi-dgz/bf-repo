from math import sqrt
from math import factorial as fact

class Term:
    def __init__(self, coefficient: int, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent

    def __repr__(self):
        if self.exponent == 0:
            return f"{self.coefficient}"
        elif self.exponent == 1:
            return f"{self.coefficient} x"
        else:
            return f"{self.coefficient} x^{self.exponent}"

    def integral(self):
        new_exponent = self.exponent + 1
        new_coefficient = self.coefficient / new_exponent
        uwu = Term(new_coefficient, new_exponent)
        return uwu

    def evaluate(self, x: float) -> float:
        return self.coefficient * (x ** self.exponent)

    def __add__(self, other):
        if self.exponent == other.exponent:
            return Term(self.coefficient + other.coefficient, self.exponent)
        else:
            raise ValueError("Terms must have the same exponent to add")

    def __mul__(self, other):
        if isinstance(other, Term):
            return Term(self.coefficient * other.coefficient, self.exponent + other.exponent)
        elif isinstance(other, (int, float)):
            return Term(self.coefficient * other, self.exponent)
        else:
            raise TypeError("Can only multiply by a Term or scalar (int/float)")


def get_term(n: int):
    top = (-1)**(n-1) * fact(2*n)
    bottom = 4**n * (fact(n) ** 2) * (2*n - 1)
    exponent = n
    coeff = top/bottom
    uwu = Term(coeff, exponent)
    return uwu

terms = []
for n in range(20):
    term = get_term(n)
    print(term)
    terms.append(term)
    # now integrate them term by term across [0, 1/4]

integral_list = []
for term in terms:
    term.exponent += 0.5 # times by sqrt(x)
    integral_list.append(term.integral())

print(integral_list)

final = []
for term in integral_list:
    bottom = term.evaluate(0)
    top = term.evaluate(1/4)
    diff = top - bottom
    final.append(diff)
print(final)

final_final = 0
for num in final:
    final_final += num

print(final_final)
print(24*final_final +  (3/4 * sqrt(3)))