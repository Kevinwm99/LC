dit = {1:1,2:1,3:2,4:3}
res =[]
key =4
if res==[]:
    res.append(key)
    res.append(dit[key])
key = dit[key]
while key != dit[key]:
    key = dit[key]
    res.append(key)