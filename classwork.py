def(stroke):
    letters = [i for i in stroke if i.isalpha()]
    digitsd = [i for i in stroke if i.isdigit()]
    print(f'''
    Letters = {len(letters)}
    Digits = {len(digits)}
    ''')