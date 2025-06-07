from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL
from phonenumber_field.modelfields import PhoneNumberField

# Родительский класс для всех пользователей
class User(models.Model):
    """
    Класс с данными о пользователе
    """

    name = models.CharField(max_length=10, verbose_name="Имя")
    is_verified = models.BooleanField(default=False)
    phone = PhoneNumberField(region='RU', verbose_name="Номер телефона")


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        ordering = ['id']


class RubbishType(models.Model):
    """
    Класс для подводов мусора (стекло, пластик и тд)
    """

    type = models.CharField(unique=True, verbose_name="Тип")

    class Meta:
        verbose_name = "Тип мусора"
        verbose_name_plural = "Типы мусора"

        ordering = ['type']


class PollutionReport(models.Model):
    """
    Класс меток загрязнений на карте
    """


    pollution_types = models.ForeignKey(RubbishType, on_delete=CASCADE, verbose_name="Тип мусора", related_name="polluted_zones")
    location = models.CharField(verbose_name="Координаты")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True, verbose_name="Автор", related_name="marked_zones")

    size = models.PositiveSmallIntegerField(
        verbose_name="Масштаб загрязнения",
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        verbose_name = "Метка загрязнения"
        verbose_name_plural = "Метки загрязнений"

        ordering = ['-created_at', 'user']


class CleanupEvent(models.Model):
    participants = models.ManyToManyField(User, related_name='cleanup_events')
    report = models.OneToOneField(PollutionReport, on_delete=models.CASCADE, related_name='cleanup_event')
    scheduled_for = models.DateTimeField(verbose_name="Дата уборки")
    meeting_point = models.OneToOneField(PollutionReport, on_delete=CASCADE)
    description = models.TextField(verbose_name="Детали мероприятия")

    class Meta:
        verbose_name = "Мероприятие по уборке"
        verbose_name_plural = "Мероприятия по уборке"