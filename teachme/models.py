from django.db import models
# Create your models here.


class Story(models.Model): #start, finish storylar bo'lsa o'zi
    story_name = models.CharField(max_length=255)
    img1 = models.CharField(max_length=255)
    text1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    img3 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    audio_link = models.CharField(max_length=255)
    def __str__(self):
        return self.story_name


class Course(models.Model):
    name = models.CharField(max_length=255)
    course_image = models.CharField(max_length=255)
    about = models.TextField()
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    video1 = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    video2 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    video3 = models.CharField(max_length=255, blank=True, null=True)
    title3 = models.CharField(max_length=255, blank=True, null=True)
    video4 = models.CharField(max_length=255, blank=True, null=True)
    title4 = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    story_post = models.ForeignKey(Story, default=1, on_delete=models.CASCADE)

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