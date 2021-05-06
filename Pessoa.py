class Pessoa():
    def __init__(self, nome, idade, institucionalizada, pcd, trabalhaNaAreaDeSaude, possuiComorbidades, trabalhaNaAreaDaEducacao, trabalhaNaAreaDeSeguranca, trabalhaNaAreaDeTransporte):
        self.nome = nome
        self.idade = idade
        self.institucionalizada = institucionalizada
        self.pcd = pcd
        self.areaDeSaude = trabalhaNaAreaDeSaude
        self.comorbidades = possuiComorbidades
        self.areaDaEducacao = trabalhaNaAreaDaEducacao
        self.areaDeSeguranca = trabalhaNaAreaDeSeguranca
        self.areaDeTransporte = trabalhaNaAreaDeTransporte
        
        self.pontuacao = self.calculaPontuacao()
        
    def calculaPontuacao(self):
        # Pessoas com 60 anos ou mais institucionalizadas
        # Pessoas com deficiência institucionalizadas
        if (self.institucionalizada):
            if (self.idade >= 60):
                return 100
            elif (self.pcd):
                return 95
        
        # Trabalhadores de saúde
        if (self.areaDeSaude):
            return 90
        
        # Pessoas de 80 anos ou mais
        if (self.idade >= 80):
            return 85
        # Pessoas de 75 a 79 anos
        elif (self.idade >= 75):
            return 80
        # Pessoas de 70 a 74 anos
        elif (self.idade >= 70):
            return 75
        # Pessoas de 65 a 69 anos
        elif (self.idade >= 65):
            return 70
        # Pessoas de 60 a 64 anos
        elif (self.idade >= 60):
            return 65
        
        # Indivíduos com comorbidades (doenças que favorecem o agravamento da Covid-19)
        if (self.comorbidades):
            return 60
        # Pessoas com deficiência permanente grave
        if (self.pcd):
            return 55
        # Trabalhadores da educação
        if (self.areaDaEducacao):
            return 50
        # Forças de segurança e salvamento
        if (self.areaDeSeguranca):
            return 45
        # Trabalhadores de transporte
        if (self.areaDeTransporte):
            return 40
        
        return 20
        
        
        