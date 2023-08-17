from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .views import Laboratorio

# Create your tests here.

class InicioTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/laboratorio/inicio/")
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("insertar-lab"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("insertar-lab"))
        self.assertTemplateUsed(response, "insertar.html")

    def test_template_content(self):
        response = self.client.get(reverse("insertar-lab"))
        self.assertContains(response, "<title>Empleados</title>")
        self.assertNotContains(response, "no es la pagina")

class LaboratorioTest(TestCase):
        @classmethod
        def setUpTestData(cls):
            cls.laboratorio=Laboratorio.objects.create(id= 9,
                                                       lab_nombre = "Laboratorio00",
                                                       lab_ciudad = "ciudad00",
                                                       lab_pais= "pais00")
            
        def test_model_content(self):
            self.assertEqual(self.laboratorio.id, 9)
            self.assertEqual(self.laboratorio.lab_nombre, "Laboratorio00")
            self.assertEqual(self.laboratorio.lab_ciudad, "ciudad00")
            self.assertEqual(self.laboratorio.lab_pais, "pais00")





  