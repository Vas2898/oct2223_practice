"""
In a week temprature of a certain place is measured during winter are follow as
degree celcius (26, 24, 28, 31, 30, 26, 24)
"""

class Statistics:

    def __init__(self, data):
        self.data = data

    def mean_temprature(self):
        me = sum(self.data) // len(data)
        print(me)
        

data = [26, 24, 28, 31, 30, 26, 24]

st = Statistics(data)
st.mean_temprature()
