"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CampaignEmailTemplate import CampaignEmailTemplate



from .CampignEmailProvider import CampignEmailProvider



class CampaignEmail(BaseSchema):
    #  swagger.json

    
    template = fields.Nested(CampaignEmailTemplate, required=False)
    
    provider = fields.Nested(CampignEmailProvider, required=False)
    
