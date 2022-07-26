import unittest

from py_secureapikeys_azumio.apikeys import SecureApiKeys

class Test(unittest.TestCase):

    def setUp(self):
        s = SecureApiKeys('azumio-com', 'global', 'azumio-ci-keyring',
                          'azumio-ci-key')
        self.sak = s

    def test_decrypt(self):
        decrypted = self.sak.decrypt_key(
            'CiQAXNSpP6wYjeVyD45EokdN3T0rivhcRriRHwyYHJIijqQ+RwUSVQBYNXPqpz4phz+ylZ7UFbRtKkg6V+O5t+Hxnbo0ng4oJ6OjKwUwibr1SkcrYLK7V5TdzZzzD7ATzQxjNrKyV68bYc2N949Ac9kd1IB9uxibSJGspVA='
        )
        self.assertEqual(decrypted,
                         'this is for testing purposes only (unittest)')

    def test_encrypted_cache(self):

        decrypted = self.sak.decrypt_key(
            'CiQAXNSpP6wYjeVyD45EokdN3T0rivhcRriRHwyYHJIijqQ+RwUSVQBYNXPqpz4phz+ylZ7UFbRtKkg6V+O5t+Hxnbo0ng4oJ6OjKwUwibr1SkcrYLK7V5TdzZzzD7ATzQxjNrKyV68bYc2N949Ac9kd1IB9uxibSJGspVA='
        )
        self.assertEqual(decrypted,
                         'this is for testing purposes only (unittest)')

        decrypted = self.sak.decrypt_key(
            'CiQAXNSpP6wYjeVyD45EokdN3T0rivhcRriRHwyYHJIijqQ+RwUSVQBYNXPqpz4phz+ylZ7UFbRtKkg6V+O5t+Hxnbo0ng4oJ6OjKwUwibr1SkcrYLK7V5TdzZzzD7ATzQxjNrKyV68bYc2N949Ac9kd1IB9uxibSJGspVA='
        )
        self.assertEqual(decrypted,
                         'this is for testing purposes only (unittest)')