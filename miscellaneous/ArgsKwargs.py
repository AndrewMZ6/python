def myfunc(*args, **kwargs):

    print("args: ", args)
    print(type(args))  # args - это кортеж, его можно индексировать

    print("kwargs: ", kwargs)
    print(type(kwargs))  # kwargs - это словарь

    for o in range(len(kwargs)):
        print(kwargs[list(kwargs)[o]])

    #   Пример "листизации" словаря:
    #
    #   a = {'x':1, 'y':2, 'z':3}
    #   list(a)
    #   ['x', 'y', 'z']
    #   list(a)[0]
    #   'x'
    #   a [ list(a) [0] ]
    #   1
    #
    #   Так мы можем "индексировать" словарь


# >>> myfunc(1, 4.7, 'Hello World', x = 1, y = 2, z = 3)
#
# args:  (1, 4.7, 'Hello World')
# <class 'tuple'>
# kwargs:  {'x': 1, 'y': 2, 'z': 3}
# <class 'dict'>
# 1
# 2
# 3
