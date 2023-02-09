"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LogisticsResponse import LogisticsResponse



from .CountryMetaResponse import CountryMetaResponse







from .PincodeParentsResponse import PincodeParentsResponse













class PincodeEntityResponse(BaseSchema):
    #  swagger.json

    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    meta = fields.Nested(CountryMetaResponse, required=False)
    
    is_active = fields.Boolean(required=False)
    
    sub_type = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    name = fields.Str(required=False)
    
    display_sname = fields.Str(required=False)
    
    parent_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
