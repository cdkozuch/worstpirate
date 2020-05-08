import io

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def do_plot():
    plt.plot([1,2,3], [1,2,3])

    # here is the trick save your figure into a bytes object and you can afterwards expose it via flas
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image