# реализовать метакласс.позволяющий создавать всегда один и тот же объект класса

# Создаем метакласс
class MyMetaClass(type):
    # зададити объекту неопределенное значение
    obj = None
    # делаем перегрузку метода определяющего создание новых экземпляров объктов
    # пользовательского класса
    def __call__(self):
        # если еще не создано ни одгого экземпляра класса, создадим его
        if self.obj is None:
            self.obj = type.__call__(self)
        # иначе возвращаем созданый экземпляр
        return self.obj


class My_Class(metaclass=MyMetaClass):
    pass

obj_1 = My_Class()
obj_2 = My_Class()
print(obj_1 is obj_2)