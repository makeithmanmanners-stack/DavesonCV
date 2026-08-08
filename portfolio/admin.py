from django.contrib import admin
from .models import Project, Experience, SkillCategory, Skill, Strength, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_code', 'title', 'tech_stack', 'rank', 'featured')
    list_editable = ('rank', 'featured')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'start_date', 'end_date', 'order')
    list_editable = ('order',)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subtitle', 'order')
    list_filter = ('category',)
    list_editable = ('order',)


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ('title', 'quote', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
