"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class PincodeErrorSchemaResponse(BaseSchema):
    pass


class PincodeMetaResponse(BaseSchema):
    pass


class PincodeParentsResponse(BaseSchema):
    pass


class PincodeDataResponse(BaseSchema):
    pass


class PincodeApiResponse(BaseSchema):
    pass


class TATCategoryRequest(BaseSchema):
    pass


class TATArticlesRequest(BaseSchema):
    pass


class TATLocationDetailsRequest(BaseSchema):
    pass


class TATViewRequest(BaseSchema):
    pass


class TATErrorSchemaResponse(BaseSchema):
    pass


class TATTimestampResponse(BaseSchema):
    pass


class TATFormattedResponse(BaseSchema):
    pass


class TATPromiseResponse(BaseSchema):
    pass


class TATArticlesResponse(BaseSchema):
    pass


class TATLocationDetailsResponse(BaseSchema):
    pass


class TATViewResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass





class PincodeErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class PincodeMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    


class PincodeParentsResponse(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    


class PincodeDataResponse(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    


class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    level = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class TATArticlesRequest(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    available_quantity = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


class TATLocationDetailsRequest(BaseSchema):
    # Logistic swagger.json

    
    articles = fields.List(fields.Nested(TATArticlesRequest, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    


class TATViewRequest(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    


class TATErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class TATTimestampResponse(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class TATFormattedResponse(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class TATPromiseResponse(BaseSchema):
    # Logistic swagger.json

    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    


class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    


class TATLocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    


class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    request_uuid = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    action = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    zones = fields.List(fields.Str(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    


