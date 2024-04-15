import pytest

from fdk_client.public import PublicClient, PublicConfig


@pytest.fixture(scope="module")
def public_client():
    publicConfig = PublicConfig({
        "domain":"https://api.fyndx5.de",
        'logLevel': "DEBUG"
    })
    publicClient = PublicClient(publicConfig)
    return publicClient

@pytest.mark.asyncio
async def test_get_locations(public_client):
    response = await public_client.configuration.getLocations(location_type="country")
    locations = response['json']
    assert len(locations['items']) > 0
