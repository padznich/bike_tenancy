
# -*- coding: utf-8 -*-

from flask_peewee.rest import RestAPI
from flask_peewee.admin import Admin
from flask_peewee.auth import Auth

from app import app
from models import db
from models import Person, PersonAdmin
from models import Company, CompanyAdmin
from models import Payment, PaymentAdmin
from models import Tariff, TariffAdmin
from models import Point, PointAdmin
from models import Bike, BikeAdmin
from models import ReservationState, ReservationStateAdmin
from models import Reservation, ReservationAdmin


auth = Auth(app, db)

# REST API
api = RestAPI(app)
api.register(Person)
api.register(Company)
api.register(Payment)
api.register(Tariff)
api.register(Point)
api.register(Bike)
api.register(ReservationState)
api.register(Reservation)
api.setup()

# REST ADMIN
admin = Admin(app, auth)
admin.register(Person, PersonAdmin)
admin.register(Company, CompanyAdmin)
admin.register(Payment, PaymentAdmin)
admin.register(Tariff, TariffAdmin)
admin.register(Point, PointAdmin)
admin.register(Bike, BikeAdmin)
admin.register(ReservationState, ReservationStateAdmin)
admin.register(Reservation, ReservationAdmin)
admin.setup()


def setup_tbl():
    Person.create_table(fail_silently=True)
    Company.create_table(fail_silently=True)
    Payment.create_table(fail_silently=True)
    Tariff.create_table(fail_silently=True)
    Point.create_table(fail_silently=True)
    Bike.create_table(fail_silently=True)
    ReservationState.create_table(fail_silently=True)
    Reservation.create_table(fail_silently=True)


def setup_adm():
    auth.User.create_table(fail_silently=True)
    admin = auth.User(
        username='admin',
        email='',
        admin=True,
        active=True
    )
    admin.set_password('admin')
    admin.save()


if __name__ == "__main__":

    setup_tbl()
    setup_adm()
