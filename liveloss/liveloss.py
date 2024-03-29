import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import matplotlib.ticker as ticker


class LiveLoss:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], 'o-')
        self.xs, self.ys = [], []
        self.line.set_data(self.xs, self.ys)
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    def update(self):
        self.line.set_data(self.xs, self.ys)
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.set_title('Loss for each Epoch')
        clear_output(wait=True)
        display(self.fig)

    def send(self, x, y):
        self.xs.append(x)
        self.ys.append(y)
        self.update()
        plt.pause(0.1)

    def get_line(self):
        return self.line,
