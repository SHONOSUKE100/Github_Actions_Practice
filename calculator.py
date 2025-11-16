"""Simple arithmetic utilities for demonstration purposes."""

def average(values: list[float]) -> float:
    """Return the arithmetic mean of the provided numeric values.

    Raises:
        ValueError: If ``values`` is empty, because the average would be undefined.
    """
    if not values:
        raise ValueError("values must contain at least one number")
    return sum(values) / len(values)
