

divisor = int(input("Escolha a divisibilidade\n"
                    "[2] divisibilidade por 2: \n"
                    "[3] divisibilidade por 3: \n"
                    "[4] divisibilidade por 4: \n"
                    "[5] divisibilidade por 5: "))
num = str(input("Digite um número: "))
# print(num % 2)
if divisor == 2:
    if int(num) % 2 == 0:
        print("{} é divisível por 2".format(num))
    elif int(num) % 2 != 0:
        print("O número {} não é divisível por 2: ".format(num))
elif divisor == 3:
   if len(num) == 1 and int(num) % 3 == 0:
        print("O número {} é divisível por 3 ".format(num))
   elif int(num) % 3 != 0:
        print("O número {} não é divisível por 3".format(num))
   elif len(num) == 2:
       primeiro = int(num[0])
       segundo = int(num[1])
       if (primeiro + segundo) % 3 == 0:
           print("O número {} é divisível por 3 ".format(num))
       elif (primeiro + segundo) % 3 != 0:
           print("O número {} não é divisível por 3".format(num))
   elif len(num) == 3:
       primeiro = int(num[0])
       segundo = int(num[1])
       terceiro = int(num[2])
       if (primeiro + segundo + terceiro) % 3 == 0:
           print("O número {} é divisível por 3 ".format(num))
       elif (primeiro + segundo + terceiro) % 3 != 0:
           print("O número {} não é divisível por 3".format(num))




