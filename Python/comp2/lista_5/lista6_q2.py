class Pessoa:
    def __init__(self, nome, celular, telefone_fixo, email):
        if len(nome) < 3: raise Exception('Nome inválido')
        if len(email) <= 10: raise Exception('E=mail Inválido')
        if len(str(celular)) <8 or len(str(telefone_fixo)) < 8: raise Exception('Número Inválido')
        else:
            self.nome = nome
            self.celular = celular
            self.telefone_fixo = telefone_fixo
            self.email = email