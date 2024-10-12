from django.db import models
from taggit.managers import TaggableManager

from django.conf import settings
from core.models import user_directory_path

User = settings.AUTH_USER_MODEL


STATUS =  (
    ("active", "Active"),
    ("disable", "Disable"),
   
)

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.channel.user.id, filename)



class Channel(models.Model):
    channel_art = models.ImageField(upload_to=user_directory_path,null=True, blank=True,default='images/channel-art.jpg')
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    full_name = models.CharField(max_length=100) 
    channel_name = models.CharField(max_length=100) 
    description = models.TextField(null=True, blank=True)
    keywords = TaggableManager()
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100, default="active")
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,related_name="channel")
    subscribers = models.ManyToManyField(User,related_name="user_subs")
    verified = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.channel_name
    
class Community(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default="active")
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.channel.channel_name
     
    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Community Posts"
        
class CommunityComment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.community.channel.channel_name
    
    class Meta:
        verbose_name = "Community Comments"
        verbose_name_plural = "Community Comments"