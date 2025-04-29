import requests
import unittest

class TestStringMethods(unittest.TestCase): 

    def test_001_get_alunos(self):
        
        r = requests.get('http://localhost:8000/alunos')
        self.assertEqual(r.status_code, 200)
        alunos = r.json()
        self.assertIsInstance(alunos, list)
        print("1 OK")

    def test_002_lista_vazia(self):
         # verifica se a lista alunos está vazia

        r = requests.get('http://localhost:8000/alunos')
        self.assertEqual(r.status_code, 200)
        alunos = r.json()
        self.assertEqual(len(alunos), 0)
        print("2 OK")

    def test_003_get_dados(self):
        # garante que a lista alunos traga dados criados

        r = requests.post('http://localhost:8000/alunos', json={"id": 1, "nome": "Filipe"})
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:8000/alunos')
        self.assertEqual(len(r_lista.json()), 1)
        self.assertEqual(r_lista.json()[0]['nome'], 'Filipe')
        print("3 OK")

    # TESTES JOICY-------------------------------------------------------------------------------------
    def test_004_buscaAlunoId(self):

         # busca aluno por ID
        r = requests.get('http://localhost:8000/alunos/1')
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        self.assertEqual(aluno['id'], 1)
        self.assertEqual(aluno['nome'], 'Filipe')
        print("4 OK")

    def test_005__AlunoInexistente(self):
        # tenta acessar aluno que não existe

        r = requests.get('http://localhost:8000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("5 OK")

    def test_006_verificação(self):
         # verifica se dados retornados são certos

        r = requests.post('http://localhost:8000/alunos', json={"id": 2, "nome": "Matheus"})
        self.assertEqual(r.status_code, 200)
        r_get = requests.get('http://localhost:8000/alunos/2')
        self.assertEqual(r_get.status_code, 200)
        aluno = r_get.json()
        self.assertEqual(aluno['nome'], 'Matheus')
        print("6 OK")

    
    def test_007(self):
       # cria aluno novo com dados válidos

        aluno_data = {"id": 3, "nome": "Victoria"}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        self.assertEqual(aluno['nome'], 'Victoria')
        self.assertEqual(aluno['id'], 3)
        print("7 OK")

    def test_008(self):
        # verifica se nao é possível criar um aluno com ID que já existe

        aluno_data = {"id": 3, "nome": "Joicy"}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'id ja utilizada')
        print("8 OK")

    def test_009(self):
        # cria aluno sem nome (erro)

        aluno_data = {"id": 4}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("9 OK")
  
    # TESTE VICTORIA-----------------------------------------------------------------------------------
    def test_010(self):
        # verifica se um aluno pode ser deletado

        r = requests.delete('http://localhost:8000/alunos/3')
        self.assertEqual(r.status_code, 204) 
        r = requests.get('http://localhost:8000/alunos/3')
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("10 OK")

    def test_011(self):
        #tenta deletar um aluno que nao

        r = requests.delete('http://localhost:8000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("11 OK")

    def test_012(self):
        requests.post('http://localhost:8000/reseta')

        r = requests.post('http://localhost:8000/alunos', json={"id": 5, "nome": "Fabiano"})
        self.assertEqual(r.status_code, 200)

        r_delete = requests.delete('http://localhost:8000/alunos/5')
        self.assertEqual(r_delete.status_code, 204)

        r_lista = requests.get('http://localhost:8000/alunos')
        alunos = r_lista.json()
        self.assertFalse(any(aluno["id"] == 5 for aluno in alunos), "Aluno 5 ainda está na lista")

        print("12 OK")

    def test_013(self):
        #  editar o nome de um aluno

        r = requests.put('http://localhost:8000/alunos/3', json={"nome": "Fabiano Silva"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado') 
        print("13 OK")

    def test_014(self):
       # tentar editar um aluno sem nome (erro)
        r = requests.put('http://localhost:8000/alunos/3', json={"id": 3})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("14 OK")

    def test_015(self):
        # tenta editar um aluno que nao existe
        r = requests.put('http://localhost:8000/alunos/100', json={"nome": "Novo Nome"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("15 OK")
        
     # TESTE EXTRA------------------------------------------------------------------------------------
    def test_016(self):
        #criar aluno sem nome (erro)

        aluno_data = {"id": 6}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("16 OK")

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()
    unittest.main()
