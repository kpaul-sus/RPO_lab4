
def main():
    file = open('result.txt', 'w')
    a = int(input("Введите первый операнд: "))
    b = int(input("Введите второй операнд: "))

    file.write("Сложение\n")
    file.write(str(add(a, b)))
    file.write('\n')
    
    file.write("Вычитание\n")
    file.write(str(sub(a, b)))
    file.write('\n')
    

def add( a, b ):
    res = a + b
    return res

def sub( a, b ):
    return a - b

if __name__ == "__main__":
    main()