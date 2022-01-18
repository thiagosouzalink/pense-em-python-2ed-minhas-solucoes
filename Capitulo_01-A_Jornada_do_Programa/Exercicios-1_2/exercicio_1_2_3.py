"""
3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o
seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua
velocidade média em milhas por hora?
"""
quilometros = 10
minutos = 42
segundos = 42

milhas = quilometros / 1.61
tempo_total_segundos = minutos * 60 + segundos
tempo_total_horas = tempo_total_segundos / 3600

# Passo médio (min e seg por milha)
passo_medio = tempo_total_segundos / milhas # segundos / milha
passo_minuto = passo_medio // 60
passo_segundo = round(passo_medio % 60, 2)

# Velocidade média (milhas / hora)
velocidade_media = milhas / tempo_total_horas

print(f"O passo médio: {passo_minuto} min e {passo_segundo} s por milha")
print(f"A velocidade média é: {velocidade_media:.2f} milhas por hora")
