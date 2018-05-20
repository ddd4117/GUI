class ROI :
    def __init__(self, _x, _y, _width, _height, _element, _number):
        self.startX = _x
        self.startY = _y
        self.endX = _x + _width
        self.endY = _y + _height
        self.width = _width
        self.height = _height
        self.element = _element
        self.number = _number

class sideROI :
    def __init__(self, _side):
        self.dict = {}
        self.side = _side

    def append(self, unit):
        elem = unit.element
        if elem in self.dict :
            self.dict[elem].append(unit)
        else :
            self.dict[elem] = [unit]

    def getElements(self, elem):
        return self.dict[elem]
