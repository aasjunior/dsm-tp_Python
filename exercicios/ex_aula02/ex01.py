estatura_pessoa1 = float(input("Digite a estatura da primeira pessoa: "))
estatura_pessoa2 = float(input("Digite a estatura da segunda pessoa: "))
estatura_pessoa3 = float(input("Digite a estatura da terceira pessoa: "))
if estatura_pessoa1 == estatura_pessoa2 or estatura_pessoa2 == estatura_pessoa3 or estatura_pessoa1 == estatura_pessoa3:
    if estatura_pessoa2 == estatura_pessoa3:
        print("A estatura das três pessoas é a mesma")
    elif estatura_pessoa1 > estatura_pessoa3:
        print("A primeira e a segunda pessoa tem a mesma altura e são maiores que a terceira")
    else:
        print("A terceira pessoa é a maior")
elif estatura_pessoa1 > estatura_pessoa2 and estatura_pessoa1 > estatura_pessoa3:
    print("A primeira pessoa é maior")
elif estatura_pessoa2 > estatura_pessoa1 and estatura_pessoa2 > estatura_pessoa3:
    print("A segunda pessoa é maior")
elif estatura_pessoa3 > estatura_pessoa1 and estatura_pessoa3 > estatura_pessoa2:
    print("A terceira pessoa é maior")