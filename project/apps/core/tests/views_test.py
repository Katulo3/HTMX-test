from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index(client):
    response = client.get(reverse("core:index"))
    assertTemplateUsed(response, "index.html")
