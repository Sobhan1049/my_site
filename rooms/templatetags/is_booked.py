# import datetime
# from django import template
# from reservations import models as reservation_models
#
# register = template.Library()
#
#
# @register.simple_tag
# def is_booked(room, day):
#     if day.number == 0:
#         return
#     try:
#         date = datetime.datetime(year=day.year, month=day.month, day=day.number)
#         reservation_models.BookedDay.objects.get(day=date, reservation__room=room)
#         return True
#     except reservation_models.BookedDay.DoesNotExist:
#         return False



import datetime
import calendar
from django import template
from reservations import models as reservation_models

register = template.Library()


@register.simple_tag
def is_booked(room, day):
    if day.number == 0:
        return

    try:

        last_day = calendar.monthrange(day.year, day.month)[1]
        if not (1 <= day.number <= last_day):

            return False

        date = datetime.datetime(year=day.year, month=day.month, day=day.number)
        reservation_models.BookedDay.objects.get(day=date, reservation__room=room)
        return True

    except reservation_models.BookedDay.DoesNotExist:
        return False
    except ValueError as ve:
        return False
