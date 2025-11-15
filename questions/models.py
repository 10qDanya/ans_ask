from django.db import models

class Question(models.Model):
    text = models.CharField(verbose_name='Текст вопроса')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания вопроса')

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

        



