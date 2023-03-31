def main():
    while True:
        try:
            f = (input("Fraction: ")).split("/")
            p = (int(f[0])/int(f[1]))*100
            if f[1] != 0 and f[1] > f[0]:
                 break
        except (ValueError, ZeroDivisionError):
            pass
    if 0 <= p <= 1.0 :
        print("E")
    elif 99.0 <= p <= 100.0 :
        print("F")
    else:
        print(f"{round(p)}%")
if __name__=="__main__":
    main()