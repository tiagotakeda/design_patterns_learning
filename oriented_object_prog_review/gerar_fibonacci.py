def gerar_fibonacci(qnt):
    if qnt <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        print(f'A sequência Fibonacci para {qnt} termo(s) é: ')
        cont = 0
        aux1, aux2 = 0, 1
        while cont < qnt:
            print(aux1)
            prox = aux1 + aux2
            aux1 = aux2
            aux2 = prox
            cont += 1

def main():
    qnt = int(input('Entre com a quantidade: '))
    gerar_fibonacci(qnt)

if __name__ == "__main__":
    main()