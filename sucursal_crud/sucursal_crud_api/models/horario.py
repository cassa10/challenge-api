from django.db import models

class Horario(models.Model):
    DIAS = (
        ('1','Lunes'),
        ('2','Martes'),
        ('3','Miercoles'),
        ('4','Jueves'),
        ('5','Viernes'),
        ('6','Sabado'),
        ('7','Domingo'),
    )
    dia = models.CharField(max_length=1, choices=DIAS)
    apertura = models.TimeField()
    cierre = models.TimeField()

    def __str__(self):
        return f'{self.DIAS[int(self.dia)][1]}|{self.apertura.strftime("%H:%M")}-{self.cierre.strftime("%H:%M")}'

    def __eq__(self, obj):
        if isinstance(obj, Horario):
                return (self.dia == obj.dia 
                    and self.apertura == obj.apertura 
                    and self.cierre == obj.cierre)
        return False
