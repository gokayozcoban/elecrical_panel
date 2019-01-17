
a = "ON"
b = "ON"
c = "ON"
d = "ON"
e = "ON"
button = input("Which button turn off \n(Select a/b/c/d/e): ")
for i in a,b,c,d,e:
    if button == "a":
        print("b OFF\ne OFF\nc ON\nd ON")
        break
    if button == "b":
        print("c OFF\na OFF\nd ON\ne ON")
        break
    if button == "c":
        print("d OFF\nb OFF\ne ON\na ON")
        break
    if button == "d":
        print("e OFF\nc OFF\na ON\nb ON")
        break
    if button == "e":
        print("a OFF\nd OFF\nb ON\nc ON")
        break
else:
    print("Hatalı seçim!\nsadece a/b/c/d/e harflerini kullanın.")
