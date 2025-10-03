def main(**kwargs):
    """Функция работающая с **kwargs."""

    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")


def mean(data):
    """Функция подсчета среднего арифметического."""

    return sum(data) / float(len(data))


if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0])