def saskaitit(a, b):
    return a + b

def atnemt(a, b):
    return a - b

def main():
    a = 5
    b = 2
    result_saskaitit = saskaitit(a, b)
    result_atnemt = atnemt(a, b)
    
    print()
    print("Kalkulators - saskaita un atņem 2 skaitļus")
    print(f"Ja a ir {a} un b ir {b} tad saskaitot rezultāts ir {result_saskaitit}")
    print(f"Ja a ir {a} un b ir {b} tad atņemot rezultāts ir {result_atnemt}")
    print()
    
    
if __name__ == "__main__":
    main()