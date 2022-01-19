from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    自定义异常函数
    exc: 异常实例对象，发生异常实例化出来的
    context: 字典，异常，解析器的记忆
    """
    response = exception_handler(exc, context)
    if response is None:
        if isinstance(exc, ZeroDivisionError):
            return Response({"detail": "0 不能作为函数", "status": status.HTTP_500_INTERNAL_SERVER_ERROR})
