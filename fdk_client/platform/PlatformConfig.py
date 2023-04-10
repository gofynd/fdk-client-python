"""Platform Config."""

from typing import Dict

from ..common.constants import DEFAULT_DOMAIN
from .OAuthClient import OAuthClient
class PlatformConfig:
    def __init__(self, config: Dict):
        self.companyId = config.get("companyId", "")
        self.domain = config.get("domain", DEFAULT_DOMAIN)
        self.apiKey = config.get("apiKey", "")
        self.apiSecret = config.get("apiSecret", "")
        self.useAutoRenewTimer = config.get("useAutoRenewTimer", True)
        self.oauthClient = OAuthClient(self)
        self.extraHeaders = []

    async def getAccessToken(self) -> str:
        return await self.oauthClient.getAccessToken()
