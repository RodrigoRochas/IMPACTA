class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def lista_filmes(self, lista_filmes):
        self.lista_filmes = []

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

lista_filmes = []

for c in range(1,4):
    titulo = str(input('Digite o titulo do filme : '))
    genero = str(input('Digite o genero do filme : '))
    filme = Filme(titulo, genero)
    lista_filmes.append(filme)


for i in lista_filmes:
    print('*' * 30)
    print('Titulo', filme.get_titulo())
    print('Genero', filme.get_genero())