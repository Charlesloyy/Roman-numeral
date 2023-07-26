import re
import numpy as np
class RomanNumeral:
    def __init__(self):
        self.my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    def convert(self, s):
        t = []
        if re.findall(r'IV\w*',s):
            i = 4
            t.append(i)
            s = s.replace("IV", "")

        if re.findall(r'IX\w*',s):
            i = 9
            t.append(i)
            s = s.replace("IX", "")

        if re.findall(r'XL\w*',s):
            i = 40
            t.append(i)
            s = s.replace("XL", "")

        if re.findall(r'XC\w*',s):
            i = 90
            t.append(i)
            s = s.replace("XC", "")

        if re.findall(r'CD\w*',s):
            i = 400
            t.append(i)
            s = s.replace("CD", "")

        if re.findall(r'CM\w*',s):
            i = 900
            t.append(i)
            s = s.replace("CM", "")
        t = np.array(t)
        t = np.sum(t)

        p = []
        l = [i[1] for i in enumerate(s)]
        for i in l:
            p.append(self.my_dict[i])

        p = np.array(p)
        p = np.sum(p)
        output = p + t
        return int(output)

        

s = input("Enter Roman Figure: ")

roman = RomanNumeral()
print(roman.convert(s.upper()))
        
