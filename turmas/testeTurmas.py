import requests
import unittest

class TestStringMethods(unittest.TestCase):  
    
    def teste_1_get_turmas_lista(self):
        resp = requests.get('http://localhost:5000/turmas')
        if resp.status_code == 404:
            self.fail("pagina /turmas não encontrada")

        try:
            retorno = resp.json()
        except:
            self.fail("retorno não saiu como json")

        self.assertEqual(type(retorno),type([]))
        print("1 OK")


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    unittest.main()
    unittest.main()


