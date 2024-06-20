import pytest, pytest_asyncio, os

from fdk_client.partner import PartnerClient, PartnerConfig


@pytest_asyncio.fixture(scope="module")
async def partner_client():
    partnerConfig = PartnerConfig({
        'domain': "https://api.fyndx1.de",
        "organizationId": "64aec4634bc407961ed265c5",
        "apiKey": os.environ['PARTNER_API_KEY'],
        "apiSecret": os.environ['PARTNER_API_SECRET'],
        "useAutoRenewTimer": False,
        'logLevel': "DEBUG"
    })
    
    token = await partnerConfig.oauthClient.getAccesstokenObj(grant_type='client_credentials')
    partnerConfig.oauthClient.setToken(token)

    partnerClient = PartnerClient(partnerConfig)

    return partnerClient

@pytest.mark.asyncio
async def test_get_theme_versions(partner_client):
    response = await partner_client.theme.getThemeVersions(
            theme_slug="astra-primary-theme-test"
        )
    theme_list = response['json']
    assert len(theme_list['items']) > 0


