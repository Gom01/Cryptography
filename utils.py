from enum import Enum
from Encode import xor, shift, vigenere
from Sender import message_to_array


class EncryptionMethod(Enum):
    NOTHING = 'nothing'
    XOR = 'xor'
    SHIFT = 'shift'
    VIGENERE = 'vigenere'


def frequency_analysis(message):
    res = {}

    for c in message:
        if c in res.keys():
            res[c] = res[c] + 1
        else:
            res[c] = 1
    return res

#print(frequency_analysis("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."))


def encrypt(array_message):
    is_input_ok = False
    
    while not is_input_ok:
        encryption_type = input('Choose an encryption method (shift, xor, vigenere) : ')
        is_input_ok = True

        if encryption_type == 'EncryptionMethod.XOR.value':
            xor_value = input('Choose xor value : ')
            if not xor_value.isnumeric():
                return ''
            return xor(array_message, int(xor_value))
        elif encryption_type == EncryptionMethod.SHIFT.value:
            shift_value = input('Choose shift value : ')
            if not shift_value.isnumeric():
                return ''
            return shift(array_message, int(shift_value))
        elif encryption_type == EncryptionMethod.VIGENERE.value:
            vigenere_key = input('Choose vigenere key : ')
            return vigenere(array_message, vigenere_key)
        else:
            print('Wrong input')
            is_input_ok = False

print(encrypt(message_to_array("Bonjour")))
