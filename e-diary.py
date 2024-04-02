from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
stud_surname_and_name = "Фролов Иван"
subject = "Математика"
commendation = "Хвалю!"


def get_student(stud_full_name):
    student_list = get_list_or_404(Schoolkid, full_name__contains=stud_full_name)
    if len(student_list) > 1:
        print('''There are {} students with that name.
            Please specify full name.'''.format(len(student_list)))
    else:
        return student_list[0]


def fix_marks(student):
    Mark.objects.filter(schoolkid=student, points__in=[2, 3]).update(points=5)


def remove_chastisements(student):
    stud_chastisements = Chastisement.objects.filter(schoolkid=student)
    stud_chastisements.delete()


def create_commendation(student, lesson, commendation):
    stud_needed_lessons = get_object_or_404(Lesson,
        year_of_study=student.year_of_study,
        group_letter=student.group_letter,
        subject__title__contains=lesson)
    last_lesson = stud_needed_lessons.order_by('-date').first()
    Commendation.objects.create(
        text=commendation,
        created=last_lesson.date,
        schoolkid=student,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher)
