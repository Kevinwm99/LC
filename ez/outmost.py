inp = list("(()())(())(()(()))") # -> ()(())
c = 0
stack = []
cn = 1
for i in inp:
    # if cn==7:print(c)
    if i == '(':
        c += 1
        if c > 1: stack.append(i)
    if i == ')':
        if c > 1:
            c -= 1
            stack.append(i)
        if c == 1:
            try:
                val = stack.pop()
                if i == val:  # )
                    stack.append(val)
                    c -= 1
                    cn += 1
                    continue
                else:
                    stack.append(val)
                    stack.append(i)
                    c -= 1
            except:
                stack.append(val)
                stack.append(i)
                c -= 1
    cn += 1

