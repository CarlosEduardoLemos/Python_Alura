from validate_docbr import CPF

class Cpf:
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
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return (f"{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}")


