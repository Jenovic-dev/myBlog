from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Post

@receiver(pre_save, sender=Post)
def add_slug_to_post(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        slug = base_slug
        num = 1

        # Vérifie si le slug existe déjà, sinon ajoute "-1", "-2", etc.
        while Post.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        instance.slug = slug
