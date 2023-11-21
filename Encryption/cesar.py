# plain text to encryption text using cesar method
text = input('Enter your text: ')
key = int(input('Enter your key: '))
encryption = ''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    if i in alphabet:
        position = alphabet.find(i)
        new_position = (position + key) % 26
        encryption += alphabet[new_position]
    else:
        encryption += i

print(encryption)

# encryption text to plain text using cesar method
text = input('Enter your text: ')
key = int(input('Enter your key: '))
encryption = ''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    if i in alphabet:
        position = alphabet.find(i)
        new_position = (position - key) % 26
        encryption += alphabet[new_position]
    else:
        encryption += i

print(encryption)
