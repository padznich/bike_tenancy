
# -*- coding: utf-8 -*-

from bike_tenancy.views import app as application, setup_tbl, setup_adm

setup_tbl()
setup_adm()
application.run()
