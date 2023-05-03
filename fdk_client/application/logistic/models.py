"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class PincodeErrorSchemaResponse(BaseSchema):
    pass


class PincodeParentsResponse(BaseSchema):
    pass


class CountryMetaResponse(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class PincodeMetaResponse(BaseSchema):
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


class DP(BaseSchema):
    pass


class LogisticsResponse(BaseSchema):
    pass


class CountryEntityResponse(BaseSchema):
    pass


class CountryListResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass


class ReAssignStoreRequest(BaseSchema):
    pass


class ReAssignStoreResponse(BaseSchema):
    pass





class PincodeErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class PincodeParentsResponse(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class CountryMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    isd_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Str(required=False), required=False)
    


class PincodeMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    internal_zone_id = fields.Int(required=False)
    
    zone = fields.Str(required=False)
    


class PincodeDataResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    meta_code = fields.Nested(CountryMetaResponse, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    sub_type = fields.Str(required=False)
    


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    success = fields.Boolean(required=False)
    


class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    


class TATArticlesRequest(BaseSchema):
    # Logistic swagger.json

    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    manufacturing_time = fields.Int(required=False)
    


class TATLocationDetailsRequest(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesRequest, required=False), required=False)
    


class TATViewRequest(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


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

    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


class TATLocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    


class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    to_pincode = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    request_uuid = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    journey = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    action = fields.Str(required=False)
    


class DP(BaseSchema):
    # Logistic swagger.json

    
    fm_priority = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    area_code = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    internal_account_id = fields.Str(required=False)
    
    external_account_id = fields.Str(required=False)
    
    transport_mode = fields.Str(required=False)
    


class LogisticsResponse(BaseSchema):
    # Logistic swagger.json

    
    dp = fields.Dict(required=False)
    


class CountryEntityResponse(BaseSchema):
    # Logistic swagger.json

    
    parent_id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Nested(CountryMetaResponse, required=False)
    
    type = fields.Str(required=False)
    


class CountryListResponse(BaseSchema):
    # Logistic swagger.json

    
    results = fields.List(fields.Nested(CountryEntityResponse, required=False), required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class ReAssignStoreRequest(BaseSchema):
    # Logistic swagger.json

    
    configuration = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    ignored_locations = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


class ReAssignStoreResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    


