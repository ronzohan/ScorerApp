class ComputeTotalScore(object):
    def __init__(self, TEAMS):
        self.TEAMS = TEAMS

    def compute_total(self):
        total1 = 0
        total2 = 0

        total_list = []

        for key, value in self.TEAMS['Chelsea']['scores'].iteritems():
            total1 += value
        total_list.append(total1)

        for key, value in self.TEAMS['Liverpool']['scores'].iteritems():
            total2 += value
        total_list.append(total2)
        return total_list

