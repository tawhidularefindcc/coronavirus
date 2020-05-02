from django import forms
from orgApp import models
from django.utils.translation import ugettext_lazy as _
from mediumeditor.widgets import MediumEditorTextarea
from .models import OrgDetail


class CategoryMainRegForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class OrganisationMainRegForm(forms.ModelForm):
    # org_details = forms.ModelChoiceField(orgDetail.objects.all())
    class Meta:
        model = models.Organisation
        fields = ('name', 'about', 'division', 'district', 'thana', 'phone', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass', 'title': 'hello'}),
            'about': forms.Textarea(attrs={'class': 'editable medium_editor_textarea postcontent'})
        }
        labels = {
            'name': _('সংস্থার নাম'),
            'about': _('সংস্থার উদ্দেশ্য ও কাজ'),
            'division': _('বিভাগ'),
            'district': _('জেলা'),
            'thana': _('থানা'),
            'phone': _('মোবাইল নাম্বার'),
            'email': _('ইমেইল'),

        }
    # def save(self, commit=True):
    #     instance = super().save(commit)
    #     # set Car reverse foreign key from the Person model
    #     instance.org_details_set.add(self.cleaned_data['org_details'])
    #     return instance


class OrgDetailMainRegForm(forms.ModelForm):
    class Meta:
        model = models.OrgDetail
        fields = ('image', 'logo', 'facebook_url', 'website_url', 'youtube_url')
        labels = {
            'image': _('সংস্থার গ্রপ ছবি'),
            'logo': _('লগো'),
            'facebook_url': _('ফেসবুক পেজ লিংক'),
            'website_url': _('ওয়েবসাইট লিংক'),
            'youtube_url': _('ইউটিউব লিংক'),

        }

# 'description': _(' অন্যান্য কথা'),

class OrgProjectMainRegForm(forms.ModelForm):
    class Meta:
        model = models.OrgProject
        fields = '__all__'


"""
If we need any extra features in form we will create a class which will extends those class accordingly...
"""
