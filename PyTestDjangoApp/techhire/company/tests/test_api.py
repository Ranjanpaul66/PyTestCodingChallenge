import json

import pytest
from django.test import Client
from unittest import TestCase

from django.urls import reverse

from company.models import Company


@pytest.mark.django_db
class BasicCompanyApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def testDown(self) -> None:
        pass


class TestGetCompany(BasicCompanyApiTestCase):

    def test_zero_companies_should_return_empty_list(self) -> None:
        companies_url = reverse("companies-list")
        response = self.client.get(companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self):
        test_company = Company.objects.create(name="Amazon")
        companies_url = reverse("companies-list")
        response = self.client.get(companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), test_company.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("notes"), "")

        test_company.delete()


class TestPostCompanies(BasicCompanyApiTestCase):
    def test_creat_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {
            "name": [
                "This field is required."
            ]
        })
