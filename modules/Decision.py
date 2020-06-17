class Decision:

    def __init__(self, id):
        self.market = ""
        self.decision = []
        self.timeline = []
        self.id = id

    def set_decision(self, event, mode):
        """
        mode 0 : add
        mode 1 : edit
        """
        if mode == 0:
            self.decision.append(event)
        elif mode == 1:
            self.decision[-1] = event[:10]
        print(self.decision)

    def set_timeline(self, event, mode):
        """
        mode 0 : add
        mode 1 : edit
        """
        if mode == 0:
            self.timeline.append(event)
        elif mode == 1:
            self.timeline[-1] = event[:10]
        print(self.timeline)

    def print_pic(self):
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.dates as mdates
        from datetime import datetime
        print("print_pic")
        names = self.decision
        dates = self.timeline
        # Chinese support
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

        # Choose some nice levels
        levels = np.tile([-5, 5, -3, 3, -1, 1],
                         int(np.ceil(len(dates)/6)))[:len(dates)]

        # Create figure and plot a stem plot with the date
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
        ax.set(title="Matplotlib release dates")

        markerline, stemline, baseline = ax.stem(dates, levels,
                                                 linefmt="C3-", basefmt="k-")

        plt.setp(markerline, mec="k", mfc="w", zorder=3)

        # Shift the markers to the baseline by replacing the y-data by zeros.
        markerline.set_ydata(np.zeros(len(dates)))

        # annotate lines
        vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
        for d, l, r, va in zip(dates, levels, names, vert):
            ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                        textcoords="offset points", va=va, ha="right")

        # format xaxis with 4 month intervals
        ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=4))
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        # remove y axis and spines
        ax.get_yaxis().set_visible(False)
        for spine in ["left", "top", "right"]:
            ax.spines[spine].set_visible(False)

        ax.margins(y=0.1)
        print("print_pic")
        plt.savefig(str(self.id))