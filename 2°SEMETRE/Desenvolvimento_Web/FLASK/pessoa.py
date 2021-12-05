class Pessoa():
    def __init__(self, nome, matricula, curso, nota):
        self.nota = nota
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso
    
    def get_nota(self):
        return self.nota    
    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def get_curso(self):
        return self.__curso
        