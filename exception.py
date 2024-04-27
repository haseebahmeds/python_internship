def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except valueError:
        print("value error")
    finally:
        print("funn")         