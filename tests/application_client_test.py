import pytest

from fdk_client.application import ApplicationClient, ApplicationConfig


@pytest.fixture(scope="module")
def application_client():
    applicationConfig = ApplicationConfig({
        "domain":"https://api.fynd.com",
        "applicationID":"000000000000000000000001",
        "applicationToken":"9502d710-5a22-11e9-a001-57d85417c280",
        "locationDetails":{
            "pincode": "385001",
            "country": "India",
            "city": "Ahmedabad",
            "location": {"longitude": "72.585022", "latitude": "23.033863"},
        },
        'logLevel': "DEBUG"
    })
    applicationClient = ApplicationClient(applicationConfig)
    return applicationClient

@pytest.mark.asyncio
async def test_get_products(application_client):
    response = await application_client.catalog.getProducts()
    products = response['json']
    assert len(products['items']) > 0

@pytest.mark.asyncio
async def test_get_navigations(application_client):
    res = await application_client.content.getNavigations()
    assert res['json'] is not None