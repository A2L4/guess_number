class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, original_text, shift, is_encrypt):
        new_text = ''
        original_text = original_text.lower()
        if is_encrypt is not True:
            shift = -shift
        for letter in original_text:
            if letter in self.alphabet:
                i = self.alphabet.index(letter)
                if (i + shift) > len(self.alphabet)-1:
                    test = i + shift - len(self.alphabet)
                    new_text += self.alphabet[test]
                else:
                    new_text += self.alphabet[i + shift]
            else:
                new_text += letter
        return new_text


cipher_master = CipherMaster()
print(cipher_master.process_text(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    original_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
