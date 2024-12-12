from django.utils import timezone
import calendar
import jdatetime


class Day:
    def __init__(self, number, past, month, year):
        self.number = number
        self.past = past
        self.month = month
        self.year = year

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.days_names = ("دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه")
        self.months = (
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند")

    def get_days(self):

        jalali_date = jdatetime.date.fromgregorian(year=self.year, month=self.month, day=1)
        year_jalali = jalali_date.year
        month_jalali = jalali_date.month



        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        for week in weeks:
            for day, _ in week:
                if day == 0:
                    continue
                now = timezone.now()
                today_jalali = jdatetime.date.fromgregorian(date=now).day
                month_jalali_now = jdatetime.date.fromgregorian(date=now).month
                past = False
                if month_jalali == month_jalali_now:
                    if day <= today_jalali:
                        past = True
                new_day = Day(number=day, past=past, month=month_jalali, year=year_jalali)
                days.append(new_day)
        return days

    def get_month(self):

        jalali_date = jdatetime.date.fromgregorian(year=self.year, month=self.month, day=1)
        return self.months[jalali_date.month - 1]




