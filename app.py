"""
#Try, Except, else e finally

try:
    a = 18
    b=0
    print('Inicío do Try')
    c=a/b
    print('Fim do try')
except ZeroDivisionError as e:
    print(f'Deu um erro',e.__class__.__name__,' no try')
except NameError:
    print('Deu um erro NameError no try')
except (TypeError, IndexError) as error:
    print('Deu um erro TypeError e IndexError no try')
    print('MSG:',error)
    print('Nome do erro:', error.__class__.__name__)
except Exception:
    print('Aqui fodeu, o erro é desconhecido')

print('Código normal')
"""

"""
#try, finally e else
try:
    print('Try')
    8/0
except ZeroDivisionError:
    print('Except de erro')
else:
    print('Else, Não deu erro nenhum')
finally:
    print('Finally')
"""

""""""
#RAISE - lançando exceções (erros)
#print(123)
#raise ValueError('Deu erri')
def divide(n,d):
    try:
        return n/d 
    except ZeroDivisionError:
        print('Except')
        raise
def nao_aceito_zero(d):
    if d==0:
        raise ZeroDivisionError('Você dividio por zero')
    return True
def tipo_dado(a):
    tipo_d = type(a)
    if not isinstance(a, (float, int)):
        raise TypeError(
            f'{a} deve ser int ou float, o dado de erro '
            ''
            f'{tipo_d.__name__} enviado'
        )
def div (n,d):
    tipo_dado(d)
    tipo_dado(n)

    nao_aceito_zero(d)
    return n/d
print(div(8,'0'))