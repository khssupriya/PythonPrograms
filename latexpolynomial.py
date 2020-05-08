def pre_process(polynomial):
    return polynomial.strip("$").replace(" ","").replace("+"," +").replace("-"," -")

def mathematician_latex_polynomial(polynomial: str)->str:
    polynomial = pre_process(polynomial)

    if polynomial[0] != "-":
        polynomial = "+" + polynomial

    expressions = polynomial.split(" ")
    mathematician_polynomial=" ".join(expressions[::-1])

    if mathematician_polynomial[0] == "+":
        mathematician_polynomial = mathematician_polynomial[1:]

    return  "$" + mathematician_polynomial + "$"

print(mathematician_latex_polynomial("$3x^4 -  7x^3 +21x +17$"))
print(mathematician_latex_polynomial("$3x^4 - 7x^3 + 21x +17$"))