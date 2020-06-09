from django.db import models


class Bed(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Plant(models.Model):
    common_name = models.CharField(max_length=255)

    latin_name = models.CharField(max_length=255, blank=True, null=True)

    origin = models.TextField(blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.common_name


class EventTypes(models.TextChoices):
    SOW = 'sow', 'Sow'
    TRANSPLANT = 'transplant', 'Transplant'
    HARVEST = 'harvest', 'Harvest'
    DESTROY = 'destroy', 'Destory'


class Event(models.Model):

    type = models.CharField(
        max_length=255,
        choices=EventTypes.choices,
    )

    bed = models.ForeignKey(
        'Bed',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    plant = models.ForeignKey(
        'Plant',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    count = models.PositiveSmallIntegerField(default=1)

    notes = models.TextField(blank=True, null=True)

    datetime = models.DateTimeField()

    def __str__(self):
        string = f'{EventTypes(self.type).label} {self.plant}'

        if self.bed:
            string += f' in {self.bed}'

        string += f' on {self.datetime}'

        return string
