class Statistics:

    def __init__(self, data):
        self.data = data

    def Frequency(self):
        frequency = 0
        givenNumber = int(input("Enter : "))

        for i in data:
            if (i == givenNumber):
                frequency += 1
        print(frequency)

    def mean(self):
        me = sum(self.data) // len(data)
        print(me)
        

data = [15, 17, 20, 21, 22, 13, 18, 17, 11, 20, 20, 21, 24]

st = Statistics(data)
st.Frequency()
st.mean()
