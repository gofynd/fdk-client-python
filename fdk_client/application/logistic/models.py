"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class FulfillmentOptionsList(BaseSchema):
    pass


class ValidateAddressDetails(BaseSchema):
    pass


class PincodeDetailsResult(BaseSchema):
    pass


class CountryResult(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass


class GetCountry(BaseSchema):
    pass


class GetLocalitiesApp(BaseSchema):
    pass


class GetLocalityApp(BaseSchema):
    pass


class ErrorResult(BaseSchema):
    pass


class ShipmentCourierPartnerDetails(BaseSchema):
    pass


class ShipmentCourierPartnerResult(BaseSchema):
    pass


class GetPromiseDetails(BaseSchema):
    pass


class ErrorResultApp(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class FulfillmentOptionItem(BaseSchema):
    pass


class PincodeData(BaseSchema):
    pass


class PincodeParentsResult(BaseSchema):
    pass


class PincodeMetaResult(BaseSchema):
    pass


class PincodeErrorSchemaResult(BaseSchema):
    pass


class CountryMeta(BaseSchema):
    pass


class CurrencyObject(BaseSchema):
    pass


class CountryHierarchy(BaseSchema):
    pass


class PincodesLatLongData(BaseSchema):
    pass


class LocalityParent(BaseSchema):
    pass


class CountryEntity(BaseSchema):
    pass


class LogisticsResult(BaseSchema):
    pass


class DP(BaseSchema):
    pass


class ServiceabilityModel(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class GetCountriesItems(BaseSchema):
    pass


class HierarchyItems(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CountryMetaFields(BaseSchema):
    pass


class ApplicationFields(BaseSchema):
    pass


class GetCountryFieldsAddress(BaseSchema):
    pass


class FieldValidation(BaseSchema):
    pass


class FieldValidationRegex(BaseSchema):
    pass


class LengthValidation(BaseSchema):
    pass


class GetCountryFieldsAddressValues(BaseSchema):
    pass


class GetOneOrAll(BaseSchema):
    pass


class GetOneOrAllParams(BaseSchema):
    pass


class GetOneOrAllPath(BaseSchema):
    pass


class GetOneOrAllQuery(BaseSchema):
    pass


class GetCountryFieldsAddressTemplateApplication(BaseSchema):
    pass


class GetCountryFields(BaseSchema):
    pass


class GetCountryFieldsAddressTemplate(BaseSchema):
    pass


class LocalitiesApp(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class ShipmentsCourierPartnersServiceability(BaseSchema):
    pass


class CPShipments(BaseSchema):
    pass


class ShipmentDimension(BaseSchema):
    pass


class ShipmentsArticles(BaseSchema):
    pass


class ArticleWeight(BaseSchema):
    pass


class ArticleAttributes(BaseSchema):
    pass


class ArticleDimension(BaseSchema):
    pass


class ArticleSet(BaseSchema):
    pass


class ArticleSizeDistribution(BaseSchema):
    pass


class SetSize(BaseSchema):
    pass


class ArticleDeliverySlots(BaseSchema):
    pass


class ArticleReturnReason(BaseSchema):
    pass


class CourierPartners(BaseSchema):
    pass


class CourierPartnerPromise(BaseSchema):
    pass


class CourierPartnerAttributes(BaseSchema):
    pass


class CourierPartnerTAT(BaseSchema):
    pass


class ShipmentCourierPartners(BaseSchema):
    pass


class StorePromise(BaseSchema):
    pass


class Promise(BaseSchema):
    pass





class FulfillmentOptionsList(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(FulfillmentOptionItem, required=False), required=False)
    


class ValidateAddressDetails(BaseSchema):
    # Logistic swagger.json

    
    address = fields.Str(required=False)
    
    address_meta = fields.Dict(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False, allow_none=True)
    
    phone = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    country_iso_code = fields.Str(required=False)
    


class PincodeDetailsResult(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeData, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResult, required=False)
    
    request_uuid = fields.Str(required=False, allow_none=True)
    
    stormbreaker_uuid = fields.Str(required=False)
    


class CountryResult(BaseSchema):
    # Logistic swagger.json

    
    results = fields.List(fields.Nested(CountryEntity, required=False), required=False)
    


class GetCountries(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(GetCountriesItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetCountry(BaseSchema):
    # Logistic swagger.json

    
    meta = fields.Nested(CountryMetaFields, required=False)
    
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
    


class GetLocalitiesApp(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(LocalitiesApp, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetLocalityApp(BaseSchema):
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
    


class ErrorResult(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(Error, required=False)
    


class ShipmentCourierPartnerDetails(BaseSchema):
    # Logistic swagger.json

    
    from_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    to_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    shipments = fields.List(fields.Nested(CPShipments, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class ShipmentCourierPartnerResult(BaseSchema):
    # Logistic swagger.json

    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    
    shipments = fields.List(fields.Nested(ShipmentCourierPartners, required=False), required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class GetPromiseDetails(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(StorePromise, required=False), required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    page = fields.Nested(Page, required=False)
    


class ErrorResultApp(BaseSchema):
    # Logistic swagger.json

    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class ValidationError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class StandardError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    


class FulfillmentOptionItem(BaseSchema):
    # Logistic swagger.json

    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PincodeData(BaseSchema):
    # Logistic swagger.json

    
    parents = fields.List(fields.Nested(PincodeParentsResult, required=False), required=False)
    
    meta = fields.Nested(PincodeMetaResult, required=False)
    
    display_name = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResult, required=False)
    
    meta_code = fields.Nested(CountryMeta, required=False)
    
    lat_long = fields.Nested(PincodesLatLongData, required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


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
    


class CountryMeta(BaseSchema):
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
    


class CurrencyObject(BaseSchema):
    # Logistic swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CountryHierarchy(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class PincodesLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Str(required=False), required=False)
    


class LocalityParent(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    serviceability = fields.Dict(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class CountryEntity(BaseSchema):
    # Logistic swagger.json

    
    meta = fields.Nested(CountryMeta, required=False)
    
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
    


class LogisticsResult(BaseSchema):
    # Logistic swagger.json

    
    dp = fields.Dict(required=False)
    


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
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class GetCountriesItems(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(HierarchyItems, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    has_next_hierarchy = fields.Boolean(required=False)
    


class HierarchyItems(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class Page(BaseSchema):
    # Logistic swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class CountryMetaFields(BaseSchema):
    # Logistic swagger.json

    
    application_fields = fields.Nested(ApplicationFields, required=False)
    


class ApplicationFields(BaseSchema):
    # Logistic swagger.json

    
    address = fields.List(fields.Nested(GetCountryFieldsAddress, required=False), required=False)
    
    serviceability_fields = fields.List(fields.Str(required=False), required=False)
    
    address_template = fields.Nested(GetCountryFieldsAddressTemplateApplication, required=False)
    


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
    


class FieldValidation(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    regex = fields.Nested(FieldValidationRegex, required=False)
    


class FieldValidationRegex(BaseSchema):
    # Logistic swagger.json

    
    value = fields.Str(required=False)
    
    length = fields.Nested(LengthValidation, required=False)
    


class LengthValidation(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False, allow_none=True)
    
    max = fields.Int(required=False, allow_none=True)
    


class GetCountryFieldsAddressValues(BaseSchema):
    # Logistic swagger.json

    
    get_one = fields.Nested(GetOneOrAll, required=False)
    
    get_all = fields.Nested(GetOneOrAll, required=False)
    


class GetOneOrAll(BaseSchema):
    # Logistic swagger.json

    
    operation_id = fields.Str(required=False)
    
    params = fields.Nested(GetOneOrAllParams, required=False)
    


class GetOneOrAllParams(BaseSchema):
    # Logistic swagger.json

    
    path = fields.Nested(GetOneOrAllPath, required=False)
    
    query = fields.Nested(GetOneOrAllQuery, required=False)
    


class GetOneOrAllPath(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class GetOneOrAllQuery(BaseSchema):
    # Logistic swagger.json

    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    sector = fields.Str(required=False, allow_none=True)
    


class GetCountryFieldsAddressTemplateApplication(BaseSchema):
    # Logistic swagger.json

    
    checkout_form = fields.Str(required=False)
    
    store_os_form = fields.Str(required=False)
    
    default_display = fields.Str(required=False)
    


class GetCountryFields(BaseSchema):
    # Logistic swagger.json

    
    address = fields.List(fields.Nested(GetCountryFieldsAddress, required=False), required=False)
    
    serviceability_fields = fields.List(fields.Str(required=False), required=False)
    
    address_template = fields.Nested(GetCountryFieldsAddressTemplate, required=False)
    


class GetCountryFieldsAddressTemplate(BaseSchema):
    # Logistic swagger.json

    
    checkout_form = fields.Str(required=False)
    
    store_os_form = fields.Str(required=False)
    
    default_display = fields.Str(required=False)
    


class LocalitiesApp(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    code = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class Error(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class ShipmentsCourierPartnersServiceability(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class CPShipments(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    location_id = fields.Float(required=False)
    
    location_tags = fields.List(fields.Str(required=False), required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    shipment_cost = fields.Float(required=False)
    
    shipment_dimension = fields.Nested(ShipmentDimension, required=False)
    
    courier_partner_schemes = fields.List(fields.Str(required=False), required=False)
    
    location_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticles, required=False), required=False)
    


class ShipmentDimension(BaseSchema):
    # Logistic swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    


class ShipmentsArticles(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    sla = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    group_id = fields.Str(required=False)
    
    weight = fields.Nested(ArticleWeight, required=False)
    
    attributes = fields.Nested(ArticleAttributes, required=False)
    
    category_id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    dimension = fields.Nested(ArticleDimension, required=False)
    
    price = fields.Float(required=False)
    
    brand_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(ArticleSet, required=False)
    
    set_quantity = fields.Int(required=False)
    
    delivery_slots = fields.Nested(ArticleDeliverySlots, required=False)
    
    return_reason = fields.Nested(ArticleReturnReason, required=False)
    


class ArticleWeight(BaseSchema):
    # Logistic swagger.json

    
    shipping = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class ArticleAttributes(BaseSchema):
    # Logistic swagger.json

    
    battery_operated = fields.Str(required=False)
    
    is_flammable = fields.Str(required=False)
    


class ArticleDimension(BaseSchema):
    # Logistic swagger.json

    
    height = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class ArticleSet(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ArticleSizeDistribution, required=False)
    


class ArticleSizeDistribution(BaseSchema):
    # Logistic swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    


class SetSize(BaseSchema):
    # Logistic swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ArticleDeliverySlots(BaseSchema):
    # Logistic swagger.json

    
    delivery_date = fields.Str(required=False)
    
    min_slot = fields.Str(required=False)
    
    max_slot = fields.Str(required=False)
    


class ArticleReturnReason(BaseSchema):
    # Logistic swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    


class CourierPartners(BaseSchema):
    # Logistic swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class CourierPartnerPromise(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
    attributes = fields.Nested(CourierPartnerAttributes, required=False)
    


class CourierPartnerAttributes(BaseSchema):
    # Logistic swagger.json

    
    tat = fields.Nested(CourierPartnerTAT, required=False)
    


class CourierPartnerTAT(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class ShipmentCourierPartners(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class StorePromise(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    


class Promise(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


