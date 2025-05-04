import requests
import unittest

class TestStringMethods(unittest.TestCase):  
    
    def teste_1_get_turmas_lista(self):
        r = requests.get('http://localhost:8000/turmas')
        self.assertEqual(r.status_code, 200)
        turmas = r.json()
        self.assertIsInstance(turmas, list)
        print("1 OK")



    def teste_2_get_turma_por_id_existente(self):
        # Primeiro cria uma turma para testar
        r = requests.get('http://localhost:8000/turmas/1')
        self.assertEqual(r.status_code, 200)
        turma = r.json()
        self.assertEqual(turma['id'], 1)
        print("2 OK")
 
    def teste_3_get_turma_por_id_inexistente(self):
        resp = requests.get('http://localhost:8000/turmas/999999')
        self.assertEqual(resp.status_code, 400)  
        self.assertEqual(resp.json()["erro"], 'Turma não encontrada')  
        print("3 OK")

    # Testes POST /turmas
    def teste_4_post_turma_criacao(self):
        nova_turma = {
            "descricao": "API",
            "ativo": True,
            "professor_id": 1
        }
        resp = requests.post('http://localhost:8000/turmas', json=nova_turma)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('professor_id', resp.json())
        print("4 OK")

    def teste_5_post_turma_dados_incompletos(self):
        turma_incompleta = {"nome": "Turma Incompleta"}
        resp = requests.post('http://localhost:8000/turmas', json=turma_incompleta)
        
        self.assertEqual(resp.status_code, 400)
        print("5 OK")

    def teste_6_post_turma_dados_vazios(self):
        turma_vazia = {}
        resp = requests.post('http://localhost:8000/turmas', json=turma_vazia)
        
        self.assertEqual(resp.status_code, 400)
        print("6 OK")

    # Testes PUT /turmas/<id>
    def teste_7_put_turma_atualizacao(self):
        # Cria turma para testar
        nova_turma = {
            "descricao": "Banco de Dados",
            "ativo": True,
            "professor_id": 1
        }
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        dados_atualizacao = {"descricao": "Linguagem SQL", "ativo": True, "professor_id": 1}
        resp = requests.put(f'http://localhost:8000/turmas/{id_turma}', json=dados_atualizacao)
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['descricao'], "Linguagem SQL")
        print("7 OK")
  
    def teste_8_put_turma_inexistente(self):
        dados_atualizacao = {
            "descricao": "Sem materia",
            "ativo": True,
            "professor_id": 1
        }
        resp = requests.put('http://localhost:8000/turmas/999999', json=dados_atualizacao)
        
        self.assertEqual(resp.status_code, 400)
        print("8 OK")

   
    # Testes DELETE /turmas/<id>
    def teste_10_delete_turma_existente(self):
        # Cria turma para testar
        nova_turma = {
            "descricao": "DEVOPS",
            "ativo": True,
            "professor_id": 1
        }
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        resp = requests.delete(f'http://localhost:8000/turmas/{id_turma}')
        self.assertEqual(resp.status_code, 204)
        print("10 OK")


    

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()