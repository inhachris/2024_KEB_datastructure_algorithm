# def factorial(number) -> int :
#     '''
#     factorial by repetition
#     :param number: number (int)
#     :return: factorial result (int)
#     '''
#     result = 1
#     for i in range(1, number + 1):
#         result = result * i
#     return result


def factorial(number) -> int:
    '''
    factorial by recursion
    :param number: number (int)
    :return: factorial result (int)
    '''
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def nCr(n, r) -> int :
    """
    combination function
    :param n: 전체 수
    :param r: 조합할 수
    :return: 경우의 수
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)