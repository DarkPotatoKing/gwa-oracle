class Grades:
    def __init__(self, subjects = []):
        self.subjects = subjects

    def add(self, subject):
        self.subjects.append(subject)

    def computeUnits(self):
        return reduce(lambda a,b: a+b, [i.units for i in self.subjects])

    def computeGWA(self):
        units = self.computeUnits()
        total = reduce(lambda a,b: a+b, [i.units*i.grade for i in self.subjects])
        return int(total / units * 1000) / 1000.0 

    def printSubjects(self):
        for i in self.subjects:
            print i

    def printGWA(self):
        print 'GWA:\t\t' + str(self.computeGWA())

    def printAll(self):
        print 'Grades'
        self.printSubjects()
        self.printGWA()
        print ''