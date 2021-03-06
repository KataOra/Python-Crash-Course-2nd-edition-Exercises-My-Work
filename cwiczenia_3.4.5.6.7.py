#3.4
goscie = ['tata', 'babcia', 'tesciowa', 'pawlikowska']
print(f"Serdecznie zapraszam na obiad {goscie[0].title()}!")
zaproszenie = 'Serdecznie zapraszam na obiad'
print(f"{zaproszenie} {goscie[1].title()}")
print(f"{zaproszenie} {goscie[2].title()}")
print(f"{zaproszenie} {goscie[3].title()}")
# 3.5
print(f"{goscie[2].title()} nie może przyjsc")
goscie.remove('tesciowa')
print(goscie)
goscie.insert(2, 'patka')
print(goscie)
print(f"{zaproszenie} {goscie[0].title()}")
print(f"{zaproszenie} {goscie[1].upper()}")
print(f"{zaproszenie} {goscie[2].title()}")
print(f"{zaproszenie} {goscie[3].upper()}")
# 3.6
print("Znaleziono wiekszy stol")
goscie.insert(0, 'Bartek')
goscie.insert(2, 'krychu')
goscie.append('lechu')
print(goscie)
print(f"{zaproszenie} {goscie[0].title()}")
print(f"{zaproszenie} {goscie[1].title()}")
print(f"{zaproszenie} {goscie[2].title()}")
print(f"{zaproszenie} {goscie[3].title()}")
print(f"{zaproszenie} {goscie[4].title()}")
print(f"{zaproszenie} {goscie[5].title()}")
print(f"{zaproszenie} {goscie[6].title()}")
#3.7
print("Na obiad niestety moge zaprosic tylko 2 osoby, stol nie dojechal")
wywalony1 = goscie.pop()
przepraszam = 'Przepraszam ale nie ma dla ciebie miejsca'
print(f"{przepraszam} {wywalony1.title()}")
wywalony2 = goscie.pop()
print(f"{przepraszam} {wywalony2.title()}")
wywalony3 = goscie.pop()
print(f"{przepraszam} {wywalony3.title()}")
wywalony4 = goscie.pop()
print(f"{przepraszam} {wywalony4.title()}")
wywalony5 = goscie.pop()
print(f"{przepraszam} {wywalony5.title()}")
print(f"{zaproszenie} {goscie[0].title()}")
print(f"{zaproszenie} {goscie[1].title()}")
del goscie[0]
del goscie[0]
print(goscie)

