# def add(a, b):
#     return a + b
#
# operation = add
#
# print(f'Result {operation(2,3)}')
#
# def handle_get(request):
#     return 'GET Response'
#
# def handle_post(request):
#     return 'POST Response'
#
# routers = {
#     'GET': handle_get,
#     'POST': handle_post
# }
#
# def process_request(method, request):
#     handler = routers.get(method)
#     if handler:
#         return handler(request)
#
#     return '405 Method Not Allowed'
#
# print(process_request('GET', {}))
# print(process_request('POST', {}))
# print(process_request('PUT', {}))

# def process_list(data):
#     def is_positive(x):
#         return x > 0
#     return [x for x in data if is_positive(x)]
# numbers = [5, -3, 0, 10]
# print(process_list(numbers))

# def process_user_input(input_data):
#     def validate(field, value):
#         if not value:
#             raise ValueError(f'Поле {field} не може бути порожнім')
#         return value.strip()
#
#
#     process_data = {}
#     for field, value in input_data.items():
#         process_data[field] = validate(field,value)
#     return process_data
#
# user_data = {'username': 'bob', 'email': 'bob@example.com'}
# print(process_user_input(user_data))

# def apply_operation(a, b, operation):
#     return operation(a,b)
#
# def subtract(a,b):
#     return a - b
#
# print(apply_operation(10, 4, subtract))


# def filter_records(records, criteria_func):
#     return [record for record in records if criteria_func(record)]
#
# def is_active_user(user):
#     return user.get('active', False)
#
# users = [
#     {'id': 1, 'name': 'Bob', 'active': False},
#     {'id': 2, 'name': 'Alice', 'active': True},
#     {'id': 3, 'name': 'Peter', 'active': True},
# ]
#
# active_users = filter_records(users,is_active_user)
# print(active_users)


# def greeting_factory(greeting):
#     def greet(name):
#         return f'{greeting}, {name}'
#
#     return greet
#
# say_hello = greeting_factory('Hello')
# say_how_are_you = greeting_factory('How are you?')
# print(say_hello('Bob'))
# print(say_how_are_you('Bob'))
# print(say_hello('Alice'))
# print(say_how_are_you('Alice'))

# def error_handler_factory(logger):
#     def error_handler(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 logger.error(f'Error in {func.__name__}: {e}')
#                 return None
#         return wrapper
#     return error_handler
#
# class SimpleLogger:
#     def error(self, message):
#         print(f'[ERROR] {message}')
#
# logger = SimpleLogger()
# handle_error = error_handler_factory(logger)
#
# @handle_error
# def process_order(order):
#     if order.get('amount', 0) <= 0:
#         raise ValueError('Amount <= 0')
#     return 'Order processed'
# print(process_order({'amount': 10}))
# print(process_order({'amount': -5}))


# def rate_limited(limit):
#     calls = 0
#     def decorator(func):
#         nonlocal calls
#         def wrapper(*args, **kwargs):
#             nonlocal calls
#             if calls >= limit:
#                 raise Exception('Rate limit exceeded')
#             calls += 1
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @rate_limited(3)
# def api_request(endpoint):
#     return f'Response from {endpoint}'
#
# print(api_request('/data'))
# print(api_request('/status'))
# print(api_request('/info'))
# try:
#     print(api_request('/extra'))
# except Exception as e:
#     print('Error 404')

# from time import sleep
# def simple_cache(func):
#     cache = {}
#     def wrapper (*args):
#         nonlocal cache
#         if args in cache:
#             print('[CACHE] Повертаємо кешований результат')
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
#     return wrapper
#
# @simple_cache
# def slow_func(x):
#     print('Обчислюємо результат... ')
#     return x ** x
#
# @simple_cache
# def slow_func2(x):
#     for i in range(1,5):
#         print('Sleep')
#         sleep(1)
#     return 2**x
# print(slow_func2(100))
# print(slow_func2(1000))
# print(slow_func2(1000))
# print(slow_func2(100))
# print(slow_func2(10))
# print('Result', slow_func(4))
# print('Result', slow_func(5))
# print('Result', slow_func(5))
# print('Result', slow_func(4))

# def require_admin(func):
#     def wrapper(user, *args, **kwargs):
#         if user.get('role') != 'admin':
#             raise PermissionError('Доступ заборонено: тільки для адміну')
#         return func(user, *args, **kwargs)
#     return wrapper
#
#
# @require_admin
# def delete_user(user, user_id):
#     return f'User {user_id} delete'
#
# admin = {'name': 'Alice', 'role': 'admin'}
# regular_user = {'name': 'Bob', 'role': 'user'}
#
# print(f'Delete {delete_user(admin, 42)}')
# print(f'Delete {delete_user(regular_user, 42)}')

import time
from time import sleep


def ttl_cache(ttl):
    cache = {}
    def decorator(func):
        nonlocal cache
        def wrapper(*args, **kwargs):
            nonlocal cache
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl:
                    print('[CACHE]')
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator
@ttl_cache(ttl=5)
def get_data(x):
    print('Result...')
    return x * 10

print(f'Result: {get_data(3)}')
print('Waiting')
sleep(3)
print(f'Result: {get_data(3)}')
print(f'Result: {get_data(3)}')
print(f'Result: {get_data(3)}')
print(f'Result: {get_data(3)}')
print('Waiting')
sleep(3)