from django.db import models


# Create your models here.
class Category(models.Model):
    """Category of OSINT services"""

    name = models.CharField("Name of the category", max_length=150)
    description = models.TextField("Short description of the category")
    url = models.SlugField(max_length=200, unique=True)
    img = models.ImageField("Image for category", upload_to="mages/")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "OSINT category"
        verbose_name_plural = "OSINT category"


class OsintServices(models.Model):
    """Links to the OSINT services with short description"""

    name = models.CharField("Name of the service", max_length=150)
    description = models.TextField("Short description of the category")
    url = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category,
                                 verbose_name="OSINT category",
                                 on_delete=models.SET_NULL,
                                 null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "OSINT service"
        verbose_name_plural = "OSINT service"