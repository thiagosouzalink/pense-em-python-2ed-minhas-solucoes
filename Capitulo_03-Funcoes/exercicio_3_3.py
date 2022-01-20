"""
1. Escreva uma função que desenhe uma grade como a seguinte:
            + - - - - + - - - - +
            |         |         |
            |         |         |
            |         |         |
            |         |         |
            + - - - - + - - - - +
            |         |         |
            |         |         |
            |         |         |
            |         |         |
            + - - - - + - - - - +
Dica: para exibir mais de um valor em uma linha, podemos usar uma
sequência de valores separados por vírgula:
print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma: python
print('+', end=' ') print('-') A saída dessas instruções é + -. Uma
instrução print sem argumento termina a linha atual e vai para a próxima
linha.
2. Escreva uma função que desenhe uma grade semelhante com quatro linhas
e quatro colunas.
"""

# Function that draws two complementary columns
def draw_complete_two_column():
    print(' -'*4, '+', end='')
    print(' -'*4, '+', end='')


# Function that draws two complementary columns containing blanks spaces.
def draw_complete_two_column_with_blank_space():
    print('  '*4, '|', end='')
    print('  '*4, '|', end='')


# Function that draws two columns with symbol at the beginning
def draw_init_traces_two_column():
    print('+', end='')
    draw_complete_two_column()


# Function that draws two columns, containing blanks spaces, with symbol at the beginning
def draw_init_blanck_two_column():
    print('|', end='')
    draw_complete_two_column_with_blank_space()


# Function that draws two complete columns
def draw_first_twice_columns():
   draw_init_traces_two_column()
   print()
   draw_init_blanck_two_column()
   print()
   draw_init_blanck_two_column()
   print()
   draw_init_blanck_two_column()
   print()
   draw_init_blanck_two_column()


# Function that draws four complete columns
def draw_one_line_four_columns():
    draw_init_traces_two_column()
    draw_complete_two_column()
    print()
    draw_init_blanck_two_column()
    draw_complete_two_column_with_blank_space()
    print()
    draw_init_blanck_two_column()
    draw_complete_two_column_with_blank_space()
    print()
    draw_init_blanck_two_column()
    draw_complete_two_column_with_blank_space()
    print()
    draw_init_blanck_two_column()
    draw_complete_two_column_with_blank_space()


# 1. Escreva uma função que desenhe uma grade
def draw_grid():
    draw_first_twice_columns()
    print()
    draw_first_twice_columns()
    print()
    draw_init_traces_two_column()


# Escreva uma função que desenhe uma grade semelhante com quatro linhas
# e quatro colunas.
def draw_four_lines_four_columns():
    draw_one_line_four_columns()
    print()
    draw_one_line_four_columns()
    print()
    draw_one_line_four_columns()
    print()
    draw_one_line_four_columns()
    print()
    draw_init_traces_two_column()
    draw_complete_two_column()



draw_grid()
print()
draw_four_lines_four_columns()
