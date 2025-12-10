import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.asarray(A)

    ranges = A.max(axis=0) - A.min(axis=0)

    plt.figure()
    plt.bar(np.arange(len(ranges)), ranges)
    plt.xlabel("Column index")
    plt.ylabel("Range (max - min)")
    plt.title("Column Ranges")

    plt.savefig(filename)
    plt.show()
    plt.close()

    return ranges