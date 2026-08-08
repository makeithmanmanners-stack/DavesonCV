from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    project_code = models.CharField(max_length=20, help_text="e.g. PROJECT 01")
    tech_stack = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    url = models.URLField(max_length=300)
    image_path = models.CharField(max_length=255, default='images/project_mhcs.png')
    rank = models.IntegerField(default=1)
    featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['rank']

    def __str__(self):
        return f"{self.project_code} - {self.title}"


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=150, default="System DALTA")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    order = models.IntegerField(default=1)
    responsibilities = models.JSONField(help_text="List of responsibilities with title & text")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.organization}"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True)
    depth_specs = models.JSONField(default=list, help_text="List of spec strings for hover info")
    connected_skills = models.CharField(max_length=255, blank=True, help_text="Comma-separated skills in ecosystem")
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Strength(models.Model):
    title = models.CharField(max_length=150)
    quote = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, default="Portfolio Inquiry")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
