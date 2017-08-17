with open('update.txt', 'r+') as file:
    text = file.read()
    print('\nString:', text)

    print('\nPosition In File Now:', file.tell())

    file.seek(35)
    print('Verify position in file now:', file.tell())
    file.write('Python File Handling')

    file.seek(55)
    file.write('Seek and Tell Methods')
    print('\nPosition In File Now:', file.tell())

    content = file.read()
    print('\nContent from the current position is :', content)

    file.seek(0)
    text = file.read()
    print('\nContent from the beginning of file is :', text)