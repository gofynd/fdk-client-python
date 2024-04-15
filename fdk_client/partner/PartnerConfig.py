"""Partner Config."""

from typing import Dict

from ..common.constants import DEFAULT_DOMAIN
from .OAuthClient import OAuthClient

class PartnerConfig:
    def __init__(self, config: Dict):
        self.organizationId = config.get("organizationId", "")
        self.domain = config.get("domain", DEFAULT_DOMAIN)
        self.apiKey = config.get("apiKey", "")
        self.apiSecret = config.get("apiSecret", "")
        self.useAutoRenewTimer = config.get("useAutoRenewTimer", True)
        self.oauthClient = OAuthClient(self)
        self.extraHeaders = []
        self.logLevel=config.get("logLevel", "ERROR")

    async def getAccessToken(self) -> str:
        return await self.oauthClient.getAccessToken()