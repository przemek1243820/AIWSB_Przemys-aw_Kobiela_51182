a = 3
b = 2
c = 3
if a == b and c != a:
    print("Liczby a i b są równe")
elif b == c and a != b:
    print("Liczby b i c są równe")
elif a == c and b != a:
    print("Liczby a i c są równe")
elif a != b and b != c and a != c:
    print("nie ma równych liczb")
elif a == b and b == c and c == a:
    print("wszystkie są równe")