
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
    
    file.write("Деление")
    file.write(str(div(a, b)))
    file.write('\n')

def add( a, b ):
    return a + b

def mult( a, b ):
    return a * b

def sub( a, b ):
    return a - b

def div( a, b ):
    return a / b

if __name__ == "__main__":
    main()