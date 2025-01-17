from django.db import models
import datetime
from django.utils import timezone
from core import models as core_models






class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)



    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):
    """Reservation Model definition"""

    STATUS_PANDING = "panding"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = ((STATUS_PANDING , "panding"),
                      (STATUS_CONFIRMED ,"confirmed"),
                      (STATUS_CANCELED, "canceled")
                      )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PANDING)

    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guest = models.ForeignKey("users.User",related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room",related_name="reservations", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now()
        return now >= self.check_in and now <= self.check_out
    in_progress.boolean = True


    def is_finished(self):
        now = timezone.now()
        is_finished = now > self.check_out
        if is_finished:
            BookedDay.objects.filter(reservation=self).delete()
        return is_finished


    def save(self, *args, **kwargs):
        if self.pk is None:
            start = self.check_in
            end = self.check_out
            difference = end - start
            existing_booked_day = BookedDay.objects.filter(day__range=(start,end)).exists()
            if not existing_booked_day:
                super().save(*args, **kwargs)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    BookedDay.objects.create(day=day,reservation=self)
                return
        return super().save(*args, **kwargs)