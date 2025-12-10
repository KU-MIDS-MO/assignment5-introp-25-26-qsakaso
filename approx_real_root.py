import numpy as np
def approx_real_root(coeffs, interval):
    a, b = interval
    c0, c1, c2, c3 = coeffs

    def p(x):
        return ((c3 * x + c2) * x + c1) * x + c0

    fa = p(a)
    fb = p(b)

    for _ in range(200):
        m = 0.5 * (a + b)
        fm = p(m)

        if np.sign(fm) == np.sign(fa):
            a, fa = m, fm
        else:
            b, fb = m, fm

        if abs(b - a) < 1e-12:
            break

    return 0.5 * (a + b)