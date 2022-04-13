from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete = models.CASCADE,
        related_name = 'measurements'
    )
    temperature = models.DecimalField(max_digits = 4, decimal_places = 2)
    time_stamp = models.DateTimeField(auto_now = True)
    image = models.ImageField(blank = True, upload_to = 'images/%Y-%m-%d/')


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
