#print("Verificação clientes 8, 15, 20, cinema")
def verify(age):
    if age < 20:
        if age == 8 or age == 15:
            print("Sua idade é inferior a permitida, proibido entrar!\n")
        else:
            print("\Sua idade é inferior a permitida, proibido entrar!\n")
    else:
        print("Idade adequada, entrada permitida!\n")

verify(15)
verify(20)
verify(8)
