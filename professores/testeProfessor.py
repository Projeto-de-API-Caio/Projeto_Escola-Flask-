import requests
import unittest

class TestStringMethods(unittest.TestCase):

    def test_001_get_professores(self):
            r = requests.get('http://localhost:5000/professores')
            self.assertEqual(r.status_code, 200)
            professores = r.json()
            self.assertIsInstance(professores, list)
            print("1 OK")

    def test_002_lista_vazia(self):
         # verifica se a lista professores está vazia

        r = requests.get('http://localhost:5000/professores')
        self.assertEqual(r.status_code, 200)
        professores = r.json()
        self.assertEqual(len(professores), 0)
        print("2 OK")

    def test_003_get_dados(self):
        # garante que a lista professores traga dados criados

        r = requests.post('http://localhost:5000/professores', json={"id": 1, "nome": "Filipe"})
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:5000/professores')
        self.assertEqual(len(r_lista.json()), 1)
        self.assertEqual(r_lista.json()[0]['nome'], 'Filipe')
        print("3 OK")

    # TESTES JOICY-------------------------------------------------------------------------------------
    def test_004_buscaProfessorId(self):

         # busca professor por ID
        r = requests.get('http://localhost:5000/professores/1')
        self.assertEqual(r.status_code, 200)
        professor = r.json()
        self.assertEqual(professor['id'], 1)
        self.assertEqual(professor['nome'], 'Filipe')
        print("4 OK")

    def test_005__ProfessorInexistente(self):
        # tenta acessar professor que não existe

        r = requests.get('http://localhost:5000/professores/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], 'Professor não encontrado')  
        print("5 OK")

    def test_006_verificação(self):
         # verifica se dados retornados são certos

        r = requests.post('http://localhost:5000/professores', json={"id": 2, "nome": "Matheus"})
        self.assertEqual(r.status_code, 200)
        r_get = requests.get('http://localhost:5000/professores/2')
        self.assertEqual(r_get.status_code, 200)
        professor = r_get.json()
        self.assertEqual(professor["nome"], "Matheus")
        print("6 OK")

    
    def test_007(self):
       # cria professor novo com dados válidos

        professor_data = {"id": 3, "nome": "Victoria"}
        r = requests.post('http://localhost:5000/professores', json=professor_data)
        self.assertEqual(r.status_code, 200)
        professor = r.json()
        self.assertEqual(professor["nome"], 'Victoria')
        self.assertEqual(professor["id"], 3)
        print("7 OK")

    def test_008(self):
        # verifica se nao é possível criar um professor com ID que já existe

        professor_data = {"id": 3, "nome": "Joicy"}
        r = requests.post('http://localhost:5000/professores', json=professor_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["error"], "id ja utilizada")
        print("8 OK")

    def test_009(self):
        # cria professor sem nome (erro)

        professor_data = {"id": 4}
        r = requests.post('http://localhost:5000/professores', json=professor_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["error"], "professor sem nome")
        print("9 OK")
  
    # TESTE VICTORIA-----------------------------------------------------------------------------------
    def test_010(self):
        # verifica se um professor pode ser deletado

        r = requests.delete('http://localhost:5000/professores/3')
        self.assertEqual(r.status_code, 200) 
        r = requests.get('http://localhost:5000/professores/3')
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["error"], "Professor não encontrado")
        print("10 OK")

    def test_011(self):
        #tenta deletar um professor que nao

        r = requests.delete('http://localhost:5000/professores/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], "Professor não encontrado")
        print("11 OK")

    def test_012(self):
        requests.post('http://localhost:5000/reseta')

        r = requests.post('http://localhost:5000/professores', json={"id": 5, "nome": "Fabiano"})
        self.assertEqual(r.status_code, 200)

        r_delete = requests.delete('http://localhost:5000/professores/5')
        self.assertEqual(r_delete.status_code, 200)

        r_lista = requests.get('http://localhost:5000/professores')
        professores = r_lista.json()
        self.assertFalse(any(professor["id"] == 5 for professor in professores), "Professor 5 ainda está na lista")

        print("12 OK")

    def test_013(self):
        #  editar o nome de um professor

        r = requests.put('http://localhost:5000/professores/3', json={"nome": "Fabiano Silva"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], "Professor não encontrado") 
        print("13 OK")

    def test_014(self):
       # tentar editar um professor sem nome (erro)
        r = requests.put('http://localhost:5000/professores/3', json={"id": 3})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], "Professor não encontrado")  
        print("14 OK")

    def test_015(self):
        # tenta editar um professor que nao existe
        r = requests.put('http://localhost:5000/professores/100', json={"nome": "Novo Nome"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], "Professor não encontrado")  
        print("15 OK")
        
     # TESTE EXTRA------------------------------------------------------------------------------------
    def test_016(self):
        #criar professor sem nome (erro)

        professor_data = {"id": 6}
        r = requests.post('http://localhost:5000/professores', json=professor_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["error"], "professor sem nome")
        print("16 OK")



def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()
    unittest.main()