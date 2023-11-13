def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    hanoi(n - 1, origen, destino, auxiliar)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, origen, destino)

n = 3  # Cambia este valor para el número de discos
hanoi(n, 'Origen', 'Auxiliar', 'Destino')