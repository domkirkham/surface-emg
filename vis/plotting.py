import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_from_obj(obj):

    sns.set()

    obj.abs_acc()

    x_ticks = np.arange(len(obj.x_array))/100

    plt.figure(figsize=(10, 5))
    plt.plot(x_ticks, obj.abs_array)
    plt.title(f'Tremor Magnitude from recording {obj.title}')
    plt.ylabel('Magnitude')
    plt.xlabel('Time (s)')
    plt.savefig(f'mag-{obj.title}.png', dpi=200)

    plt.figure(figsize=(10, 5))
    plt.plot(x_ticks[500:1000], obj.abs_array[500:1000])
    plt.title(f'Tremor Magnitude from recording {obj.title}')
    plt.ylabel('Magnitude')
    plt.xlabel('Time (s)')
    plt.savefig(f'mag-{obj.title}-zoom.png', dpi=200)

    plt.figure(figsize=(10, 5))
    plt.plot(x_ticks[500:1000], obj.x_array[500:1000])
    plt.plot(x_ticks[500:1000], obj.y_array[500:1000])
    plt.plot(x_ticks[500:1000], obj.z_array[500:1000])
    plt.title(f'Tremor axes readings from recording {obj.title}')
    plt.legend(['x-axis', 'y-axis', 'z-axis'], loc='upper left')
    plt.ylabel('Magnitude')
    plt.xlabel('Time (s)')
    plt.savefig(f'mag-{obj.title}-zoom-triax.png', dpi=200)