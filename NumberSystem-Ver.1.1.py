def bintodec(binn):
    n=0
    dec=0
    for i in binn[::-1]:
        dec+=int(i)*(2**n)
        n+=1
    print(f"BIN to DEC:{dec}\n")

def bintohex(binn):
    #bintodec
    n = 0
    dec = 0
    for i in binn[::-1]:
        dec += int(i) * (2 ** n)
        n += 1
    #dectohex
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hexx = ""
    while True:
        if dec % 16 == 10:
            hexx += "A"
        elif dec % 16 == 11:
            hexx += "B"
        elif dec % 16 == 12:
            hexx += "C"
        elif dec % 16 == 13:
            hexx += "D"
        elif dec % 16 == 14:
            hexx += "E"
        elif dec % 16 == 15:
            hexx += "F"
        else:
            hexx += str(dec % 16)
        dec = dec // 16
        if dec in lst:
            if dec == 10:
                hexx += "A"
            elif dec == 11:
                hexx += "B"
            elif dec == 12:
                hexx += "C"
            elif dec == 13:
                hexx += "D"
            elif dec == 14:
                hexx += "E"
            elif dec == 15:
                hexx += "F"
            else:
                hexx += str(dec)
            break
    return print(f"BIN to HEX:{hexx[::-1]}\n")

def dectobin(dec):
    binn=""
    while True:
        binn += str(dec % 2)
        dec = dec // 2
        if dec==1 or dec==0:
            binn+=str(dec)
            break
    return print(f"DEC to BIN:{binn[::-1]}\n")

def dectohex(dec):
    lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    hexx=""
    while True:
        if dec%16==10:
            hexx+="A"
        elif dec%16==11:
            hexx+="B"
        elif dec%16==12:
            hexx+="C"
        elif dec%16==13:
            hexx+="D"
        elif dec%16==14:
            hexx+="E"
        elif dec%16==15:
            hexx+="F"
        else:
            hexx+=str(dec%16)
        dec=dec//16
        if dec in lst:
            if dec== 10:
                hexx += "A"
            elif dec== 11:
                hexx += "B"
            elif dec== 12:
                hexx += "C"
            elif dec== 13:
                hexx += "D"
            elif dec== 14:
                hexx += "E"
            elif dec== 15:
                hexx += "F"
            else:
                hexx += str(dec)
            break
    return print(f"DEC to HEX:{hexx[::-1]}\n")

def hextodec(hexx):
    n=0
    dec=0
    for i in hexx[::-1]:
        if i=='A':
            dec+=10*(16**n)
        elif i=="B":
            dec+=11*(16**n)
        elif i=="C":
            dec+=12*(16*n)
        elif i=="D":
            dec+=13*(16**n)
        elif i=="E":
            dec+=14*(16**n)
        elif i=="F":
            dec+=15*(16**n)
        else:
            dec+=int(i)*(16**n)
        n+=1
    print(f"HEX to DEC:{dec}\n")

def hextobin(hexx):
    #hextodec
    n=0
    dec=0
    for i in hexx[::-1]:
        if i=='A':
            dec+=10*(16**n)
        elif i=="B":
            dec+=11*(16**n)
        elif i=="C":
            dec+=12*(16*n)
        elif i=="D":
            dec+=13*(16**n)
        elif i=="E":
            dec+=14*(16**n)
        elif i=="F":
            dec+=15*(16**n)
        else:
            dec+=int(i)*(16**n)
        n+=1
    #dectobin
    binn = ""
    while True:
        binn += str(dec % 2)
        dec = dec // 2
        if dec == 1 or dec == 0:
            binn += str(dec)
            break
    return print(f"HEX to BIN:{binn[::-1]}\n")

while True:
    print("Calculator NuberSystem\n1.BINtoDEC\n2.BINtoHEX\n3.DECtoBIN\n4.DECtoHEX\n5.HEXtoDEC\n6.HEXtoBIN\n")
    ns=input("Enter NumberSystem(-1 for Exit):")
    if ns=="-1":
        print("\nCalculator NumberSystem \nEnd Program\nBye Bye...")
        break
    elif ns=="1":
        binn=input("Enter Binary Number:")
        bintodec(binn)
        continue
    elif ns=="2":
        binn=input("Enter Binary Number:")
        bintohex(binn)
        continue
    elif ns=="3":
        dec=int(input("Enter Decimal Number:"))
        dectobin(dec)
        continue
    elif ns=="4":
        dec=int(input("Enter Decimal Number:"))
        dectohex(dec)
        continue
    elif ns=="5":
        hexx=input("Enter Hexadecimal Number:")
        hextodec(hexx)
        continue
    elif ns=="6":
        hexx = input("Enter Hexadecimal Number:")
        hextobin(hexx)
        continue
    else:
        print("Eror Eror\nPlease Enter Agian")
        continue