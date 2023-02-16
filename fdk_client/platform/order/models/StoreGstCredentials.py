"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StoreEinvoice import StoreEinvoice



from .StoreEwaybill import StoreEwaybill



class StoreGstCredentials(BaseSchema):
    #  swagger.json

    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    
