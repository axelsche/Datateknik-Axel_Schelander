def arithmetic_series_sum(a1, d, n):
    # Calculate the sum of the arithmetic series
    series_sum = n * (2 * a1 + (n - 1) * d) / 2
    return series_sum

# Example usage:
a1 = 1.0  # First term (float)
d = 2.0   # Common difference (float)
n = 5.0   # Number of terms (float)

result = arithmetic_series_sum(a1, d, n)
print("Sum of the arithmetic series:", result)