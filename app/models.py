from django.db import models


class Composition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_release = models.DateField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    compositions = models.ManyToManyField(Composition)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    groups = models.ManyToManyField(Group)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
