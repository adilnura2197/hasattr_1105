class Simple:
    def info(self):
        print(f"Simple info")


class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def metod_1(self, obj):
        if hasattr(obj, 'info'):
            obj.info()

        else:
            print(f"Bu object yo'q")


obj = MyClass(40, 30)

s = Simple()
obj.metod_1(s)
