"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class GetStoreResponse(BaseSchema):
    pass


class StoreItemResponse(BaseSchema):
    pass


class ValidateAddressRequest(BaseSchema):
    pass


class PincodeParentsResponse(BaseSchema):
    pass


class PincodeMetaResponse(BaseSchema):
    pass


class PincodeErrorSchemaResponse(BaseSchema):
    pass


class CountryMetaResponse(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
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


class CountryHierarchy(BaseSchema):
    pass


class CurrencyObject(BaseSchema):
    pass


class CountryObject(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass


class GetOneOrAllPath(BaseSchema):
    pass


class GetOneOrAllQuery(BaseSchema):
    pass


class GetOneOrAllParams(BaseSchema):
    pass


class GetOneOrAll(BaseSchema):
    pass


class LengthValidation(BaseSchema):
    pass


class FieldValidationRegex(BaseSchema):
    pass


class FieldValidation(BaseSchema):
    pass


class GetCountryFieldsAddressValues(BaseSchema):
    pass


class GetCountryFieldsAddress(BaseSchema):
    pass


class GetCountryFieldsAddressTemplate(BaseSchema):
    pass


class GetCountryFields(BaseSchema):
    pass


class GetCountry(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class Localities(BaseSchema):
    pass


class LocalityParent(BaseSchema):
    pass


class GetLocalities(BaseSchema):
    pass


class GetLocality(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass





class GetStoreResponse(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(StoreItemResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class StoreItemResponse(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    processing_time = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class ValidateAddressRequest(BaseSchema):
    # Logistic swagger.json

    
    address = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class PincodeParentsResponse(BaseSchema):
    # Logistic swagger.json

    
    sub_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class PincodeMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    


class PincodeErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class CountryMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    country_code = fields.Str(required=False)
    
    isd_code = fields.Str(required=False)
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Str(required=False), required=False)
    


class PincodeDataResponse(BaseSchema):
    # Logistic swagger.json

    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    meta_code = fields.Nested(CountryMetaResponse, required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    


class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    level = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


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

    
    to_pincode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    journey = fields.Str(required=False)
    


class TATErrorSchemaResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


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

    
    manufacturing_time_unit = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    promise = fields.Nested(TATPromiseResponse, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryRequest, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    


class TATLocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    


class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    request_uuid = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    journey = fields.Str(required=False)
    


class DP(BaseSchema):
    # Logistic swagger.json

    
    fm_priority = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    area_code = fields.Str(required=False, allow_none=True)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    internal_account_id = fields.Str(required=False)
    
    external_account_id = fields.Str(required=False, allow_none=True)
    
    transport_mode = fields.Str(required=False)
    


class LogisticsResponse(BaseSchema):
    # Logistic swagger.json

    
    dp = fields.Dict(required=False)
    


class CountryEntityResponse(BaseSchema):
    # Logistic swagger.json

    
    meta = fields.Nested(CountryMetaResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    parent_id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class CountryListResponse(BaseSchema):
    # Logistic swagger.json

    
    results = fields.List(fields.Nested(CountryEntityResponse, required=False), required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class ReAssignStoreRequest(BaseSchema):
    # Logistic swagger.json

    
    configuration = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    
    ignored_locations = fields.List(fields.Int(required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


class ReAssignStoreResponse(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    pystormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    assigned_stores = fields.List(fields.Dict(required=False), required=False)
    


class CountryHierarchy(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class CurrencyObject(BaseSchema):
    # Logistic swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CountryObject(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    


class GetCountries(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(CountryObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetOneOrAllPath(BaseSchema):
    # Logistic swagger.json

    
    locality_type = fields.Str(required=False)
    
    locality_value = fields.Str(required=False)
    


class GetOneOrAllQuery(BaseSchema):
    # Logistic swagger.json

    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    sector = fields.Str(required=False, allow_none=True)
    


class GetOneOrAllParams(BaseSchema):
    # Logistic swagger.json

    
    path = fields.Nested(GetOneOrAllPath, required=False)
    
    query = fields.Nested(GetOneOrAllQuery, required=False)
    


class GetOneOrAll(BaseSchema):
    # Logistic swagger.json

    
    operation_id = fields.Str(required=False)
    
    params = fields.Nested(GetOneOrAllParams, required=False)
    


class LengthValidation(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False, allow_none=True)
    
    max = fields.Int(required=False, allow_none=True)
    


class FieldValidationRegex(BaseSchema):
    # Logistic swagger.json

    
    value = fields.Str(required=False)
    
    length = fields.Nested(LengthValidation, required=False)
    


class FieldValidation(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    regex = fields.Nested(FieldValidationRegex, required=False)
    


class GetCountryFieldsAddressValues(BaseSchema):
    # Logistic swagger.json

    
    get_one = fields.Nested(GetOneOrAll, required=False)
    
    get_all = fields.Nested(GetOneOrAll, required=False)
    


class GetCountryFieldsAddress(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    edit = fields.Boolean(required=False)
    
    input = fields.Str(required=False)
    
    validation = fields.Nested(FieldValidation, required=False)
    
    values = fields.Nested(GetCountryFieldsAddressValues, required=False)
    
    error_text = fields.Str(required=False, allow_none=True)
    


class GetCountryFieldsAddressTemplate(BaseSchema):
    # Logistic swagger.json

    
    checkout_form = fields.Str(required=False)
    
    store_os_form = fields.Str(required=False)
    
    default_display = fields.Str(required=False)
    


class GetCountryFields(BaseSchema):
    # Logistic swagger.json

    
    address = fields.List(fields.Nested(GetCountryFieldsAddress, required=False), required=False)
    
    serviceability_fields = fields.List(fields.Str(required=False), required=False)
    
    address_template = fields.Nested(GetCountryFieldsAddressTemplate, required=False)
    


class GetCountry(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    
    fields = fields.Nested(GetCountryFields, required=False)
    


class Page(BaseSchema):
    # Logistic swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class Localities(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class LocalityParent(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class GetLocalities(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(Localities, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetLocality(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Str(required=False)
    


