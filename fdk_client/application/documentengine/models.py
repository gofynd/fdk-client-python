"""DocumentEngine Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..ApplicationModel import BaseSchema





class creditNoteParameter(BaseSchema):
    pass


class invoiceParameter(BaseSchema):
    pass


class ResponseGetInvoiceShipment(BaseSchema):
    pass


class getInvoiceByShipmentId400Response(BaseSchema):
    pass


class getInvoiceByShipmentId500Response(BaseSchema):
    pass


class ReqBodyPresignedPOST(BaseSchema):
    pass


class ResponsePresignedGETURL(BaseSchema):
    pass


class ErrorResponsePresignedUrl(BaseSchema):
    pass





class creditNoteParameter(BaseSchema):
    # DocumentEngine swagger.json

    
    expires_in = fields.Int(required=False)
    


class invoiceParameter(BaseSchema):
    # DocumentEngine swagger.json

    
    document_type = fields.Str(required=False)
    
    expires_in = fields.Int(required=False)
    


class ResponseGetInvoiceShipment(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    


class getInvoiceByShipmentId400Response(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class getInvoiceByShipmentId500Response(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    


class ReqBodyPresignedPOST(BaseSchema):
    # DocumentEngine swagger.json

    
    event = fields.Str(required=False)
    
    media_type = fields.List(fields.Raw(required=False), required=False)
    
    expires_in = fields.Int(required=False)
    


class ResponsePresignedGETURL(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    


class ErrorResponsePresignedUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


