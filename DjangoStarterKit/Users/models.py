from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics/default-image.png')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

class UserFollowing(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following_user'], name='unique_followers')
        ]
        ordering = ["-created"]

    @staticmethod
    def is_friend(user1, user2):
        return UserFollowing.objects.filter(user=user1, following_user=user2).exists() and \
               UserFollowing.objects.filter(user=user2, following_user=user1).exists()

    @staticmethod
    def followers(user):
        return User.objects.filter(following__following_user=user)

    @staticmethod
    def following(user):
        return User.objects.filter(followers__user=user)

    @staticmethod
    def friends(user):
        # This gets users who follow each other
        return User.objects.filter(following__following_user=user, followers__user=user)

    def __str__(self):
        return f'{self.user} follows {self.following_user}'