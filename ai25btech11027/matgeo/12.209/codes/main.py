import sympy as sp

# Define symbols
a, b, c, d, alpha, beta = sp.symbols('a b c d alpha beta', real=True)
i = sp.I  # imaginary unit

# Define the matrix
M = sp.Matrix([
    [a * sp.exp(i * alpha), b],
    [c * sp.exp(i * beta),  d]
])

# Compute the conjugate transpose (Hermitian adjoint)
M_conj_transpose = M.conjugate().T

# Compute the inverse directly
M_inverse = M.inv()

print("M =")
sp.pprint(M)
print("\nM_conjugate_transpose =")
sp.pprint(M_conj_transpose)
print("\nM_inverse =")
sp.pprint(M_inverse)

# Verify if M is unitary (M * M† = I)
print("\nIs M unitary?")
sp.pprint(sp.simplify(M * M_conj_transpose))

