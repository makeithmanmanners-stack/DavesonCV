from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project, Experience, SkillCategory, Skill, Strength, ContactMessage


class PortfolioTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.cat = SkillCategory.objects.create(name="BACKEND DEVELOPMENT", order=1)
        self.skill = Skill.objects.create(
            category=self.cat,
            name="Python (Django)",
            subtitle="Web Framework",
            depth_specs=["Django", "API"],
            connected_skills="Django,Backend"
        )
        self.project = Project.objects.create(
            title="MHCS ALUMNI PLATFORM",
            slug="mhcs-alumni-platform",
            project_code="PROJECT 01",
            tech_stack="Django / MySQL",
            description="Full-stack alumni management system",
            url="https://mhcs-alumni.com/",
            rank=1,
            featured=True
        )

    def test_home_view(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DAVESON")
        self.assertContains(response, "MHCS ALUMNI PLATFORM")

    def test_web_resume_view(self):
        response = self.client.get(reverse('portfolio:web_resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DAVESON CARL A. VASQUEZ")

    def test_download_resume_view(self):
        response = self.client.get(reverse('portfolio:download_resume'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_api_status_view(self):
        response = self.client.get(reverse('portfolio:api_status'))
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data['status'], 'ONLINE')

    def test_contact_form_api(self):
        response = self.client.post(
            reverse('portfolio:api_contact'),
            data={'name': 'Recruiter', 'email': 'recruiter@company.com', 'subject': 'Job Offer', 'message': 'We want to hire you!'},
            CSRF_COOKIE='csrf_token'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)
