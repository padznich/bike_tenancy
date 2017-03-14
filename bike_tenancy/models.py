
# -*- coding: utf-8 -*-

from datetime import datetime

from flask_peewee.db import Database, ForeignKeyField
from flask_peewee.db import CharField, FloatField, TextField, BooleanField
from flask_peewee.db import DateField, TimeField
from flask_peewee.admin import ModelAdmin

from app import app


db = Database(app)
now = datetime.now()


class Person(db.Model):

    name = CharField()
    mail = CharField(unique=True)
    address = TextField()
    contacts = TextField()

    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    customer = BooleanField()
    point_keeper = BooleanField()

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        order_by = ("name",)


class PersonAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
        "mail",
        "addres",
        "contacts",
        "customer",
        "point_keeper"
    )


class Company(db.Model):

    name = CharField(unique=True)
    mail = CharField(unique=True)
    address = TextField()
    contacts = TextField()
    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        order_by = ("name",)


class CompanyAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
        "mail",
        "addres",
        "contacts",
    )


class Payment(db.Model):

    name = CharField(unique=True)

    def __unicode__(self):
        return "%s" % self.name


class PaymentAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
    )


class Tariff(db.Model):

    name = CharField()
    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    period = FloatField()
    cost = FloatField()
    discount = FloatField()

    def __unicode__(self):
        return "%s" % self.name


class TariffAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
        "period",
        "cost",
        "discount",
    )


class Point(db.Model):

    name = CharField()
    address = TextField()
    contacts = TextField()
    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    location = CharField(unique=True)
    company_id = ForeignKeyField(Company)
    payment_id = ForeignKeyField(Payment)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        order_by = ("name",)


class PointAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
        "addres",
        "contacts",
        "location",
        "company_id",
        "payment_id"
    )
    foreign_key_lookups = {"company_id": "summary", "payment_id": "payment"}


class Bike(db.Model):

    name = CharField()
    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    gender = CharField()
    size = CharField()
    point_id = ForeignKeyField(Point)
    tariff_id = ForeignKeyField(Tariff)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        order_by = ("name",)


class BikeAdmin(ModelAdmin):

    columns = (
        "id",
        "name",
        "gender",
        "size",
        "point_id",
        "tariff_id"
    )
    foreign_key_lookups = {"point_id": "point", "tariff_id": "tariff"}


class ReservationState(db.Model):

    value = CharField()
    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    identifier = BooleanField()

    def __unicode__(self):
        return "%s" % self.value


class ReservationStateAdmin(ModelAdmin):

    columns = (
        "id",
        "value",
        "identifier",
    )


class Reservation(db.Model):

    date_created = DateField(default=now)
    date_updated = DateField(default=now)

    time_start = TimeField()
    time_finish = TimeField()
    reservation_state_id = ForeignKeyField(ReservationState)
    bike_id = ForeignKeyField(Bike)
    person_id = ForeignKeyField(Person)

    def __unicode__(self):
        return "%s : %s" % (self.time_start, self.time_finish)

    class Meta:
        order_by = ("date_updated",)


class ReservationAdmin(ModelAdmin):

    columns = (
        "id",
        "time_start",
        "time_finish",
        "reservation_state_id",
        "bike_id",
        "tariff_id",
        "person_id"
    )
    foreign_key_lookups = {
        "reservation_state_id": "reservation_state",
        "bike_id": "bike",
        "person_id": "person",
    }
