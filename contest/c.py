

n = int(input())


if n != 0:

    last_el = int(input())
    print(last_el)
    for i in range(n - 1):
        el = int(input())

        if el != last_el:
            print(el)

        last_el = el
