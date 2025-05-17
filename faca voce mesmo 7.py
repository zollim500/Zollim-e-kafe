kmpecorrido = float(input("quantos km você pecorreu:"))
diasalugados = int(input("Dias que você alugou:"))
total = (kmpecorrido* 90) + (diasalugados * 0.20)

print ("----------nota fiscal-----------")
print (f"[1] - km = $ {(kmpecorrido * 0.20)}")
print (f"[2] - dias = $ {(diasalugados * 90)}")
print ("===================================")
print (f"TOTAL = R$ {total}")