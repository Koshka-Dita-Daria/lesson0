def test_function():
    def inner_function():
        def testing():
            print("Я в области видимости функции test_function")
    print("test")
test_function()
inner_function()
