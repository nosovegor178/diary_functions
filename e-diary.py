from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
stud_surname_and_name = "Фролов Иван"
subject = "Математика"
def get_student(stud_full_name):
    students_list = Schoolkid.objects.filter(full_name__contains=stud_surname_and_name)
    if len(student_list) > 1:
        print('There are {} students with that name. Please specify full name.'.format(len(student_list)))
    elif len(student_list) == 0:
        print('There are no students with such name.')
    else:
        return(student_list[0])
def fix_marks(schoolkid):
    stud_bad_marks = Mark.objects.filter(schoolkid=student, points__in=[2, 3])
    for bad_mark in stud_bad_marks:
        bad_mark.points=5
        bad_mark.save()
def remove_chastisements(schoolkid):
    stud_chastisements = Chastisement.objects.filter(schoolkid=student)
    stud_chastisements.delete()
def create_commendation(student, lesson):
    all_stud_lessons = Lesson.objects.filter(year_of_study=student.year_of_study, group_letter=student.group_letter)
    all_stud_needed_lessons = all_stud_lessons.filter(subject__title__contains=lesson)
    last_lesson = all_stud_needed_lessons.order_by('date').first()
    Commendation.objects.create(text="Хвалю!", created=last_lesson.date, schoolkid=student, subject=last_lesson.subject, teacher=last_lesson.teacher)