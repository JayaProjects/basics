f1 = open("pree.jpg",'rb')
f2 = open("preeNew1.jpg",'wb')
bytes = f1.read()
f2.write(bytes)