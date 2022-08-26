from ast import arg
import re 
#same purpose as main.py but it can add and subtract between 0 and 2 billion
def special_match(strg, search=re.compile(r'[^x]').search):     
    return not bool(search(strg))
def GetNumber(number):
    if special_match(number):
        return len(number)
    else:
        return "Invalid"
def GetX(number):
    output = ""
    for i in range(number):
        output += "x"
    return output
def Add(*args):
    output = ""
    for i in args:
        output += i
    return GetNumber(output)
def Subtract(*args):
    output = ""
    index = 0
    length = ""
    temp = 0
    for i in args:
        if Mod(GetX(len(args)), "xx") != 0:
            break
        temp = len(args[Add(GetX(index), "x")])
        for j in range(temp):
            length += "x"
        while True:
            if len(length) == 0:
                break
            i = i[1:]
            length = length[1:]
        output += i
        index = Add(GetX(index), "x")
        args = args[:1]
    return GetNumber(output)
def Multiply(*args):
    output = ""
    for i in range(Subtract(GetX(len(args)), "x")):
        for j in range(Add(args[Add(GetX(i), "x")], "x")):
            if j == 0:
                continue
            output += args[i]
    return GetNumber(output)
def Divide(*args):
    output = ""
    index = 1
    temp = ""
    for i in range(Subtract(GetX(len(args)), "x")):
        temp = args[Add(GetX(i), "x")]
        while temp != args[i] and int(GetNumber(temp)) < int(GetNumber(args[i])):
            temp += args[Add(GetX(i), "x")]
            index = Add(GetX(index), "x")
        output += GetX(index)
        temp = ""
    return GetNumber(output)
def Mod(*args):
    output = ""
    index = 1
    temp = ""
    temp2 = ""
    for i in range(GetNumber(GetX(len(args))[:1])):
        temp = args[Add(GetX(i), "x")]
        while temp != args[i] and int(GetNumber(temp)) < int(GetNumber(args[i])):
            temp += args[Add(GetX(i), "x")]
            index = Add(GetX(index), "x")
        while GetNumber(temp) > GetNumber(args[i]):
            temp = temp[int(GetNumber(args[Add(GetX(i), "x")])):]
        index = 0
        while temp != args[i]:
            temp = GetX(Add(temp, "x"))
            index = Add(GetX(index), "x")
        output += GetX(index)
        temp = ""
    return GetNumber(output)
def AddNum(*args):
    output = 0
    for i in range(len(args) - 1):
        output += Add(GetX(args[i]), GetX(args[i+1]))
    return output
def SubtractNum(*args):
    output = 0
    for i in range(len(args) - 1):
        output += Subtract(GetX(args[i]), GetX(args[i+1]))
    return output
def MultiplyNum(*args):
    output = 0
    for i in range(len(args) - 1):
        output += Multiply(GetX(args[i]), GetX(args[i+1]))
    return output
def DivideNum(*args):
    output = 0
    for i in range(len(args) - 1):
        output += Divide(GetX(args[i]), GetX(args[i+1]))
    return output
def ModNum(*args):
    output = 0
    for i in range(len(args) - 1):
        output += Mod(GetX(args[i]), GetX(args[i+1]))
    return output
print(AddNum(2, 2))