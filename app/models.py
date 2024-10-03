from django.db import models


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
        ordering = ('date',)

    def __str__(self):
        return self.date.strftime('%d/%m/%Y %H:%M')
