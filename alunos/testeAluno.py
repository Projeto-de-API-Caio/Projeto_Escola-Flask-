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
        
        r = requests.post('http://localhost:8000/alunos', json={"id": 1, "nome": "Filipe", "data_nascimento":"2000-01-01", "nota_primeiro_semestre":10.0, "nota_segundo_semestre":5.0, "turma_id":2})
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:8000/alunos')
        self.assertEqual(len(r_lista.json()), 1)
        self.assertEqual(r_lista.json()[0]['id'], 1)
        print("3 OK")

    # TESTES JOICY-------------------------------------------------------------------------------------
    

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()
