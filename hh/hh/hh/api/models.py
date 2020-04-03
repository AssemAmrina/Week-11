from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=100)
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    def to_json(self):
        return {
                'name': self.name,
                'description': self.description,
                'city': self.city,
                'address': self.address,
                }
class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def to_json(self):
        return {
                'name': self.name,
                'description': self.description,
                'salary': self.salary,
                'company': self.company.id,
                }

