from django.test import TestCase 
from .models import Taller

class TestTaller(TestCase):
   # fixtures = ['dump_blog.json']
   def test_grabacion(self):
      q = Taller(nombre="Quimica")
      q.save()
      self.assertEqual(Taller.objects.count(),1)
