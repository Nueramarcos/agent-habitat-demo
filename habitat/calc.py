"""Calculator helpers — intentional bugs for agent-habitat-demo."""


def sum_range(start: int, end: int) -> int:
    """Sum integers from start through end inclusive."""
    if start > end:
        start, end = end, start
    # Fix off-by-one error by using end instead of end-1
    return sum(range(start, end + 1))


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards."""
    cleaned = "".join(ch for ch in text if ch.isalnum())
    # Fix case-sensitive palindrome check by normalizing with .lower()
    return cleaned.lower() == cleaned[::-1].lower()


def clamp(value: float, low: float, high: float) -> float:
    """Clamp value to [low, high]."""
    # Swap bounds when low > high
    if low > high:
        low, high = high, low
    if value < low:
        return low
    if value > high:
        return high
    return value
