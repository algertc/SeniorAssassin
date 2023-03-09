class Team:

    name = ""
    number = ""

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.target = Team

    @staticmethod
    def generateArray():
        import csv
        with open('teams.csv', mode='r') as file:
            teamList = []
            csvFile = csv.reader(file)
            for line in csvFile:
                teamList.append(Team(str(line[0]), str(line[1])))
        return teamList


    def setTarget(self, target):
        self.target = target

    def getTarget(self):
        return self.target.name