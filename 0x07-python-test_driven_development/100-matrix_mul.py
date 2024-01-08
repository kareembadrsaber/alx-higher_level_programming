#!/usr/bin/python3
def matrix_mul(m_a, m_b):
   """Return the matrix resulting of
   the multiplication of m_a and m_b."""

   if not all(isinstance(x, list) for x in m_a):
       raise TypeError("m_a must be a list of lists")
   if not all(isinstance(x, list) for x in m_b):
       raise TypeError("m_b must be a list of lists")

   if not m_a or not m_b:
       raise ValueError("Neither m_a nor m_b can be empty")

   if not all(all(isinstance(x, (int, float)) for x in row) for row in m_a):
       raise TypeError("All elements in m_a should be integers or floats")
   if not all(all(isinstance(x, (int, float)) for x in row) for row in m_b):
       raise TypeError("All elements in m_b should be integers or floats")

   if len(m_a[0]) != len(m_b):
       raise ValueError("The number of columns in m_a must match the number of rows in m_b")

   result = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*m_b)] for X_row in m_a]

   return result
