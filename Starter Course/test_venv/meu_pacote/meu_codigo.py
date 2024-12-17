from meu_pacote.modulo_A.script_A import var_A
from meu_pacote.modulo_B.script_B import var_B
from meu_pacote.modulo_C.script_C import var_C

def func():
  print(var_A + var_B + var_C)

if __name__ == '__main__':
  print('testando: func')
  func()