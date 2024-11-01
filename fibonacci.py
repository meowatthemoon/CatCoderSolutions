def fibbonaci(number):
    if number == 0:
        return 0
    
    if number == 1:
        return 1
    
    return fibbonaci(number - 2) + fibbonaci(number - 1)

if __name__ == '__main__':
    number = int(input("Input:"))
    output = fibbonaci(number = number)
    print(output)
