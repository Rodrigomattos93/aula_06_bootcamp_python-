lista_recebida = input("Digite uma lista de números: ")
lista_recebida_splitada = lista_recebida.split(",")
lista_recebida_final = list(map(int, lista_recebida_splitada))

numero_recebido = input("Digite um número: ")
numero_recebido_final = int(numero_recebido)


def somar_um_numero_aos_elementos_da_lista(
        entrada_lista: list, entrada_numero: int) -> list:
    for i in range(0, len(entrada_lista)):
        entrada_lista[i] = entrada_lista[i] + entrada_numero

    return print(entrada_lista)


somar_um_numero_aos_elementos_da_lista(
    lista_recebida_final, numero_recebido_final)
