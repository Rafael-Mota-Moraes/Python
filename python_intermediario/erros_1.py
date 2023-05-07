a = 18
b = 0

try:
    c = a / b
    print('string'[1000])
except (ZeroDivisionError, IndexError) as error:
    print('ZeroDivisionError ou IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except NameError:
    print('NameError')
except Exception:
    print('Erro genérico')
