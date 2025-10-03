import os
def lower1(s):
    Result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            Result += chr(ord(c) + 32)
        else:
            Result += c
    return Result



if __name__ == "__main__": 
 print(lower1("BonJouR, j'Ai FaIM")) 
os.system("pause")  # Pour garder la console ouverte sous Windows 