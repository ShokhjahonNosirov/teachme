from django.db import models
# Create your models here.


class Story(models.Model): #start, finish storylar bo'lsa o'zi
    text = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    #video
    text = models.TextField()
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    post = models.ForeignKey(Post, related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Title")

    def __str__(self):
        return self.title

class Answer(models.Model):

    class Meta:
        ordering = ['id']
    question = models.ForeignKey(Question, default=1, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name="Answer Text")
    is_right = models.BooleanField(default=False)
    # ^ it checks whether the question is right or wrong

    def __str__(self):
        return self.answer_text