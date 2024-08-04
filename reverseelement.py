def reverse_array(arr):
  """Reverses an array of integer values.

  Args:
    arr: The array to reverse.

  Returns:
    The reversed array.
  """
  return arr[::-1]

# Example usage:
my_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(my_array)
print(reversed_array)