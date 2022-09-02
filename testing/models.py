from multiprocessing.dummy import Manager
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Сounterparty(models.Model):
    organization_name = models.CharField(max_length=200, unique=False)
    phone_number = models.CharField(max_length=15, unique=True)
    inn_document = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.organization_name


class Order(models.Model):
    order_code = models.CharField(max_length=10, unique=False)
    manager_id = models.ForeignKey(Profile, on_delete=models.PROTECT)
    from_organization_id = models.ForeignKey(Сounterparty, related_name='sender',on_delete=models.CASCADE)
    to_organization_id = models.ForeignKey(Сounterparty, related_name='reciever',on_delete=models.CASCADE)

    def __str__(self):
        return self.order_code  # TODO записать номер заказа откуда куда


class Detail(models.Model):
    class Meta:
        ordering = ["-date_created"]

    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    weight = models.DecimalField(max_digits=7, decimal_places=3)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=200, unique=False)
    volume = models.DecimalField(max_digits=7, decimal_places=3)
    place_quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
