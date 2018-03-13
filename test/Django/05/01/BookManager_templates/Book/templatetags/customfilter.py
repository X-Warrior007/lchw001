from django.template import Library

# 注册对象：注册过滤器的对象 （注意点：注册对象必须叫做register）
register = Library()

# 获取过滤器装饰器filter，使用filter装饰mod函数
@register.filter
def mod(num):
    """判断奇偶数:num是外接传入的数字"""
    return num%2 # 得到的结果，0 / 1, 非零即真


# 获取过滤器装饰器filter，使用filter装饰mod函数
@register.filter
def mod1(num1, num2):
    """判断奇偶数:num1是外接传入的模板变量"""
    return num1%num2 # 得到的结果，0 / 1, 非零即真