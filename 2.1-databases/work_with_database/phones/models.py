from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.PositiveIntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
