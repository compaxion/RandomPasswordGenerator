import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))

lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
lowercaseLetter3 = chr(random.randint(97, 122))

digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
digit3 = chr(random.randint(48,57))

punctuationSign1 = chr(random.randint(33,152))
punctuationSign2 = chr(random.randint(33,152))
punctuationSign3 = chr(random.randint(33,152))

password = (uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 +
            lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 +
            digit1 + digit2 + digit3 +
            punctuationSign1 + punctuationSign2 + punctuationSign3)

password = shuffle(password)

print(password)
