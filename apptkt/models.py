# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    siren = models.IntegerField()

    def __str__(self):
        return "{} company (sector: {}, siren: {})".format(self.name, self.sector, self.siren)


class Result(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    ca = models.IntegerField()
    margin = models.IntegerField()
    ebitda = models.IntegerField()
    loss = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return "{} {} results >>> ca: {}, margin: {}, ebitda: {}, loss: {}".format(self.company.name, self.year,
                                                                                   self.ca, self.margin, self.ebitda,
                                                                                   self.loss)