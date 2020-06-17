class Decision:

    def __init__(self, id):
        self.market = ""
        self.decision = ['疫情影響', 'OPEC石油減產言論', '政府資金入場']
        self.timeline = ['2020-02-01', '2020-04-05', '2020-05-05']
        self.bbi = ['空', '空', '多']
        self.id = id
        self.stock = -1
        self.stock_status = False

    def set_stock_status(self, is_true):
        self.stock_status = is_true
        print(self.stock_status)

    def get_stock_status(self):
        print(self.stock_status)
        return self.stock_status

    def set_stock(self, stock):
        self.stock = stock
        print(self.stock)

    def set_decision(self, event, mode):
        """
        mode 0 : add
        mode 1 : edit
        """
        if mode == 0:
            self.decision.append(event)
        elif mode == 1:
            self.decision[-1] = event
        print(self.decision)

    def set_timeline(self, event, mode):
        """
        mode 0 : add
        mode 1 : edit
        """
        if mode == 0:
            self.timeline.append(event[:10])
        elif mode == 1:
            self.timeline[-1] = event[:10]
        print(self.timeline)

    def set_bbi(self, event, mode):
        """
        mode 0 : add
        mode 1 : edit
        """
        if mode == 0:
            self.bbi.append(event)
        elif mode == 1:
            self.bbi[-1] = event
        print(self.bbi)

    def clear_data(self):
        self.decision = []
        self.timeline = []
        self.bbi = []

    def str_to_bool(self):
        bool_bbi = []
        for item in self.bbi:
            if item == "多":
                bool_bbi.append(1)
            else:
                bool_bbi.append(-1)
        return bool_bbi

    def level(self, input):
        mul = [5, 3, 1]
        pos = 0
        neg = 0
        ouput = []
        for i in input:
            if i > 0:
                ouput.append(i * mul[pos % 3])
                pos += 1
            else:
                ouput.append(i * mul[neg % 3])
                neg += 1
        print(ouput)
        return ouput

    def get_ts(self, mode):
        """
        0 : start
        -1 : end
        """
        import time
        from datetime import datetime

        dt = datetime.strptime(
            self.timeline[mode], '%Y-%m-%d')
        ts = time.mktime(dt.timetuple())
        return str(int(ts))

    # site = "https://query1.finance.yahoo.com/v8/finance/chart/" + str(self.stock) + \
    #    ".TW?period1="+self.get_ts(0)+"&period2="+self.get_ts(-1) + \
    #    "&interval=1d&events=history&=hP2rOschxO0"

    def show_stock(self):
        from modules import test
        test.show_stock(str(self.stock), str(self.get_ts(0)), str(self.get_ts(-1)), self.id)

    def print_pic(self):
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.dates as mdates
        from datetime import datetime
        print("print_pic")
        names = self.decision
        dates = self.timeline
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
        # Chinese support
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

        # Choose some nice levels

        if len(self.bbi) == len(names):
            bool_bbi = self.str_to_bool()
            levels = self.level(bool_bbi)
            levels = np.array(levels)
            print(levels)
        else:
            levels = np.tile([-5, 5, -3, 3, -1, 1],
                             int(np.ceil(len(dates)/6)))[:len(dates)]

        # Create figure and plot a stem plot with the date
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=False)
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


"""
    def show_stock(self):
        import matplotlib.pyplot as plt
        import requests
        import json
        import numpy as np
        import pandas as pd

        site = "https://query1.finance.yahoo.com/v8/finance/chart/" + str(self.stock) + \
            ".TW?period1="++"&period2="+str(self.get_ts(-1)) + \
            "&interval=1d&events=history&=hP2rOschxO0"

        print(site)
        response = requests.get(site)

        plt.rcParams['figure.constrained_layout.use'] = True
        data = json.loads(response.text)
        df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(
            np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
        print(df)
        fig = df.close.plot()

        #fig = class_counts.plot(kind='bar',  figsize=(20, 16), fontsize=26).get_figure()
        fig.figure.savefig(str(self.id) + '_stock.png')
"""
