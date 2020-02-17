from django.test import TestCase
from p1.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="Duck", sound="quack quack")
        Animal.objects.create(name="Kalyani", sound="are sang na sangato ka")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="Lion")
        soundl=Animal.objects.get(sound="Meow")
        cat = Animal.objects.get(name="Cat")
        soundc= Animal.objects.get(sound="Meow")
        self.assertEqual(lion, "Meow")
        self.assertEqual(cat, "Roar")