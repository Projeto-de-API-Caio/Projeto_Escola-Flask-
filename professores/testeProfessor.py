import requests
import unittest

class TestStringMethods(unittest.TestCase):

    def test_001_get_professores(self):
            r = requests.get('http://localhost:8000/professores')
            self.assertEqual(r.status_code, 200)
            professores = r.json()
            self.assertIsInstance(professores, list)
            print("1 OK")

    def test_002_lista_vazia(self):
         # verifica se a lista professores está vazia

        r = requests.get('http://localhost:8000/professores')
        self.assertEqual(r.status_code, 200)
        professores = r.json()
        self.assertEqual(len(professores), 0)
        print("2 OK")

    def test_003_get_dados(self):
        # garante que a lista professores traga dados criados

        r = requests.post('http://localhost:8000/professores', json={
                                                                "nome": "Caio",
                                                                "idade":35,
                                                                "materia":"API",
                                                                "observacoes":"teste"})
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:8000/professores')
        self.assertEqual(r_lista.json()[0]['id'], 1)
        print("3 OK")

    # TESTES JOICY-------------------------------------------------------------------------------------
    def test_004_buscaProfessorId(self):

         # busca professor por ID
        r = requests.get('http://localhost:8000/professores/1')
        self.assertEqual(r.status_code, 200)
        professor = r.json()
        self.assertEqual(professor['id'], 1)
        print("4 OK")

    def test_005__ProfessorInexistente(self):
        # tenta acessar professor que não existe

        r = requests.get('http://localhost:8000/professores/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["error"], 'Professor não encontrado')  
        print("5 OK")

    def test_006_verificação(self):
         # verifica se dados retornados são certos

        r = requests.post('http://localhost:8000/professores', json={
                                                                "nome": "João",
                                                                "idade":48,
                                                                "materia":"dev",
                                                                "observacoes":"teste6"})
        self.assertEqual(r.status_code, 200)
        professor_id = r.json()['id']
        r_get = requests.get(f'http://localhost:8000/professores/{professor_id}')
        self.assertEqual(r_get.status_code, 200)
        professor = r_get.json()
        self.assertEqual(professor['id'], professor_id)
        print("6 OK")


    def test_007(self):
       # cria professor novo com dados válidos

        professor_data = {"nome": "Lucas", "idade":60, "materia":"matematica", "observacoes":"teste7"}
        r = requests.post('http://localhost:8000/professores', json=professor_data)
        self.assertEqual(r.status_code, 200)
        professor = r.json()
        professor_id = r.json()['id']
        self.assertEqual(professor['id'], professor_id)
        print("7 OK")


    def test_008(self):
        # cria professor sem nome (erro)

        professor_data = {"id": 4}
        r = requests.post('http://localhost:8000/professores', json=professor_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["erro"], "professor sem nome")
        print("8 OK")

    # TESTE VICTORIA-----------------------------------------------------------------------------------
    def test_009(self):
        # verifica se um professor pode ser deletado
        r = requests.delete('http://localhost:8000/professores/3')
        self.assertEqual(r.status_code, 204) 
        r = requests.get('http://localhost:8000/professores/3')
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["error"], "Professor não encontrado")
        print("9 OK")

    def test_010(self):
        #tenta deletar um professor que nao

        r = requests.delete('http://localhost:8000/professores/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["erro"], "Professor não encontrado")
        print("10 OK")

    def test_011(self):
        requests.post('http://localhost:8000/reseta')

        r = requests.post('http://localhost:8000/professores', json={"id": 5, "nome": "Fabiano"})
        self.assertEqual(r.status_code, 200)

        r_delete = requests.delete('http://localhost:8000/professores/5')
        self.assertEqual(r_delete.status_code, 200)

        r_lista = requests.get('http://localhost:8000/professores')
        professores = r_lista.json()
        self.assertFalse(any(professor["id"] == 5 for professor in professores), "Professor 5 ainda está na lista")

        print("11 OK")

    def test_012(self):
        #  editar o nome de um professor
        r = requests.post('http://localhost:8000/professores', json={
                                                                "nome": "Yohan",
                                                                "idade":31,
                                                                "materia":"português",
                                                                "observacoes":"teste12"})
        r = requests.put(f'http://localhost:8000/professores/1', json={"nome": "Yohan Lima"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["erro"], "Professor não encontrado") 
        print("12 OK")


    def test_013(self):
       # tentar editar um professor sem nome (erro)
        r = requests.put('http://localhost:8000/professores/3', json={"id": 3})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["erro"], "Professor não encontrado")  
        print("13 OK")

    def test_014(self):
        # tenta editar um professor que nao existe
        r = requests.put('http://localhost:8000/professores/1000', json={"nome": "Novo Nome"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()["erro"], "Professor não encontrado")  
        print("14 OK")
    
     # TESTE EXTRA------------------------------------------------------------------------------------
    def test_015(self):
        #criar professor sem nome (erro)

        professor_data = {"id": 6}
        r = requests.post('http://localhost:8000/professores', json=professor_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["erro"], "professor sem nome")
        print("15 OK")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()
    unittest.main()