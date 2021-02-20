
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i


def Decrypt():
    print("You have chosen to decrypt.")
    print("Please insert the Message:")
    message = input()
    translated = ''

    f = open("The Illiad of Homer.txt", "r")
    fileLenght = file_len("The Illiad of Homer.txt")
    key = ''
    messageLenght = len(message)
    keyList = []

    message = message.split("fin", 1)[0]
    counter = message.split("fin", 1)[1] #This is what I couldn't get around. Even though further down I did try it in the enrypt whether it worked and it did.


    for i, line in enumerate(f):
        if i >= counter:

            for character in line:
                keyList.append(ord(character))

            keyListLenght = len(keyList)
            keyListCounter = 0

    for symbol in message:
        num = ord(symbol)

        if keyListCounter < keyListLenght:
            num -= keyList[keyListCounter]
            keyListCounter += 1

        if num > ord('~'):
            num -= 95
        if num < ord(' '):
            num += 95

        translated += chr(num)

    print(translated)

def Encrypt():
    print("You have chosen to encrypt.")
    print("Please insert your Message:")
    message = input().lower()
    translated = ''

    c = open("counter.txt", "r+")
    line = c.readlines()
    counter = int(line[0])
    begginingCounter = counter

    f = open("The Illiad of Homer.txt","r")

    fileLenght = file_len("The Illiad of Homer.txt")
    key = ''
    messageLenght = len(message)
    keyList = []

    for i, line in enumerate(f):
        if i >= counter:

            for character in line:
                keyList.append(ord(character))

            keyListLenght = len(keyList)
            keyListCounter = 0
            counter += 1
            if keyListLenght > messageLenght+1:
                deleteContent(c)
                c.write('%d' % counter)
                c.close()
                break

        elif i > fileLenght:
            print("New SourceCrypt needed.")
            break



    for symbol in message:
        num = ord(symbol)

        if keyListCounter < keyListLenght:
            num += keyList[keyListCounter]
            keyListCounter += 1

        if num > ord('~'):
            num -= 95
        if num < ord(' '):
            num += 95

        translated += chr(num)

    translated += 'fin' + str(begginingCounter)
    print(translated)
    '''
    counter = translated.split("fin", 1)[1]
    print(counter)
    '''
    # here Ive demonstrated that the .split() does take away the line at the end signifying the counter at which the decrypt would start
    # but for some reason this same thing does not work in the decrypt


def Main():
    print("Hello User, what  would you like to do?")
    print("Decrypt-d or Encrypt-e")
    choice = input().lower()

    if choice in 'encrypt e'.split():
        Encrypt()
    elif choice in 'decrypt d'.split():
        Decrypt()
    else:
        print("Something went wrong")


if __name__ == "__main__":
    Main()