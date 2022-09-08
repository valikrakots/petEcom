from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(max_length=4)
    description = models.CharField(max_length=250)
    main_image = models.ImageField(upload_to='main_images/', default='default.jpg')




class Image(models.Model):
    #class ImageType(models.TextChoices):
    #    MAIN = ('MN','Main')
    #    SOPHOMORE = ('SC', 'Secondary')

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    #im_type = models.CharField(max_length=2, choices=ImageType.choices)
    image = models.ImageField(upload_to='product_images/')

class PageImage(models.Model):
    #class ImageType(models.TextChoices):
    #    MAIN_CAROUSEL = ('MC', 'main_carousel')

    image = models.ImageField(upload_to='page_images/')
    #im_type = models.CharField(max_length=40, choices=ImageType.choices)


class FavouriteItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



@receiver(post_delete, sender=Image)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Image)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


@receiver(post_delete, sender=Product)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        old_img = str(instance.__class__.objects.get(id=instance.id).main_image.path)
        if not old_img.endswith('default.jpg'):
            instance.main_image.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Product)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img and not old_img.endswith('default.jpg'):
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


@receiver(post_delete, sender=PageImage)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=PageImage)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
