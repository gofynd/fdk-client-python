"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EinvoiceResponse import EinvoiceResponse



from .EwayBillResponse import EwayBillResponse



class GstCredentialsResponse(BaseSchema):
    #  swagger.json

    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    
