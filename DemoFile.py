# DemoFile.py 
#쓰기(유니코드방식으로 쓰기) 
f = open("c:\\work2\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#읽기 
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read() 
print(result)
f.close() 



