import json

import pytest
from django.test import Client
from unittest import TestCase

from django.urls import reverse

from company.models import Company

companies_url = reverse("companies-list")
#Mark in whole class or modules so `pytestmark` should not be changed
pytestmark = pytest.mark.django_db

class BasicCompanyApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def testDown(self) -> None:
        pass


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_one_company_exists_should_succeed(client):
    test_company = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_company.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


#Test POST companies
def test_creat_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": [
            "This field is required."
        ]
    }

def test_create_company_with_layoffs_status_should_success(client) -> None:
    response = client.post(path=companies_url, data={"name": "test company name", "status": "Layoffs"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"

def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(path=companies_url,
                                data={"name": "test company name", "status": "WrongStatus"})
    assert(response.status_code, 400)
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)

# which test can will be failed but still want to run for further run pass that time we use xfail
@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    assert 1 == 2

@pytest.mark.skip
def test_should_be_ok_if_fails() -> None:
    assert 1 == 2


def raise_custom_exception() -> None:
    raise ValueError('Custom Exception')


def test_raise_custom_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_custom_exception()
    assert "Custom Exception" == str(e.value)


import logging

logger = logging.getLogger('CUSTOM_EXCEPTION_LOGS')


def function_that_logs_somthing() -> None:
    try:
        raise ValueError("Custom Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_somthing()
    assert "I am logging Custom Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
