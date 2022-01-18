"""
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
(7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro
lugar, que horas chego em casa para o café da manhã?
"""
# Sair da minha casa às 6:52
inicio_hora = 6
inicio_minuto = 52
inicio_segundo = 0

# correr 1 quilômetro a um certo passo (8min15s por quilômetro)
p1_hora = 0
p1_minuto = 8
p1_segundo = 15

# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro)
p2_hora = 0
p2_minuto = 7
p2_segundo = 12

# 1 quilômetro no mesmo passo usado em primeiro lugar
p3_hora = 0
p3_minuto = 8
p3_segundo = 15

# Que horas chego em casa para o café da manhã?
total_segundo = inicio_segundo + p1_segundo + p2_segundo + p3_segundo
chegada_segundo = total_segundo % 60
resto_segundo = total_segundo // 60

total_minuto = inicio_minuto + p1_minuto + p2_minuto + p3_minuto + resto_segundo
chegada_minuto = total_minuto % 60
resto_minuto = total_minuto // 60

total_hora = inicio_hora + p1_hora + p2_hora + p3_hora + resto_minuto
chegada_hora = total_hora % 24

print(f"A chegada foi às {chegada_hora}:{chegada_minuto}:{chegada_segundo}")