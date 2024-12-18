def v(d):
    for i in range(3):
        if d["a"][i]:
            continue
        else:
            return False
    return True
d = {"a": [1,2,3]}
if v(d):
    print("yes")
else:
    print("no")