import colorgram


class Read_Colors():
    def __init__(self,):
        self.colors=None
        self.image_path='test_colors.png'
    def dominant_colors(self,number_of_colors):

        colors=colorgram.extract(self.image_path,number_of_colors)

        self.colors=[(old.rgb.r,old.rgb.g,old.rgb.b) for old in colors]



