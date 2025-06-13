# ЗАДАЧА 1: Patient с alias и default_factory
# Создать базовую модель пациента с алиасами для
# first_name и last_name(CamelCase), и автоматическим временем регистрации.
#
# Требования:
# Поля: first_name, last_name (алиасы: firstName, lastName)
# Поле registration_time: генерируется автоматически через default_factory
#
# Включить populate_by_name = True
# Добавить описание в json_schema_extra

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class Patient(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    registration_time: datetime = Field(default_factory=lambda:datetime.now())

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "title": "Информация о пациенте",
            "description": "Модель содержит данные о зарегистрированном пациенте.",
            "deprecated": False,
            "example": {
                "firstName": "Иван",
                "lastName": "Петров",
                "registration_time": "2025-06-12T14:30:00"
            }
        }
    }

if __name__ == '__main__':
    patient = Patient(firstName="Serhii",lastName="Zash")
    print(patient)
