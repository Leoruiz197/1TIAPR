try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print(f"resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: nao é possivel dividir por zero")
except ValueError:
    print("Erro: entrada invalida")
except:
    print("Erro: generico")
finally:
    print("Bloco finally executado")