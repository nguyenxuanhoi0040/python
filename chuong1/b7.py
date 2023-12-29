#Xây lớp Date
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def display(self):
        print(f'{self.day:02d}/{self.month:02d}/{self.year}')

    def next_date(self):
        max_days = 31 
        
        if self.month in [4, 6, 9, 11]:
            max_days = 30
        elif self.month == 2:

            nam_nhuan = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

            if nam_nhuan:
                max_days = 29
            else:
                max_days = 28
        # tính ngày tiếp theo    
        if self.day < max_days:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

day = int(input("Nhập ngày:"))
month = int(input("Nhập tháng:"))
year = int(input("Nhập năm:"))
date = Date(day, month, year)
date.display()
date.next_date()
date.display()  