import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    signal = np.asarray(signal)


    diff = np.diff(signal)

    signs = np.sign(diff)

    turning_indices = np.where(signs[1:] != signs[:-1])[0] + 1

    plt.figure()
    plt.plot(signal, marker='o', label="signal")

    plt.scatter(turning_indices, signal[turning_indices], color='red', zorder=5, label="turning points")

    plt.title("Turning Points in Signal")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()

    plt.savefig(filename)
    plt.show()
    plt.close()

    return turning_indices
