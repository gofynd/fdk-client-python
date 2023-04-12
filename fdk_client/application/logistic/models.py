"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class GetPincodeCityResponse(BaseSchema):
    pass


class LogisticPincodeData(BaseSchema):
    pass


class LogisticMeta(BaseSchema):
    pass


class LogisticParents(BaseSchema):
    pass


class LogisticError(BaseSchema):
    pass


class GetTatProductReqBody(BaseSchema):
    pass


class LocationDetailsReq(BaseSchema):
    pass


class TatReqProductArticles(BaseSchema):
    pass


class LogisticRequestCategory(BaseSchema):
    pass


class GetTatProductResponse(BaseSchema):
    pass


class LocationDetails(BaseSchema):
    pass


class TatProductArticles(BaseSchema):
    pass


class LogisticResponseCategory(BaseSchema):
    pass


class LogisticPromise(BaseSchema):
    pass


class LogisticTimestamp(BaseSchema):
    pass


class Formatted(BaseSchema):
    pass


class ApefaceApiError(BaseSchema):
    pass





class GetPincodeCityResponse(BaseSchema):
    # Logistic swagger.json

    
    request_uuid = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(LogisticPincodeData, required=False), required=False)
    


class LogisticPincodeData(BaseSchema):
    # Logistic swagger.json

    
    meta = fields.Nested(LogisticMeta, required=False)
    
    parents = fields.List(fields.Nested(LogisticParents, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    error = fields.Nested(LogisticError, required=False)
    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class LogisticMeta(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Raw(required=False), required=False)
    


class LogisticParents(BaseSchema):
    # Logistic swagger.json

    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class LogisticError(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class GetTatProductReqBody(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(LocationDetailsReq, required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class LocationDetailsReq(BaseSchema):
    # Logistic swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatReqProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    


class TatReqProductArticles(BaseSchema):
    # Logistic swagger.json

    
    category = fields.Nested(LogisticRequestCategory, required=False)
    


class LogisticRequestCategory(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    


class GetTatProductResponse(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(LocationDetails, required=False), required=False)
    
    request_uuid = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    to_city = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    


class LocationDetails(BaseSchema):
    # Logistic swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    


class TatProductArticles(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Dict(required=False)
    
    category = fields.Nested(LogisticResponseCategory, required=False)
    
    promise = fields.Nested(LogisticPromise, required=False)
    


class LogisticResponseCategory(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    


class LogisticPromise(BaseSchema):
    # Logistic swagger.json

    
    timestamp = fields.Nested(LogisticTimestamp, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    


class LogisticTimestamp(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class Formatted(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ApefaceApiError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    


