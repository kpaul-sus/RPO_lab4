
def main():
    file = open('result.txt', 'w')
    a = int(input("Введите первый операнд: "))
    b = int(input("Введите второй операнд: "))
    print("Сложение")
    file.write(str(add(a, b)))
    

def add( a, b ):
    res = a + b
    return res

if __name__ == "__main__":
    main()