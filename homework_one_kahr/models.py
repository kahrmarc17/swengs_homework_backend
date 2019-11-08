from django.db import models


''' class Zoo(models.Model):
    name = models.TextField()
    address = models.TextField()
    code = models.TextField()
    street = models.TextField()
    land = models.TextField()
    telephone = models.TextField()
    mail = models.TextField(blank=True)

    def __str__(self):
        return self.name '''


''' class Zookeeper(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField(blank=True)
    adjusted = models.DateField()
    salary = models.IntegerField()
    telephone = models.TextField()

    def __str__(self):
        return self.first_name '''


class Animal(models.Model):
    CHOICES1 = (
        ('g', 'Großkatzen'),
        ('kk','Kleinkatzen'),
        ('p', 'Primaten'),
        ('h', 'Hunde'),
        ('k', 'Kamele'),
        ('b', 'Großbären'),
        ('pf','Pferde'),
    )

    CHOICES2 = (
        ('l', 'Löwe'),
        ('p', 'Puma'),
        ('a', 'Affe'),
        ('w', 'Wolf'),
        ('t', 'Trampeltier'),
        ('e', 'Esel'),
        ('le', 'Leopard'),
        ('lu', 'Luchs'),
        ('b', 'Braunbär')
    )

    family = models.CharField(max_length=1, choices=CHOICES1)
    category = models.CharField(max_length=1, choices=CHOICES2)
    name = models.TextField()
    origin_land = models.TextField(blank=True)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    food = models.TextField()
    zoo = models.TextField()
    zookeeper = models.TextField(blank=True)
    #zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, blank=True)
    #zookeeper = models.ForeignKey(Zookeeper, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
