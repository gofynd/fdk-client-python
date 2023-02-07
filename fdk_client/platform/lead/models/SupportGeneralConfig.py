"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CommunicationDetails import CommunicationDetails



from .CommunicationDetails import CommunicationDetails



from .CommunicationDetails import CommunicationDetails





from .CommunicationDetails import CommunicationDetails







class SupportGeneralConfig(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    support_email = fields.Nested(CommunicationDetails, required=False)
    
    support_phone = fields.Nested(CommunicationDetails, required=False)
    
    support_faq = fields.Nested(CommunicationDetails, required=False)
    
    show_communication_info = fields.Boolean(required=False)
    
    support_communication = fields.Nested(CommunicationDetails, required=False)
    
    show_support_dris = fields.Boolean(required=False)
    
    integration = fields.Dict(required=False)
    
