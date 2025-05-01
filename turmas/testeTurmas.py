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
        self.assertEqual(resp.json()["error"], 'Turma não encontrada')  
        print("3 OK")
'''
    # Testes POST /turmas
    def teste_4_post_turma_criacao(self):
        nova_turma = {"nome": "Turma Nova", "curso": "Python"}
        resp = requests.post('http://localhost:8000/turmas', json=nova_turma)
        
        self.assertEqual(resp.status_code, 201)
        self.assertIn('id', resp.json())
        print("4 OK - POST /turmas criação")
    
    def teste_5_post_turma_dados_incompletos(self):
        turma_incompleta = {"nome": "Turma Incompleta"}
        resp = requests.post('http://localhost:8000/turmas', json=turma_incompleta)
        
        self.assertEqual(resp.status_code, 400)
        print("5 OK - POST /turmas dados incompletos")
    
    def teste_6_post_turma_dados_vazios(self):
        turma_vazia = {}
        resp = requests.post('http://localhost:8000/turmas', json=turma_vazia)
        
        self.assertEqual(resp.status_code, 400)
        print("6 OK - POST /turmas dados vazios")
    
    # Testes PUT /turmas/<id>
    def teste_7_put_turma_atualizacao(self):
        # Cria turma para testar
        nova_turma = {"nome": "Turma para Atualizar", "curso": "PUT Test"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        dados_atualizacao = {"nome": "Turma Atualizada", "curso": "PUT Sucesso"}
        resp = requests.put(f'http://localhost:8000/turmas/{id_turma}', json=dados_atualizacao)
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['nome'], "Turma Atualizada")
        print("7 OK - PUT /turmas/<id> atualização")
    
    def teste_8_put_turma_inexistente(self):
        dados_atualizacao = {"nome": "Turma Inexistente", "curso": "Erro"}
        resp = requests.put('http://localhost:8000/turmas/999999', json=dados_atualizacao)
        
        self.assertEqual(resp.status_code, 404)
        print("8 OK - PUT /turmas/<id> inexistente")
    
    def teste_9_put_turma_dados_invalidos(self):
        # Cria turma para testar
        nova_turma = {"nome": "Turma para PUT inválido", "curso": "Teste"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        dados_invalidos = {"nome": ""}  # Nome vazio inválido
        resp = requests.put(f'http://localhost:8000/turmas/{id_turma}', json=dados_invalidos)
        
        self.assertEqual(resp.status_code, 400)
        print("9 OK - PUT /turmas/<id> dados inválidos")
    
    # Testes DELETE /turmas/<id>
    def teste_10_delete_turma_existente(self):
        # Cria turma para testar
        nova_turma = {"nome": "Turma para Deletar", "curso": "DELETE Test"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        resp = requests.delete(f'http://localhost:8000/turmas/{id_turma}')
        self.assertEqual(resp.status_code, 204)
        print("10 OK - DELETE /turmas/<id> existente")
    
    def teste_11_delete_turma_inexistente(self):
        resp = requests.delete('http://localhost:8000/turmas/999999')
        self.assertEqual(resp.status_code, 404)
        print("11 OK - DELETE /turmas/<id> inexistente")
    
    # Testes adicionais de consistência
    def teste_12_consistencia_apos_delete(self):
        # Cria e depois deleta uma turma
        nova_turma = {"nome": "Turma Consistência", "curso": "Teste"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        requests.delete(f'http://localhost:8000/turmas/{id_turma}')
        resp_get = requests.get(f'http://localhost:8000/turma/{id_turma}')
        self.assertEqual(resp_get.status_code, 404)
        print("12 OK - Consistência após DELETE")
    
    def teste_13_lista_apos_criacao(self):
        # Verifica se a turma criada aparece na lista
        nova_turma = {"nome": "Turma Lista", "curso": "Lista Test"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        resp_get = requests.get('http://localhost:8000/turmas')
        turmas = resp_get.json()
        turmas_ids = [turma['id'] for turma in turmas]
        self.assertIn(id_turma, turmas_ids)
        print("13 OK - Turma criada aparece na lista")
    
    def teste_14_atualizacao_parcial(self):
        # Testa atualização parcial (apenas um campo)
        nova_turma = {"nome": "Turma Parcial", "curso": "Parcial"}
        resp_post = requests.post('http://localhost:8000/turmas', json=nova_turma)
        id_turma = resp_post.json()['id']
        
        dados_parciais = {"curso": "Parcial Atualizado"}
        resp_put = requests.put(f'http://localhost:8000/turmas/{id_turma}', json=dados_parciais)
        
        self.assertEqual(resp_put.status_code, 200)
        resp_get = requests.get(f'http://localhost:8000/turma/{id_turma}')
        self.assertEqual(resp_get.json()['curso'], "Parcial Atualizado")
        print("14 OK - Atualização parcial")
    
'''
def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()