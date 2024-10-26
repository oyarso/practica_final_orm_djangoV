from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Laboratorio


class InicioTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/inicio/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("inicio"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(response, "inicio.html")

    def test_template_content(self):
        response = self.client.get(reverse("inicio"))
        self.assertContains(response, "<h1>Página de inicio</h1>")
        self.assertNotContains(response, "No es la Página")


class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(lab_id='123', lab_nombre='Juan', lab_ciudad='Santiago',lab_pais='Chile')
 
    def test_model_content(self):
        self.assertEqual(self.laboratorio.lab_nombre, "Juan")
        self.assertEqual(self.laboratorio.lab_ciudad, "Santiago")
        self.assertEqual(self.laboratorio.lab_pais, "Chile")
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_homepage(self):
        response = self.client.get(reverse("mostrar-lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mostrar.html")
        self.assertContains(response, "Información de Laboratorio")