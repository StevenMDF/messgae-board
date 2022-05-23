from pyexpat import model
from django.db import models

# Create your models here.
# models are tables in database
# models are class-based
"""
CREATE TABLE POST (
    ID PRIMARY KEY INTEGER,
    TEXT VARCHAR(50),
);
"""


# obj = Post("hello world")
class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):
        # index slicing in python
        return self.text[:50]
    