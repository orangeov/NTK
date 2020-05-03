from django.db import models
import os

EDUCATION_TYPES = (
     ('1', 'Отсутствует'),
     ('2', 'Среднее общее образование'),
     ('3', 'Среднее профессиональное образование'),
     ('4', 'Высшее образование'),
)

READY_TYPES = (
     ('1', 'Да'),
     ('2', 'Нет'),
)

GENDER_TYPES = (
     ('1', 'Мужской'),
     ('2', 'Женский'),
)

WORK_TYPES = (
     ('1', 'Производство'),
     ('2', 'Экономика и финансы'),
     ('3', 'Общее управление'),
     ('4', 'Другое'),
)

PRAKTIKA_TYPES = (
     ('1', 'Да'),
     ('2', 'Нет, только половину дня'),
     ('3', 'Другое'),
)

def user_directory_path(instance, filename):
    ext = filename.split()
    filename = "%s_%s_%s_%s.%s" % (instance.last_name, instance.first_name, instance.middle_name, instance.date_birth, ext )
    return os.path.join('', filename)

class Professional(models.Model):
    last_name = models.CharField('Фамилия', max_length = 30)
    first_name = models.CharField('Имя', max_length = 30)    
    middle_name = models.CharField('Отчество', max_length = 40)
    date_birth = models.DateField('Дата рождения')
    gender = models.CharField(verbose_name='Пол', max_length=5, choices=GENDER_TYPES)
    email = models.EmailField('Эл. почта')
    telephone = models.CharField('Телефон', max_length = 30)
    type_education = models.CharField(verbose_name='Вид образования', max_length=5, choices=EDUCATION_TYPES)
    program = models.CharField('Специальность', max_length = 60)
    qualification = models.CharField('Квалификация', max_length = 60)
    address = models.CharField('Адрес проживания', max_length = 300)
    ready_to_move = models.CharField(verbose_name='Переезд', max_length=5, choices=READY_TYPES)
    work_type = models.CharField(verbose_name='Направление', max_length=5, choices=WORK_TYPES)
    work_post = models.CharField('Должность', max_length = 60)
    upload = models.FileField('Файл', upload_to=user_directory_path)

    def __str__(self):
    	return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = 'Анкеты соискателей'
        verbose_name_plural = 'Анкеты соискателей'

class Student(models.Model):
    first_name = models.CharField('Имя', max_length = 30)
    last_name = models.CharField('Фамилия', max_length = 30)
    middle_name = models.CharField('Отчество', max_length = 40)
    date_birth = models.DateField('Дата рождения')
    gender = models.CharField(verbose_name='Пол', max_length=5, choices=GENDER_TYPES)
    email = models.EmailField('Эл. почта')
    telephone = models.CharField('Телефон', max_length = 30)
    praktika = models.CharField(verbose_name='Полный рабочий день', max_length=5, choices=PRAKTIKA_TYPES)
    university = models.CharField('Учебное заведение', max_length = 90)
    institute = models.CharField('Факультет', max_length = 60)
    specialty = models.CharField('Специальность', max_length = 60)
    year_of_begin = models.IntegerField('Год поступления') 
    year_of_end = models.IntegerField('Год окончания')
    
    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = 'Анкеты студентов'
        verbose_name_plural = 'Анкеты студентов'