from django.test import TestCase
from .models import *

class AuthorTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="J. R. R.", last_name="Tolkien", descriptions="John Ronald Reuel Tolkien CBE FRSL ( 3 January 1892 - 2 September 1973) was an English writer and philologist. He was the author of the high fantasy works The Hobbit and The Lord of the Rings. While many other authors had published works of fantasy before Tolkien, the great success of The Hobbit and The Lord of the Rings led directly to a popular resurgence of the genre. This has caused him to be popularly identified as the \"father\" of modern fantasy literature—or, more precisely, of high fantasy.\r\n")
        Person.objects.create(first_name="J. R. R.", last_name="Tolkien", descriptions="John Ronald Reuel Tolkien CBE FRSL ( 3 January 1892 - 2 September 1973) was an English writer and philologist. He was the author of the high fantasy works The Hobbit and The Lord of the Rings. While many other authors had published works of fantasy before Tolkien, the great success of The Hobbit and The Lord of the Rings led directly to a popular resurgence of the genre. This has caused him to be popularly identified as the \"father\" of modern fantasy literature—or, more precisely, of high fantasy.\r\n")
        
    def test_author_models(self):
        tolkien = Person.objects.get(first_name="J. R. R.")
        tolkien_duplicate = Person.objects.get(first_name=111)
        self.assertEqual(tolkien.first_name, "J. R. R.")
        self.assertEqual(tolkien_duplicate.first_name, "J. R. R.")
        
