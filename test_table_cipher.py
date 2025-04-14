import unittest
from table_cipher import TableCipher

class TestTableCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = TableCipher(key='KEYWORD')

    def test_encryption(self):
        plaintext = "HELLO WORLD"
        encrypted = self.cipher.encrypt(plaintext)
        self.assertGreater(len(encrypted), 2)
        self.assertNotIn(' ', encrypted)

    def test_decryption(self):
        plaintext = "HELLO WORLD"
        encrypted = self.cipher.encrypt(plaintext)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(plaintext.replace(" ", ""), decrypted)

    def test_table_size(self):
        cipher_4x4 = TableCipher(key='KEYWORD', size=4)
        plaintext = "HELLO WORLD"
        encrypted = cipher_4x4.encrypt(plaintext)
        decrypted = cipher_4x4.decrypt(encrypted)
        self.assertEqual(plaintext.replace(" ", ""), decrypted)

if __name__ == "__main__":
    unittest.main()