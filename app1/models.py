from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    pname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='studentimage')
    dob=models.DateField(max_length=200)
    password=models.CharField(max_length=200)


    def __str__(self):
        return self.firstname
    


class teacher(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200)
    image=models.ImageField(upload_to='teacherimage')
    password=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Homework(models.Model):
    teachername = models.ForeignKey(teacher,on_delete=models.CASCADE)
    studentname = models.ForeignKey(Student,on_delete=models.CASCADE)
    description = models.TextField()
    submissiondate = models.DateField(max_length=200)
    
class Answer(models.Model):
    studentname = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='answers')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    submitted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.studentname.firstname} for {self.homework.description}"
    
class Answers(models.Model):
    studentname = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ans')
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='ans')
    answer_text = models.TextField()
    submitted_date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return f"Answer by {self.studentname.firstname} for {self.homework.description}"

