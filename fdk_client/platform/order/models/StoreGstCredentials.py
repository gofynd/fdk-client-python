"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .StoreEwaybill import StoreEwaybill



from .StoreEinvoice import StoreEinvoice



class StoreGstCredentials(BaseSchema):
    #  swagger.json

    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    
