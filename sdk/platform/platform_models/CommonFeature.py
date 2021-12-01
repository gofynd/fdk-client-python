"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CommunicationOptinDialogFeature import CommunicationOptinDialogFeature

from .DeploymentStoreSelectionFeature import DeploymentStoreSelectionFeature

from .ListingPriceFeature import ListingPriceFeature

from .CurrencyFeature import CurrencyFeature

from .RevenueEngineFeature import RevenueEngineFeature

from .FeedbackFeature import FeedbackFeature

from .CompareProductsFeature import CompareProductsFeature

from .RewardPointsConfig import RewardPointsConfig


class CommonFeature(BaseSchema):

    
    communication_optin_dialog = fields.Nested(CommunicationOptinDialogFeature, required=False)
    
    deployment_store_selection = fields.Nested(DeploymentStoreSelectionFeature, required=False)
    
    listing_price = fields.Nested(ListingPriceFeature, required=False)
    
    currency = fields.Nested(CurrencyFeature, required=False)
    
    revenue_engine = fields.Nested(RevenueEngineFeature, required=False)
    
    feedback = fields.Nested(FeedbackFeature, required=False)
    
    compare_products = fields.Nested(CompareProductsFeature, required=False)
    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    

