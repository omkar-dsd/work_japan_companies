from django.db import models


class PostalAddress(models.Model):
    postal_code = models.IntegerField(primary_key=True)
    locality = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.postal_code, self.locality)

    class Meta:
        db_table = 'postal_address'


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    building_number = models.IntegerField()
    postal_code = models.ForeignKey(PostalAddress, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.name, self.building_number, self.postal_code.postal_code)

    class Meta:
        db_table = 'company'
