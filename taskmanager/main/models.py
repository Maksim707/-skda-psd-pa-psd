from django.db import models

class Magicnumber (models.Model):
    yrnum = models.IntegerField('Пользовательское число')
    compnum = models.IntegerField('Число компьютера')

class New (models.Model):
    newtitle = models.CharField('Название вести', max_length=15)
    newdesc = models.TextField('Описание вести')

    class Meta:
        verbose_name = 'весть'
        verbose_name_plural = 'вести'

    def __str__(self):
        return self.newtitle