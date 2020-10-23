# Decorator is a construct that adds functionality to the existing code. This is also called as meta-programming

def enable_debug(is_debug):
    def decorator(my_fun):
        def wrapper(*args):
            import logging
            logging_level = logging.DEBUG if (is_debug) else logging.INFO
            logging.basicConfig(level=logging_level)
            print("%"*50)
            print(f"DEBUG mode: {is_debug}")
            logging.debug(f"input arguments: {args}")
            for arg in args:
                logging.debug(f"arg: {arg} type: {type(arg)}")   
            print("%"*50)
            result = my_fun(*args)
            logging.info(f"input: {args}")
            logging.info(f"output: {result}")
            print("%"*50)
            return result
        return wrapper
    return decorator

@enable_debug(False)
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

add(5, 6)