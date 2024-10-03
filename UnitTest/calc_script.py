import logging


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Get divide {a} / {b}')
        return a / b
    except ZeroDivisionError as error:
        logging.error('Na null/NoZeroDivisiom', exc_info=True)
        return 0


# def add(a, b):
#     return a **2 + b**2
def sqrt(a):
    try:
        if a < 0:
            raise ValueError
        # при отсутсвии проверки на + значение извлечение квадратного корня будет работать
        result = a ** 0.5
        logging.info(f'SQRT-good {a}^0.5={result}')
        return result
    except ValueError as error:
        result = "This is a negative root"
        logging.error(f'{error}, no negative values under root', exc_info=True)
        return 0
    except TypeError as error:
        logging.error(f'{error},enter number? please', exc_info=True)
        return 0


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log'
                        , format='%(asctime)s | %(levelname)s | %(message)s')
    print(div(3, 4))
    print(div(3, 0))
    print(sqrt(4))
    print(sqrt(-1))
    print(sqrt('qwe'))
    # logging.debug('a')
    # logging.debug('j')
    # logging.warning('f')
    # logging.error('f')
    # logging.critical('a')
