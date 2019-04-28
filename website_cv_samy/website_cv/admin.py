from django.contrib import admin
from .models import ProfesionnalExperiences, PersonalInformation, Education, Skill, Hobbie, Commentary


class ProfessionalExperiencesAdmin(admin.ModelAdmin):
    list_display = ('job', 'company', 'location', 'date_start', 'date_end', 'current')
    list_filter = ('job', 'company')
    date_hierarchy = 'date_start'
    ordering = ('-date_end', '-date_start')
    search_fields = ('job', 'company', 'location')

    # Form configuration
    fieldsets = (
        # Fieldset 1 : meta-info (title, author…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('job', 'company', 'location', 'date_start', 'date_end', 'current')
        }),
        # Fieldset 2 : Description
        ('Description', {
           'description': 'The form accepts HTML tags. Use them wisely !',
           'fields': ('description', )
        }),
    )


class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'apercu_contenu')

    # Form configuration
    fieldsets = (
        # Fieldset 1 : meta-info (title, author…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('first_name', 'last_name', 'phone_number', 'email', 'linkedIN', 'gitHUB', 'skills',
                       'driving_license')
        }),
        # Fieldset 2 : Description
        ('Description', {
            'description': 'The form accepts HTML tags. Use them wisely !',
            'fields': ('title', 'description', )
        }),
    )

    def apercu_contenu(self, PersonalInformation):
        """
        Returns the first 40 characters of the article content. If he
        there are more than 40 characters, it is necessary to add suspension points.
        """
        text = PersonalInformation.description[0:40]
        if len(PersonalInformation.description) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Preview'


class EducationAdmin(admin.ModelAdmin):
    list_display = ('formation', 'school', 'location', 'date_start', 'date_end', 'current')
    list_filter = ('formation', 'school')
    date_hierarchy = 'date_start'
    ordering = ('-date_end', '-date_start')
    search_fields = ('formation', 'school',  'location')

    # Form configuration
    fieldsets = (
        # Fieldset 1 : meta-info (title, author…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('formation', 'school', 'location', 'date_start', 'date_end', 'current')
        }),
        # Fieldset 2 : Description
        ('Description', {
            'description': 'The form accepts HTML tags. Use them wisely !',
            'fields': ('description',)
        }),
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = ('expertise', 'apercu_contenu')
    list_filter = ('expertise', 'details')
    search_fields = ('expertise', 'details')

    def apercu_contenu(self, Skill):
        text = Skill.details[0:40]
        if len(Skill.details) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Preview'


class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('field', 'apercu_contenu')
    list_filter = ('field', 'details')
    search_fields = ('field', 'details')

    def apercu_contenu(self, Hobbie):
        text = Hobbie.details[0:40]
        if len(Hobbie.details) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Preview'


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('name_commentary', 'date_commentary', 'topic_commentary', 'apercu_contenu', 'visible')
    list_filter = ('name_commentary', 'date_commentary', 'visible')
    date_hierarchy = 'date_commentary'
    ordering = ('date_commentary', )
    search_fields = ('name_commentary', 'date_commentary', 'topic_commentary', 'message_commentary', 'visible')

    def apercu_contenu(self, Commentary):
        text = Commentary.message_commentary[0:40]
        if len(Commentary.message_commentary) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Preview'


admin.site.register(ProfesionnalExperiences, ProfessionalExperiencesAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Hobbie, HobbiesAdmin)
admin.site.register(Commentary, CommentaryAdmin)
