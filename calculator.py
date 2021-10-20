
while True:
    operator_c = input("Введите +, -, *, /. Если введете 0, то калькулятор закроется. ")
    if operator_c == "0":
        break
    else:
        a = int(input("первое число: "))
        b = int(input("второе число: "))
        if operator_c =="+":
            print(a+b)
        if operator_c =="*":
            print(a*b)
        if operator_c =="-":
            print(a-b)
        if operator_c =="/":
            print(a/b)