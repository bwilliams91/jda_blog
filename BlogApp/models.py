from django.db import models


class BlogPostType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPostTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    # We can add other fields here if needed

    def __str__(self):
        return self.username

class UserSocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # You can replace this with a foreign key to a separate model for social media platforms
    profile_url = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.platform}"

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=750)
    media_type = models.ForeignKey(BlogPostType, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogPostTag)
    likes = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}..."

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.comment.id}"

class Inquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
