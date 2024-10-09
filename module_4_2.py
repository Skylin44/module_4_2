def test_function(*x):
    x = 1, 3
    def inner_function(*x):
        print(x)

    inner_function("Я в области видимости функции test_function")


test_function()
#inner_function()