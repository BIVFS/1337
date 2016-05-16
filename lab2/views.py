# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

from lab2.models import Owners
from lab2.models import Rooms
from lab2.models import Agreements

class IndexView(TemplateView):
    template_name = "index.html"

#    Owners.objects.create(sname = 'Николаев', fname = 'Александр', patr = 'Иванович', sp = '1111', np = '111111', ph = '89131119821')
 #   Owners.objects.create(sname = 'Кобцев', fname = 'Роман', patr = 'Викторович', sp = '2222', np = '222222', ph = '89522223344')
  #  Owners.objects.create(sname = 'Кесс', fname = 'Сергей', patr = 'Иванович', sp = '3333', np = '333333', ph = '89233217857')
   # Owners.objects.create(sname = 'Киреев', fname = 'Сергей', patr = 'Владимирович', sp = '4444', np = '444444', ph = '89039501433')
    #Owners.objects.create(sname = 'Бусыгин', fname = 'Иван', patr = 'Владимирович', sp = '5555', np = '555555', ph = '89234220015')

#    Rooms.objects.create(square = 30, address = 'ул. Суворова, д. 1, кв. 5')
 #   Rooms.objects.create(square = 10, address = 'ул. Ленина, д. 10, кв. 1')
  #  Rooms.objects.create(square = 50, address = 'ул. Ивана Черных, д. 5, кв. 18')
   # Rooms.objects.create(square = 45, address = 'ул. Красноармейская, д. 25, кв. 7')
    #Rooms.objects.create(square = 20, address = 'ул. Елезаровых, д. 3, кв. 57')

#    Agreements.objects.create(dateConc = '12-03-2015', expDate = '15-06-2016', sname = 'Николаев', fname = 'Александр', patr = 'Иванович', address = 'ул. Суворова, д. 1, кв. 5')
 #   Agreements.objects.create(dateConc = '23-03-2016', expDate = '15-08-2017', sname = 'Кобцев', fname = 'Роман', patr = 'Викторович', address = 'ул. Ленина, д. 10, кв. 1')
  #  Agreements.objects.create(dateConc = '03-11-2015', expDate = '19-09-2016', sname = 'Кесс', fname = 'Сергей', patr = 'Иванович', address = 'ул. Ивана Черных, д. 5, кв. 18')
   # Agreements.objects.create(dateConc = '19-03-2016', expDate = '04-01-2017', sname = 'Киреев', fname = 'Сергей', patr = 'Владимирович', address = 'ул. Красноармейская, д. 25, кв. 7')
    #Agreements.objects.create(dateConc = '15-05-2016', expDate = '15-05-2017', sname = 'Бусыгин', fname = 'Иван', patr = 'Владимирович', address = 'ул. Елезаровых, д. 3, кв. 57')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'ownersList': Owners.objects.all(),
                'roomsList': Rooms.objects.all(),
                'agreementsList': Agreements.objects.all()
            }
        )
        return context