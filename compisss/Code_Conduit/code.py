def func(sen, k, t):
    if(k == 0):
        print("{}".format(t))
        return
    for i in range(0, len(sen)+1):
        func(sen[:i+1], t-i, i)


num = 123
sen = str(num)+""
for i in range(0, len(sen)+1):
    func(sen, "", i)
