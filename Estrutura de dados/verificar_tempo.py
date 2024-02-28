import time

# Registrar o tempo de início
start_time = time.time()

# Seu código aqui


# Por exemplo, uma operação demorada como um loop
for i in range(1000000):
    _ = i * i

# Registrar o tempo de término
end_time = time.time()

# Calcular a diferença para obter o tempo total
execution_time = end_time - start_time

print("O tempo de execução do código foi de:", execution_time, "segundos")
