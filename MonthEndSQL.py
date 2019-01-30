
from datetime import date, timedelta

class monthpair:
    def __init__(self,monthenddate,refdate):
        self.monthenddate = monthenddate
        self.refdate = refdate

class monthEndDates:
    def __init__(self, startYear, endYear):
        self.sy = startYear
        self.it = endYear
        self.med = []

    def GetMonthEnd(self, yr, mth):
        if mth == 12:
            dt = date(yr + 1, 1, 1)
        else:
            dt = date(yr,mth + 1, 1)
        result = dt - timedelta(days=1)
        return result

    def GetMonthEndDate(self):
        ptrCurYear = self.sy

        while ptrCurYear < self.it + 1:
            ptrCurMth = 1
            while ptrCurMth < 13:
                loopmth = 1
                while loopmth < ptrCurMth + 1:   
                    self.med.append(monthpair(self.GetMonthEnd(ptrCurYear, ptrCurMth),self.GetMonthEnd(ptrCurYear, loopmth)))                                        
                    loopmth += 1              
                ptrCurMth += 1
            ptrCurYear += 1

aa = monthEndDates(2010,2030)
aa.GetMonthEndDate()
with open("/home/jasont14/monthEnd.csv", "w") as f:
        f.write("INSERT INTO <<TABLE>> VALUES\n")
        for a in aa.med:                
                f.write("(CAST('{}' AS DATE),CAST('{}' AS DATE)),{}".format(a.monthenddate,a.refdate,"\n"))
