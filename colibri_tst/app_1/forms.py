from django import forms
import re

from app_1.models import Employee
# from colibri_tst.settings import DATE_INPUT_FORMATS

def check_date(s_input,patt):
    ''' use a regex date pattern to check the s_input string '''    
    pass

class FormEmployee(forms.ModelForm):
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # email = forms.EmailField(required=True)
    # verify_email = forms.EmailField(required=True, label="Email again")
    # gender = forms.CharField(max_length=1)
    # date_of_birth = forms.CharField(help_text="Date format: <b>dd/mm/yyyy</b>.",  )
    # date_of_birth = forms.DateField(help_text="Date format: <b>dd/mm/yyyy</b>.",  widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=DATE_INPUT_FORMATS)
    # industry = forms.CharField(max_length=50)
    # salary = forms.DecimalField(max_digits=10, decimal_places=2)
    # year_of_experience = forms.IntegerField(max_value=60)

    # def clean(self):
    #     all_clean_date = super().clean()
    #     email = all_clean_date['email']
    #     v_email = all_clean_date["verify_email"]
    #     if email!=v_email:
    #         raise forms.ValidationError("The emails is not the same !")
            
    class Meta:
        model = Employee
        # fields = ["first_name", "last_name", "email", "gender",
        #           "date_of_birth","industry","salary","year_of_experience"]
        fields = '__all__'
        exclude = ["id"]
