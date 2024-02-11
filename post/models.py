from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.db.models import UniqueConstraint

from common.models import BaseModel

User = get_user_model()


class Post(BaseModel):
    image = models.ImageField(upload_to='pots/images', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
    ])
    caption = models.TextField(validators=[MaxLengthValidator(2000)])

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"{self.author} post about {self.caption}"


class PostComment(BaseModel):
    comment = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"comment by {self.author}"


class PostLike(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
          UniqueConstraint(
              fields=['author', 'post'],
              name='postLikeUnique'
          )
        ]


class CommentLike(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
          UniqueConstraint(
              fields=['author', 'comment'],
              name='CommentLikeUnique'
          )
        ]
