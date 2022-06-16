def cobb_douglas(K, L):

    # Create alpha and z
    z = 1
    alpha = 0.33

    return z * K**alpha * L**(1 - alpha)


print(cobb_douglas(1.0, 0.5))


def returns_to_scale(K, L, gamma):
    y1 = cobb_douglas(K, L)
    y2 = cobb_douglas(gamma*K, gamma*L)
    y_ratio = y2 / y1
    return y_ratio / gamma


print(returns_to_scale(1.0, 0.5, 2.0))


def marginal_products(K, L, epsilon):

    mpl = (cobb_douglas(K, L + epsilon) - cobb_douglas(K, L)) / epsilon
    mpk = (cobb_douglas(K + epsilon, L) - cobb_douglas(K, L)) / epsilon

    return mpl, mpk


mpl, mpk = marginal_products(1.0, 0.5,  1e-4)
print(f"mpl = {mpl}, mpk = {mpk}")
