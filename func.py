def calculate_func(length: float, width: float) -> float:
    """
    обчислює плозу прямокутника

    :param length: довжина
    :param width: ширина
    :return: площац
    """
    if length <= 0 or width <= 0:
        raise ValueError("довжина і ширина повинні бути додатніми числами")
    return length * width
