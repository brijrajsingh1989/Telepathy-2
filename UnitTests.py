from urllib import response


try:
    import unittest
    from server import app
    import json
    
except Exception as e:
    print('Some modules are missing {} '.format(e))

class APITest(unittest.TestCase):
    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/Ping')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_null_data(self):
        tester = app.test_client(self)
        data = {}
        result = tester.post('/EvaluateExpression',data=json.dumps(data))
        self.assertEqual(result.data, b'{"error":"expression not found"}\n')

if __name__ == '__main__':
    unittest.main()
