from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    gentle = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'countries'
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['name']