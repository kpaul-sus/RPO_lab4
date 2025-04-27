
def main():
    file = open('result.txt', 'w')
    a = int(input("Введите первый операнд: "))
    b = int(input("Введите второй операнд: "))

    print("Сложение")
    file.write(str(add(a, b)))
    file.write('\n')

    print("Умножение")
    file.write(str(mult(a, b)))
    file.write('\n')
    

def add( a, b ):
    res = a + b
    return res

def mult( a, b ):
    res = a * b
    return res

if __name__ == "__main__":
    main()