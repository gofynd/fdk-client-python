import pytest, pytest_asyncio, os

from fdk_client.platform import PlatformClient, PlatformConfig

applicationId = "6464b1169a8c6b7d5005d12e"

@pytest_asyncio.fixture(scope="module")
async def platform_client():
    platformConfig = PlatformConfig({
        "companyId": 1,
        "domain":"https://api.fyndx1.de",
        "apiKey": os.environ['API_KEY'],
        "apiSecret": os.environ['API_SECRET'],
        'logLevel': "DEBUG"
    })
    
    token = await platformConfig.oauthClient.getAccesstokenObj(grant_type='client_credentials')
    platformConfig.oauthClient.setToken(token)

    platformClient = PlatformClient(platformConfig)

    return platformClient

@pytest.mark.asyncio
async def test_get_currencies(platform_client):
    response = await platform_client.configuration.getCurrencies()
    response = response['json']
    assert len(response['items']) > 0


@pytest.mark.asyncio
async def test_get_app_basic_details(platform_client):
    response = await platform_client.application(applicationId).configuration.getAppBasicDetails()
    app_details = response['json']
    assert app_details is not None