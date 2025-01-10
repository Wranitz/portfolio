from django.db import models

# Create your models here.


# Tag model for the portfolio app

class Tag(models.Model):
    name = models.CharField(max_length=100, unique= True)

    def __str__(self):
        return self.name


# Projects model for the portfolio app

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tag = models.ManyToManyField(Tag, related_name ="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
        )
    image = models.ImageField(upload_to="project_images/")

    
    def __str__(self):
        return f"{self.project.title} Image"
