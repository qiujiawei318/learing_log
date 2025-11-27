def dec(func):
    print("装饰器执行了（函数定义阶段）")
    def wrapper():
        print("执行包装逻辑")
        func()
    return wrapper


@dec
def test():
    print("test 本体执行")


# print("----现在开始调用 test()----")
# test()
