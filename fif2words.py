H100 = "Hundred"

def convert2digs(n: int) -> str: 
    upto20 = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ","nineteen "]
    tens = ["", "ten ", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]  
    ten_power = ["","", "hundred", "thousand", ]
    if n < len(upto20):
        return upto20[n]
    return tens[n//10] + upto20[n%10]

def convert3digs(n: int) -> str:
    if n < 100:
        return convert2digs(n)
    return convert2digs(n//100) + H100 + convert2digs(n%100)

def fix_and(s: str) -> str:
    if H100 in s and not s.endswith(H100):
        return s.replace(H100, H100 + "and ")
    else:
        return s

def fig2words(n: int) -> str:
    if n == 0:
        return "zero"
    return fix_and(convert3digs(n))
print(fig2words(11))