from django.db import models


class Zoo(models.Model):
    name = models.TextField()
    address = models.TextField()
    postal_code = models.TextField()
    town = models.TextField()
    land = models.TextField()
    telephone_number = models.TextField(blank=True)
    mail = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Zookeeper(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField(blank=True)
    adjusted_since = models.DateField()
    salary = models.IntegerField()
    telephone_number = models.TextField(blank=True)

    def __str__(self):
        return self.first_name


class Animal(models.Model):
    CHOICES1 = (
        ('gk','Großkatzen'),
        ('kk','Kleinkatzen'),
        ('p', 'Primaten'),
        ('h', 'Hunde'),
        ('k', 'Kamele'),
        ('gb','Großbären'),
        ('pf','Pferde'),
    )

    CHOICES2 = (
        ('l', 'Löwe'),
        ('p', 'Puma'),
        ('a', 'Affe'),
        ('w', 'Wolf'),
        ('tt','Trampeltier'),
        ('e', 'Esel'),
        ('le','Leopard'),
        ('lu','Luchs'),
        ('b', 'Braunbär')
    )

    family = models.CharField(max_length=2, choices=CHOICES1)
    category = models.CharField(max_length=2, choices=CHOICES2)
    name = models.TextField()
    origin_land = models.TextField(blank=True)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    food = models.TextField()
    zoo = models.ForeignKey(Zoo,on_delete=models.CASCADE)
    zookeeper = models.ForeignKey(Zookeeper,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
