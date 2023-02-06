"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .OptedStoreAddress import OptedStoreAddress



from .OptedCompany import OptedCompany



class BrandStoreInfo(BaseSchema):
    #  swagger.json

    
    store_name = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    store_address = fields.Nested(OptedStoreAddress, required=False)
    
    company = fields.Nested(OptedCompany, required=False)
    
