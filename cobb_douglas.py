def cobb_douglas(K, L):
    
    # Create alpha and z
    z = 1
    alpha = 0.33

    return z * K**alpha * L**(1 - alpha)


print(cobb_douglas(1.0, 0.5) )