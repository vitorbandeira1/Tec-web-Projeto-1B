from django.db import models



# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     def __str__(self):
#         return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400, null=True)
    tag = models.CharField(max_length=200, null=True)
    def __str__(self):
        return "{}. {}".format(self.id, self.title)

