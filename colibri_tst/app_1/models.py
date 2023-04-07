from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True, null=False) 
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True, unique=True)
    gender = models.CharField(max_length=1, null=True)
    date_of_birth = models.CharField(max_length=10,
        null=True, 
        verbose_name="DoB", 
        help_text="Date format: <em>DD/MM/YYYY</em>.")
    industry = models.CharField(max_length=50, null=True)
    salary = models.DecimalField(max_digits=10 ,decimal_places=2, null=True)
    years_of_experience = models.IntegerField(null=True, verbose_name="Year of experience")

    def __str__(self):
        return f'Id:{self.id} -  Name:{self.first_name} - {self.last_name} - {self.email} - {self.industry} - {self.gender} - {self.date_of_birth}'

    
    # def update_employee(self, request.POST):
    #     self.id = request.POST["id"]
    #     self.first_name = request.POST["first_name"]
    #     self.last_name = request.POST["last_name"]
    #     self.gender = request.POST["gender"]
    #     self.email = request.POST["email"]
    #     self.date_of_birth = request.POST["date_of_birth"]
    #     self.industry = request.POST["industry"]
    #     self.salary = request.POST["salary"]
    #     self.years_of_experience = request.POST["years_of_experience"]
   

    class Meta:
        ordering = ['first_name','last_name','industry']
        verbose_name_plural = "employee"
