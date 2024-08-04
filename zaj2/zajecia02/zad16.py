def zmien_wartosc(arg):
    if isinstance(arg, list):
       arg[0]='kalafior'
       return arg
    elif isinstance(arg, int):
        arg=65482652
        return arg
    else:
        return arg
