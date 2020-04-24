R2A=dict(zip("MDCLXVI",[1000,500,100,50,10,5,1]))

EXCEPTIONS = ["CM","CD","XC","XL","IV","IV"]
REPLACERS = ["DCCCC","CCCC","LXXXX","XXXX","VIIII","IIII"]


CONVERTERS = dict(zip(EXCEPTIONS,REPLACERS))

def standardise(s: str) -> str:
	for conv in CONVERTERS:
		s=s.replace(conv,CONVERTERS[conv])
	return s

def roam2arabic(s: str) -> int:
	s=s.replace("CM","DCCCC").replace("CD","CCCC").replace("XC","LXXXX").replace("XL","XXXX").replace("IX","VIIII").replace("IV","IIII")
	#write above line or call standardise
	return sum(R2A[ch] for ch in s)

print(roam2arabic("XIV"))


