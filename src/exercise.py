def main():
    #write your code below this line
    sum = 0
    while True:
        num = int(input("Give a number:"))
        if (num != 0):
            sum += num
        else:
            break
    print("Sum of numbers: " + str(sum))

if __name__ == '__main__':
    main()
