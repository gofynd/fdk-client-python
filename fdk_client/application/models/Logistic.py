"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class PincodeMetaResponse(BaseSchema):
    pass


class PincodeParentsResponse(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class PincodeErrorSchemaResponse(BaseSchema):
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


class TATFormattedResponse(BaseSchema):
    pass


class TATTimestampResponse(BaseSchema):
    pass


class TATPromiseResponse(BaseSchema):
    pass


class TATErrorSchemaResponse(BaseSchema):
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



class PincodeMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    


class PincodeParentsResponse(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    coordinates = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class PincodeErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class PincodeDataResponse(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    sub_type = fields.Str(required=False)
    


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    


class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    


class TATArticlesRequest(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time_unit = fields.Str(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time = fields.Int(required=False)
    


class TATLocationDetailsRequest(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesRequest, required=False), required=False)
    


class TATViewRequest(BaseSchema):
    # Logistic swagger.json

    
    identifier = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    source = fields.Str(required=False)
    


class TATFormattedResponse(BaseSchema):
    # Logistic swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class TATTimestampResponse(BaseSchema):
    # Logistic swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class TATPromiseResponse(BaseSchema):
    # Logistic swagger.json

    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    


class TATErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class TATArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    is_cod_available = fields.Boolean(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    


class TATLocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    


class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    is_cod_available = fields.Boolean(required=False)
    
    request_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    source = fields.Str(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


