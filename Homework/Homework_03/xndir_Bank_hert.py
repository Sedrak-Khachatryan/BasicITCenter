a = 0  # hertum mardkanc skzbnakan tiv
while True:
    print("Հերթում սպասող մարդկանց քանակ: 1 \nՀերթի ամրագրում: 2 \nՀերթի չեղարկում: 3 \nԵլք ծրագրից: 0")
    try:
        i = int(input())
        if i == 0:
            break
    except ValueError:
        print("Մուտքագրեք թիվ")
    try:
        i = int(input())
        if i == 2:
            a = a + 1
    except ValueError:
        print("Մուտքագրեք թիվ")

    try:
        i = int(input())
        if i == 3:
            a = a - 1
    except ValueError:
        print("Մուտքագրեք թիվ")

    try:
        i = int(input())
        if i == 1:
            print("Ձեր հերթի համարն է ՝" + str(a))
    except ValueError:
        print("Մուտքագրեք թիվ")



