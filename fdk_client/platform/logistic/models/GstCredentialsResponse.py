"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EwayBillResponse import EwayBillResponse



from .EinvoiceResponse import EinvoiceResponse



class GstCredentialsResponse(BaseSchema):
    #  swagger.json

    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    
