"""
Escreva uma função chamada right_justify, que receba uma string chamada 
's' como parâmetro e exiba a string com espaços suficientes à frente
para que a última letra da string esteja na coluna 70 da tela.
Dica: Use concatenação de strings e repetição. Além disso, o Python
oferece uma função
"""
def right_justify(s):
    total_column = 70
    total_blank_space = total_column - len(s)
    print(f"{' '*total_blank_space}{s}")

right_justify('Teste')