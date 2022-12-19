"""
    Written by SAAD-IT 19.12.2022
"""

from tortoise.models import Model
from tortoise import fields
from random import choice


class Users(Model):
    id = fields.IntField(pk=True)
    status = fields.CharField(20)
    #testField = fields.IntField (nullable=True, null=True, required=False, default=None)

    def __str__(self):
        odata = f"User {self.id} | status: {self.status}"
        odata = odata if not hasattr (self, "testField") else odata + f" | testField: {self.testField}"
        return odata

    def getId (self,):
        return self.id

    def getStatus (self,):
        return self.status

    def getStatusList():
        return ["new", "old", "gone", "fired"]

    def getRandomStatus():
        return choice(Workers.getStatusList())

class Workers(Model):
    id = fields.IntField(pk=True)
    status = fields.CharField(20)

    def __str__(self):
        return f"Worker {self.id}: {self.status}"

    def getStatusList():
        return ["lazy", "busy", "hard working", "noob", "to be fired"]

    def getRandomStatus():
        return choice(Workers.getStatusList())
