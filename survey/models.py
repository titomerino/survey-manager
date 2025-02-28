from django.db import models
from django.contrib.auth.models import User
from student.models import Student
import json

class Survey(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de la encuesta"
    )
    objective = models.TextField(
        verbose_name="Objetivo de la encuesta"
    )

    def __str__(self):
        return self.name


class ResponseGroup(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de conjunto de respuestas"
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(
        verbose_name="Pregunta"
    )
    survey = models.ForeignKey(
        Survey, 
        related_name='questions', 
        on_delete=models.CASCADE, 
        verbose_name="Encuesta"
    )
    response_group = models.ForeignKey(
        ResponseGroup, 
        related_name='questions', 
        on_delete=models.CASCADE, 
        verbose_name="Conjunto de respuestas"
    )

    def __str__(self):
        return self.question


class Option(models.Model):
    text = models.CharField(
        max_length=200, 
        verbose_name="Texto de la opción"
    )
    response_group = models.ForeignKey(
        ResponseGroup, 
        related_name='options', 
        on_delete=models.CASCADE, 
        verbose_name="Conjunto"
    )

    def __str__(self):
        return self.text


class Campaign(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre de campaña"
    )
    description = models.TextField(
        verbose_name="Descripción"
    )
    start_date = models.DateTimeField(
        verbose_name="Fecha de inicio"
    )
    end_date = models.DateTimeField(
        verbose_name="Fecha de finalización"
    )
    survey = models.ForeignKey(
        Survey, 
        related_name='Campaigns', 
        on_delete=models.CASCADE, 
        verbose_name="Encuesta"
    )

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    campaign = models.ForeignKey(
        Campaign, 
        related_name='assignments', 
        on_delete=models.CASCADE, 
        verbose_name="Campaña"
    )
    user = models.ForeignKey(
        User, 
        related_name='assignments', 
        on_delete=models.CASCADE, 
        verbose_name="Maestro"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='assignments', 
        verbose_name="Estudiante"
    )
    is_completed = models.BooleanField(
        default=False, verbose_name="Completa"
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.student)
    

class Response(models.Model):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name="responses", 
        verbose_name="Estudiante"
    )
    response = models.TextField(verbose_name="Respuestas")

    def get_campaign_id(self):
        """ Extrae el ID de la campaña desde el JSON almacenado en response """
        try:
            data = json.loads(self.response)  # Convertir el texto JSON en diccionario
            return data.get("campaign", {}).get("id")  # Obtener el ID de la campaña
        except json.JSONDecodeError:
            return None
        
    def get_campaign_name(self):
        """ Extrae el name de la campaña desde el JSON almacenado en response """
        try:
            data = json.loads(self.response)  # Convertir el texto JSON en diccionario
            return data.get("campaign", {}).get("name")  # Obtener el name de la campaña
        except json.JSONDecodeError:
            return None 
        
    def get_survey_name(self):
        """ Extrae el name de la evaluación desde el JSON almacenado en response """
        try:
            data = json.loads(self.response)  # Convertir el texto JSON en diccionario
            return data.get("survey", {}).get("name")  # Obtener el name de la evaluación
        except json.JSONDecodeError:
            return None 

    def __str__(self):
        return f"Respuestas para {self.student.name}"
    