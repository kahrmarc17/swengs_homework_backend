from django.contrib import admin
from . import models


'''class ZooAdmin(admin.ModelAdmin):
      list_display = ('name', 'address', 'code', 'street', 'land', 'telephone', 'mail')
      pass


admin.site.register(models.Zoo, ZooAdmin) '''


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('family', 'category', 'name', 'origin_land', 'date_of_birth', 'age', 'food', 'zoo', 'zookeeper')
    search_fields = ['name']
    sortable_by = ['category']
    pass


admin.site.register(models.Animal, AnimalAdmin)


''' class ZookeeperAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'adjusted', 'salary', 'telephone']
    pass


admin.site.register(models.Zookeeper, ZookeeperAdmin) '''
