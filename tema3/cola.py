import queue

# Crear una cola
cola = queue.Queue()

# Agregar elementos a la cola
cola.put("manzana")
cola.put("banana")
cola.put("cereza")

print("Elementos en la cola:")
while not cola.empty():
    print(cola.get())