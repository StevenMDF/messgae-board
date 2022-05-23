from urllib import response
from django.test import TestCase
from django.urls import reverse
# from django.test import SimpleTestCase
# Create your tests here.
from .models import Post

class PostTests(TestCase):
    # you find the same keyword from Python's testing library like unittest
    @classmethod
    def setUpTestData(cls):
        # prepare data for testing lateer on
        cls.post = Post.objects.create(text="this is a test!")
    
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "this is a test!")
    
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    
    def test_url_avaiable_by_name(self):
        # "127.0.0.1:8000/"
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "posts/home.html")
    
    
    def test_template_content(self):
        # "127.0.0.1:8000/"
        response = self.client.get(reverse("home"))
        self.assertContains(response, "this is a test!")
    
    