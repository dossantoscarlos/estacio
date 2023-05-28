from Paciente import Paciente 
class PacienteService : 
	
	def listPaciente (self, paciente) : 
		lista = paciente	
		if(self.validaCampo(lista)) :
			print("maior de idade") if self.maiorIdade(lista.getIdade()) else print("menor de idade")
			return lista.toList()
		else :
			return "Campos invalidos foram identificados!!!"

	def maiorIdade(self, idade) :
		return True if idade >= 18 else False

	def validaCampo (self, paciente) :
		if len(paciente.getNome().strip(" ")) == 0 :
			print("Nome")
			return False
		elif paciente.getIdade() == 0  :
			print('idade')
			return False
		elif len(paciente.getSexo().strip(" ")) == 0 :
			print("sexo")
			return False
		elif paciente.getDeclaracaoSaude() == 0  : 
			#print('decsau')
			return True
		else :
			return True
	
paciente = Paciente('joao','masculino', 34)
service = PacienteService()

print(service.listPaciente(paciente))