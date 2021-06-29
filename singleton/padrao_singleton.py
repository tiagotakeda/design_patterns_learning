class NomeQualquer(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NomeQualquer, cls).__new__(cls)
            ptin(f'Criando o objeto {cls.istance}')
        return cls.instance

s1 = NomeQualquer()
print(f'Instância 1: {id(s1)}')

s2 = NomeQualquer()
print(f'Instância 2: {id(s2)}')