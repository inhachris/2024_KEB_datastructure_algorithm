def factorial(number) -> int :
    pass


def nCr(n, r) -> int :
    """
    조합 함수
    :param n: 전체 수
    :param r: 조합할 수
    :return: 경우의 수
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator


if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n, r)}")