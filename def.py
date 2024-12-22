def calculate_total(prices: list[float]) -> float:
    """
    розраховує загальну суму, списку цін.
    :param prices: список цін товарів.
    :return: загальна сума цін.
    """
    return sum(prices)

def get_tems(items: list[str]) -> list[str]:
    """
    повертає список, де кожен елемент повторюється лише раз
    :param items: список рядків.
    :return: список унікальних рядків.
    """
    return list(set(items))

def enough_money(budget: float, price: float) -> bool:
    """
    перевіряє, чи достатньо бюджету для покупки товару.
    :param budget: бюджет людини.
    :param price: Ціна товару.
    :return: True, якщо вистачає бюджету, False інакше.
    """
    return budget >= price
