import random
import string

class TableCipher:
    def __init__(self, key: str, size: int = 6):
        self.key = key
        self.size = size
        self.alphabet = self._generate_alphabet()

    def _generate_alphabet(self):
        unique_key = "".join(sorted(set(self.key), key=self.key.index))
        remaining_letters = "".join(sorted(set(string.ascii_uppercase) - set(unique_key)))
        return unique_key + remaining_letters

    def _create_table(self, text: str):
        table = [["" for _ in range(self.size)] for _ in range(self.size)]
        idx, direction = 0, 1 

        for row in range(self.size):
            if direction == 1:  
                for col in range(self.size):
                    table[row][col] = text[idx] if idx < len(text) else random.choice(self.alphabet)
                    idx += 1
            else: 
                for col in range(self.size - 1, -1, -1):
                    table[row][col] = text[idx] if idx < len(text) else random.choice(self.alphabet)
                    idx += 1
            direction *= -1 

        return table

    def encrypt(self, plaintext: str) -> str:
        plaintext = plaintext.upper().replace(" ", "")
        text_length = len(plaintext) 
        table = self._create_table(plaintext)
        ciphertext = "".join(table[row][col] for col in range(self.size) for row in range(self.size))
        return f"{text_length:02d}{ciphertext}" 

    def decrypt(self, ciphertext: str) -> str:
        text_length = int(ciphertext[:2]) 
        ciphertext = ciphertext[2:] 

        table = [["" for _ in range(self.size)] for _ in range(self.size)]
        idx = 0

        for col in range(self.size):
            for row in range(self.size):
                table[row][col] = ciphertext[idx]
                idx += 1

        plaintext = []
        direction = 1  
        for row in range(self.size):
            if direction == 1:
                plaintext.extend(table[row])
            else:
                plaintext.extend(reversed(table[row]))
            direction *= -1  

        return "".join(plaintext)[:text_length]  
    

cipher = TableCipher("KEYWORD")
message = "HELLO WORLD"
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print(f"Message: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")