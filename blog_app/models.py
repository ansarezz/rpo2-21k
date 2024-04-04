from django.db import models

class Post(models.Model):
    title = models.CharField("Название бренда", max_length=255)
    image = models.CharField("Ссылка на изображение", max_length=500)
    cover_image = models.CharField("Ссылка на изображение обложка", max_length=500)
    description = models.TextField("Модель")
    description_max = models.TextField("Описание")
    price = models.CharField("Цена товара", max_length=300)

    def __str__(self):
        return self.title