import tishon

while True:
    text = input('Tishon > ')
    result, error = tishon.run('<stdin>', text)

    if error: 
        print(error.as_string())
    else:
        print(result)
        