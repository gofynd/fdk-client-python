"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class GetStoreResult(BaseSchema):
    pass


class StoreItemResult(BaseSchema):
    pass


class ValidateAddressDetails(BaseSchema):
    pass


class PincodeParentsResult(BaseSchema):
    pass


class PincodeMetaResult(BaseSchema):
    pass


class PincodeErrorSchemaResult(BaseSchema):
    pass


class CountryMetaResult(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class PincodeDataResult(BaseSchema):
    pass


class PincodeDetails(BaseSchema):
    pass


class TATCategoryDetails(BaseSchema):
    pass


class TATArticlesDetails(BaseSchema):
    pass


class TATLocationDetailsDetails(BaseSchema):
    pass


class TATViewDetails(BaseSchema):
    pass


class TATErrorSchemaResult(BaseSchema):
    pass


class TATTimestampResult(BaseSchema):
    pass


class TATFormattedResult(BaseSchema):
    pass


class TATPromiseResult(BaseSchema):
    pass


class TATArticlesResult(BaseSchema):
    pass


class TATLocationDetailsResult(BaseSchema):
    pass


class TATViewResult(BaseSchema):
    pass


class DP(BaseSchema):
    pass


class LogisticsResult(BaseSchema):
    pass


class CountryEntityResult(BaseSchema):
    pass


class ServiceabilityModel(BaseSchema):
    pass


class CountryListResult(BaseSchema):
    pass


class GetZoneFromPincodeViewDetails(BaseSchema):
    pass


class GetZoneFromPincodeViewResult(BaseSchema):
    pass


class ReAssignStoreDetails(BaseSchema):
    pass


class ReAssignStoreResult(BaseSchema):
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


class Error(BaseSchema):
    pass


class ErrorSchema(BaseSchema):
    pass


class ShipmentsArticles(BaseSchema):
    pass


class ShipmentDimension(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class ShipmentCourierPartnerDetails(BaseSchema):
    pass


class CourierPartnerPromise(BaseSchema):
    pass


class CourierPartners(BaseSchema):
    pass


class ShipmentCourierPartners(BaseSchema):
    pass


class ShipmentCourierPartnerResult(BaseSchema):
    pass


class ShipmentsCourierPartnersServiceability(BaseSchema):
    pass


class ServiceabilityLocation(BaseSchema):
    pass


class GetPromiseDetails(BaseSchema):
    pass


class StorePromise(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class ErrorResult(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass





class GetStoreResult(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(StoreItemResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class StoreItemResult(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    processing_time = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class ValidateAddressDetails(BaseSchema):
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
    


class PincodeParentsResult(BaseSchema):
    # Logistic swagger.json

    
    sub_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class PincodeMetaResult(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    
    deliverables = fields.List(fields.Str(required=False), required=False)
    


class PincodeErrorSchemaResult(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class CountryMetaResult(BaseSchema):
    # Logistic swagger.json

    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    phone_code = fields.Str(required=False)
    
    parent_id = fields.Str(required=False, allow_none=True)
    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    isd_code = fields.Str(required=False)
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Str(required=False), required=False)
    


class PincodeDataResult(BaseSchema):
    # Logistic swagger.json

    
    parents = fields.List(fields.Nested(PincodeParentsResult, required=False), required=False)
    
    meta = fields.Nested(PincodeMetaResult, required=False)
    
    display_name = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResult, required=False)
    
    meta_code = fields.Nested(CountryMetaResult, required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class PincodeDetails(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResult, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResult, required=False)
    
    request_uuid = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    


class TATCategoryDetails(BaseSchema):
    # Logistic swagger.json

    
    level = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class TATArticlesDetails(BaseSchema):
    # Logistic swagger.json

    
    category = fields.Nested(TATCategoryDetails, required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    manufacturing_time = fields.Int(required=False)
    


class TATLocationDetailsDetails(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesDetails, required=False), required=False)
    


class TATViewDetails(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsDetails, required=False), required=False)
    
    journey = fields.Str(required=False)
    


class TATErrorSchemaResult(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


class TATTimestampResult(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class TATFormattedResult(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class TATPromiseResult(BaseSchema):
    # Logistic swagger.json

    
    timestamp = fields.Nested(TATTimestampResult, required=False)
    
    formatted = fields.Nested(TATFormattedResult, required=False)
    


class TATArticlesResult(BaseSchema):
    # Logistic swagger.json

    
    manufacturing_time_unit = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResult, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    promise = fields.Nested(TATPromiseResult, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    category = fields.Nested(TATCategoryDetails, required=False)
    
    _manufacturing_time_seconds = fields.Int(required=False)
    


class TATLocationDetailsResult(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesResult, required=False), required=False)
    


class TATViewResult(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    request_uuid = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(TATErrorSchemaResult, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsResult, required=False), required=False)
    
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
    


class LogisticsResult(BaseSchema):
    # Logistic swagger.json

    
    dp = fields.Nested(DP, required=False)
    


class CountryEntityResult(BaseSchema):
    # Logistic swagger.json

    
    meta = fields.Nested(CountryMetaResult, required=False)
    
    logistics = fields.Nested(LogisticsResult, required=False)
    
    display_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    onboarding_allowed = fields.Boolean(required=False)
    
    serviceability = fields.Raw(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    


class ServiceabilityModel(BaseSchema):
    # Logistic swagger.json

    
    lm_cod_limit = fields.Int(required=False, allow_none=True)
    
    is_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    route_code = fields.Str(required=False, allow_none=True)
    
    is_first_mile = fields.Boolean(required=False)
    
    is_reverse_pickup = fields.Boolean(required=False, allow_none=True)
    
    is_return = fields.Boolean(required=False)
    
    is_installation = fields.Boolean(required=False)
    
    is_last_mile = fields.Boolean(required=False)
    


class CountryListResult(BaseSchema):
    # Logistic swagger.json

    
    results = fields.List(fields.Nested(CountryEntityResult, required=False), required=False)
    


class GetZoneFromPincodeViewDetails(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResult(BaseSchema):
    # Logistic swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class ReAssignStoreDetails(BaseSchema):
    # Logistic swagger.json

    
    configuration = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    
    ignored_locations = fields.List(fields.Int(required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


class ReAssignStoreResult(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    pystormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    assigned_stores = fields.List(fields.Dict(required=False), required=False)
    


class CountryHierarchy(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
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
    
    next = fields.Str(required=False, allow_none=True)
    
    slug = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    edit = fields.Boolean(required=False)
    
    input = fields.Str(required=False, allow_none=True)
    
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
    
    meta = fields.Dict(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    custom_meta = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    serviceability = fields.Raw(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    


class LocalityParent(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    serviceability = fields.Raw(required=False)
    
    code = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
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
    
    meta = fields.Dict(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    serviceability = fields.Raw(required=False)
    
    code = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    


class Error(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    


class ErrorSchema(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(Error, required=False)
    


class ShipmentsArticles(BaseSchema):
    # Logistic swagger.json

    
    item_id = fields.Int(required=False)
    
    category_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ShipmentDimension(BaseSchema):
    # Logistic swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    


class Shipments(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    location_id = fields.Float(required=False)
    
    location_tags = fields.List(fields.Str(required=False), required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    shipment_cost = fields.Float(required=False)
    
    shipment_dimension = fields.Nested(ShipmentDimension, required=False)
    
    courier_partner_schemes = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticles, required=False), required=False)
    


class ShipmentCourierPartnerDetails(BaseSchema):
    # Logistic swagger.json

    
    from_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    to_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class CourierPartnerPromise(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class CourierPartners(BaseSchema):
    # Logistic swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class ShipmentCourierPartners(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    


class ShipmentCourierPartnerResult(BaseSchema):
    # Logistic swagger.json

    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    
    shipments = fields.List(fields.Nested(ShipmentCourierPartners, required=False), required=False)
    


class ShipmentsCourierPartnersServiceability(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class ServiceabilityLocation(BaseSchema):
    # Logistic swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    


class GetPromiseDetails(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(StorePromise, required=False), required=False)
    
    delivery_promise = fields.Nested(Promise, required=False)
    
    page = fields.Nested(Page, required=False)
    


class StorePromise(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    delivery_promise = fields.Nested(Promise, required=False)
    


class Promise(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ErrorResult(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ValidationError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class StandardError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    


