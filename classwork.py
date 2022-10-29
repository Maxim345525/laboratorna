def(stroke, digit):
    res = re.findall(f'{digit}', stroke)
    print(len(res))