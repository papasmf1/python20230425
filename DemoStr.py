# DemoStr.py 
#print( dir(str) )
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.startswith("pyt"))
print(strB.endswith("ful"))
print(strB.upper())
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split() 
print(lst)
print("---다시 하나의 문자열---")
print(":)".join(lst))


