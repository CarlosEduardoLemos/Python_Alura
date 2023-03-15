from validate_docbr import CPF

class CpfCnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("VPF inválido!!")

        
    def __str__(self):
        return self.format_cpf()


    def cpf_eh_Valido(self, documento):
        if len(documento) ==11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida!!")
        
    
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
