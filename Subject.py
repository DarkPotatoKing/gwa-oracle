class Subject():
    def __init__(self, units, grade, name = 'Subject'):
        self.units = units
        self.grade = grade
        self.name = name

    def __repr__(self):
        return self.name + ':\t' + str(self.grade) + '\t(' + str(self.units) + ' units)'