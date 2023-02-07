"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SubscriptionLimitApplication import SubscriptionLimitApplication



from .SubscriptionLimitMarketplace import SubscriptionLimitMarketplace



from .SubscriptionLimitOtherPlatform import SubscriptionLimitOtherPlatform



from .SubscriptionLimitTeam import SubscriptionLimitTeam



from .SubscriptionLimitProducts import SubscriptionLimitProducts



from .SubscriptionLimitExtensions import SubscriptionLimitExtensions



from .SubscriptionLimitIntegrations import SubscriptionLimitIntegrations





class SubscriptionLimit(BaseSchema):
    #  swagger.json

    
    application = fields.Nested(SubscriptionLimitApplication, required=False)
    
    marketplace = fields.Nested(SubscriptionLimitMarketplace, required=False)
    
    other_platform = fields.Nested(SubscriptionLimitOtherPlatform, required=False)
    
    team = fields.Nested(SubscriptionLimitTeam, required=False)
    
    products = fields.Nested(SubscriptionLimitProducts, required=False)
    
    extensions = fields.Nested(SubscriptionLimitExtensions, required=False)
    
    integrations = fields.Nested(SubscriptionLimitIntegrations, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
