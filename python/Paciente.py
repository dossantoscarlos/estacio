class Paciente :

	def __init__(self, nome, sexo, idade = 0, declaracaoSaude = False) : 
		self.nome = nome
		self.idade = idade
		self.sexo = sexo
		self.declaracaoSaude = declaracaoSaude

	def getNome(self): 
		return self.nome

	def getIdade(self):
		return self.idade

	def getSexo(self):
		return self.sexo

	def getDeclaracaoSaude(self):
		return self.declaracaoSaude

	def setDeclaracaoSaude(self, declaracaoSaude):
		self.declaracaoSaude = declaracaoSaude
		return self.declaracaoSaude

	def setSexo(self, sexo):
		self.sexo = sexo

	def setIdade(self, idade):
		self.idade = idade

	def setNome(self, nome):
		self.nome = nome

	def toList(self) :
		return [self.getNome(), self.getIdade() , self.getSexo(), self.getDeclaracaoSaude()]

