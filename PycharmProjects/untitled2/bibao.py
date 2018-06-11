def testFun():
    temp = [lambda x : x*i for i in range(4)]
    return temp

for everyLambda in testFun():
    print(everyLambda(2))
