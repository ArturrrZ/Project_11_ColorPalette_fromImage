import colorgram


class Read_Colors():
    def __init__(self):
        self.colors=None

    def dominant_colors(self,number_of_colors):

        colors=colorgram.extract('test_colors.png',number_of_colors)

        self.colors=[(old.rgb.r,old.rgb.g,old.rgb.b) for old in colors]



