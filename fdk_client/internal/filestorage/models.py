"""FileStorage Internal Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..InternalModel import BaseSchema




class GenerateShipmentRequestBody(BaseSchema):
    pass


class GenerateShipment200(BaseSchema):
    pass


class GenerateShipment400(BaseSchema):
    pass


class GenerateShipment500(BaseSchema):
    pass





class GenerateShipmentRequestBody(BaseSchema):
    # FileStorage swagger.json

    
    uid = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    document_type = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Raw(required=False), required=False)
    
    invoice_document_type = fields.Str(required=False)
    
    label_document_type = fields.Str(required=False)
    
    document = fields.List(fields.Raw(required=False), required=False)
    


class GenerateShipment200(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    job_id = fields.Str(required=False)
    
    trace_id = fields.Float(required=False)
    


class GenerateShipment400(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class GenerateShipment500(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    stack_trace = fields.Str(required=False)
    


