letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
           'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def decrypt(txt):
    n = int(txt.split(':')[0])
    newtxt = ''
    for i in txt.lower():
        # if i in newLetters: newtxt += newLetters[i]
        if i in letters: newtxt += letters[letters.index(i)-n]
        else: newtxt += i
    return newtxt

def crypt(txt):
    n = int(txt.split(':')[0])
    newtxt = ''
    for i in txt.lower():
        # if i in newLetters: newtxt += newLetters[i]
        if i in letters:
            newtxt += letters[letters.index(i) + n]
        else:
            newtxt += i
    return newtxt
print('crypt: 1; decrypt: 2')
isCrypt = int(input())
print('text format "n: text"\n')
print(crypt(input()) if isCrypt==1 else decrypt(input()))
