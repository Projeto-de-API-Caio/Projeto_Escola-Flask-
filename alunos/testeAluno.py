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
        _ = requests.post('http://localhost:8000/professores', json={
                                                                "nome": "Caio",
                                                                "idade":35,
                                                                "materia":"API",
                                                                "observacoes":"teste"})
        _ = requests.post('http://localhost:8000/turmas', json={
                                                                "descricao": "API",
                                                                "ativo":True,
                                                                "professor_id":1})
        r = requests.post('http://localhost:8000/alunos', json={
                                                                "nome": "Filipe",
                                                                "data_nascimento":"2000-01-01",
                                                                "nota_primeiro_semestre":10.0,
                                                                "nota_segundo_semestre":5.0,
                                                                "turma_id":1})
        print(r)
        self.assertEqual(r.status_code, 200)
        r_lista = requests.get('http://localhost:8000/alunos')
        self.assertEqual(r_lista.json()[0]['id'], 1)
        print("3 OK")

    # TESTES JOICY-------------------------------------------------------------------------------------
    def test_004_buscaAlunoId(self):

         # busca aluno por ID
        r = requests.get('http://localhost:8000/alunos/1')
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        self.assertEqual(aluno['id'], 1)
        print("4 OK") 

        ##colocar o delete aqui

    def test_005__AlunoInexistente(self):
        # tenta acessar aluno que não existe

        r = requests.get('http://localhost:8000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("5 OK")

    def test_006_verificação(self):
         # verifica se dados retornados são certos

        r = requests.post('http://localhost:8000/alunos', json={
                                                                "nome": "Matheus",
                                                                "data_nascimento":"1997-01-01",
                                                                "nota_primeiro_semestre":8.0,
                                                                "nota_segundo_semestre":8.0,
                                                                "turma_id":1})
        self.assertEqual(r.status_code, 200)
        aluno_id = r.json()['id']
        r_get = requests.get(f'http://localhost:8000/alunos/{aluno_id}')
        self.assertEqual(r_get.status_code, 200)
        aluno = r_get.json()
        self.assertEqual(aluno['id'], aluno_id)
        print("6 OK")
        ##delete aqui

    
    def test_007(self):
       # cria aluno novo com dados válidos

        aluno_data = {"id": 1,
                      "nome": "Fabiano",
                      "data_nascimento":"2005-01-01",
                      "nota_primeiro_semestre":6.0,
                      "nota_segundo_semestre":6.0,
                      "turma_id":1}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 200)
        aluno = r.json()
        aluno_id = r.json()['id']
        self.assertEqual(aluno['id'], aluno_id)
        print("7 OK")
        ## delete aqui

    
    def test_008(self):
        # cria aluno sem nome (erro)

        aluno_data = {"id": 4}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("8 OK")
  
    # TESTE VICTORIA-----------------------------------------------------------------------------------
    def test_009(self):
        # verifica se um aluno pode ser deletado
        _ = requests.post('http://localhost:8000/alunos', json={
                                                                "nome": "Matheus",
                                                                "data_nascimento":"1997-01-01",
                                                                "nota_primeiro_semestre":8.0,
                                                                "nota_segundo_semestre":8.0,
                                                                "turma_id":1})
        r = requests.delete('http://localhost:8000/alunos/3')
        self.assertEqual(r.status_code, 204) 
        r = requests.get('http://localhost:8000/alunos/3')
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("9 OK")
        ##delete aqui

    def test_010(self):
        #tenta deletar um aluno que nao

        r = requests.delete('http://localhost:8000/alunos/100')
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')
        print("10 OK")

    def test_011(self):
        
        r = requests.post('http://localhost:8000/alunos', json={"nome": "Filipe",
                                                                "data_nascimento":"2000-01-01",
                                                                "nota_primeiro_semestre":10.0,
                                                                "nota_segundo_semestre":5.0,
                                                                "turma_id":1})
        self.assertEqual(r.status_code, 200)

        aluno_id = r.json()['id']
        r_delete = requests.delete('http://localhost:8000/alunos/{aluno_id}')
        self.assertEqual(r_delete.status_code, 204)

        r_lista = requests.get('http://localhost:8000/alunos')
        alunos = r_lista.json()
        self.assertFalse(any(aluno["id"] == aluno_id for aluno in alunos), "Aluno 5 ainda está na lista")

        print("11 OK")

    def test_012(self):
        #  editar o nome de um aluno
        r = requests.post('http://localhost:8000/alunos', json={"nome": "Filipe",
                                                                "data_nascimento":"2000-01-01",
                                                                "nota_primeiro_semestre":10.0,
                                                                "nota_segundo_semestre":5.0,
                                                                "turma_id":1})
        
        r = requests.put('http://localhost:8000/alunos/3', json={"nome": "Fabiano Silva"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado') 
        print("12 OK")

    def test_013(self):
       # tentar editar um aluno sem nome (erro)
        r = requests.put('http://localhost:8000/alunos/3', json={"id": 3})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("13 OK")

    def test_014(self):
        # tenta editar um aluno que nao existe
        r = requests.put('http://localhost:8000/alunos/100', json={"nome": "Novo Nome"})
        self.assertEqual(r.status_code, 400)  
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')  
        print("14 OK")
        
     # TESTE EXTRA------------------------------------------------------------------------------------
    def test_015(self):
        #criar aluno sem nome (erro)

        aluno_data = {"id": 6}
        r = requests.post('http://localhost:8000/alunos', json=aluno_data)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')
        print("15 OK")

    



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)



if __name__ == '__main__':
    unittest.main()
