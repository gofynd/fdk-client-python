"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class PackagingDimension(BaseSchema):
    pass


class ShipmentArticleMeta(BaseSchema):
    pass


class DeliveryTatSchema(BaseSchema):
    pass


class DeliveryTat(BaseSchema):
    pass


class CourierPartnerPromiseData(BaseSchema):
    pass


class PromiseMeta(BaseSchema):
    pass


class PromiseData(BaseSchema):
    pass


class CourierPartnersTat(BaseSchema):
    pass


class AreaCode(BaseSchema):
    pass


class SetSize(BaseSchema):
    pass


class ArticleSizeDistribution(BaseSchema):
    pass


class SetSizeItem(BaseSchema):
    pass


class SetSizeDistribution(BaseSchema):
    pass


class PromiseObject(BaseSchema):
    pass


class ShipmentCourierPartners(BaseSchema):
    pass


class ShipmentsArticles(BaseSchema):
    pass


class ArticleReturnReason(BaseSchema):
    pass


class ArticleDeliverySlots(BaseSchema):
    pass


class ArticleSet(BaseSchema):
    pass


class ArticleDimension(BaseSchema):
    pass


class ArticleAttributes(BaseSchema):
    pass


class ArticleWeight(BaseSchema):
    pass


class ServiceabilityLocation(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class ShipmentError(BaseSchema):
    pass


class LocationDetailsArticle(BaseSchema):
    pass


class LocationDetailsServiceability(BaseSchema):
    pass


class GenerateShipmentsLocationArticles(BaseSchema):
    pass


class GenerateShipmentsRequest(BaseSchema):
    pass


class GenerateShipmentsAndCourierPartnerResponse(BaseSchema):
    pass


class ListViewResponseV2(BaseSchema):
    pass


class ListViewItemsV2(BaseSchema):
    pass


class GeoArea(BaseSchema):
    pass


class ListViewProductV2(BaseSchema):
    pass


class Summary(BaseSchema):
    pass


class RegionSchema(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
    pass


class Region(BaseSchema):
    pass


class GeoAreaGetResponseBody(BaseSchema):
    pass


class GeoAreaItemResponse(BaseSchema):
    pass


class Page2(BaseSchema):
    pass


class AreaExpandedV2(BaseSchema):
    pass


class RegionV2(BaseSchema):
    pass


class Country(BaseSchema):
    pass


class ServiceabilityZoneErrorResponse(BaseSchema):
    pass


class ServiceabilityErrorResponse(BaseSchema):
    pass


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


class CountryMetaResponse(BaseSchema):
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


class ErrorObject(BaseSchema):
    pass


class GetLocalities(BaseSchema):
    pass


class GetLocality(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class ErrorResponseV2(BaseSchema):
    pass


class ErrorResponseV3(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class ShipmentRequest(BaseSchema):
    pass


class LocationArticle(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class Attributes(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class Set(BaseSchema):
    pass


class DeliverySlots(BaseSchema):
    pass


class ServiceabilityNew(BaseSchema):
    pass


class Location(BaseSchema):
    pass


class ShipmentResponse(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class ShipmentItem(BaseSchema):
    pass


class TAT(BaseSchema):
    pass


class CourierPartner(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class PromiseDetails(BaseSchema):
    pass


class Packaging(BaseSchema):
    pass


class StorePromise(BaseSchema):
    pass


class GetPromiseDetails(BaseSchema):
    pass





class PackagingDimension(BaseSchema):
    # Logistic swagger.json

    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    


class ShipmentArticleMeta(BaseSchema):
    # Logistic swagger.json

    
    is_set = fields.Boolean(required=False)
    
    set = fields.Dict(required=False)
    
    is_set_article = fields.Boolean(required=False)
    
    set_quantity = fields.Int(required=False)
    
    split_article_id = fields.Str(required=False)
    
    promo_ids = fields.List(fields.Str(required=False), required=False)
    


class DeliveryTatSchema(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class DeliveryTat(BaseSchema):
    # Logistic swagger.json

    
    tat = fields.Nested(DeliveryTatSchema, required=False)
    


class CourierPartnerPromiseData(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
    attributes = fields.Nested(DeliveryTat, required=False)
    


class PromiseMeta(BaseSchema):
    # Logistic swagger.json

    
    seller_promise = fields.Nested(PromiseData, required=False)
    
    courier_partner_promise = fields.Nested(CourierPartnerPromiseData, required=False)
    
    customer_initial_promise = fields.Nested(PromiseData, required=False)
    


class PromiseData(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class CourierPartnersTat(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class AreaCode(BaseSchema):
    # Logistic swagger.json

    
    source = fields.Str(required=False)
    
    destination = fields.Str(required=False)
    


class SetSize(BaseSchema):
    # Logistic swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ArticleSizeDistribution(BaseSchema):
    # Logistic swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    


class SetSizeItem(BaseSchema):
    # Logistic swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class SetSizeDistribution(BaseSchema):
    # Logistic swagger.json

    
    sizes = fields.List(fields.Nested(SetSizeItem, required=False), required=False)
    


class PromiseObject(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
    customer_promise = fields.Nested(PromiseData, required=False)
    
    meta = fields.Nested(PromiseMeta, required=False)
    


class ShipmentCourierPartners(BaseSchema):
    # Logistic swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    area_code = fields.Nested(AreaCode, required=False)
    
    tat = fields.Nested(CourierPartnersTat, required=False)
    
    display_name = fields.Str(required=False)
    
    is_qc_enabled = fields.Boolean(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    forward_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    reverse_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    ndr_attempts = fields.Int(required=False, allow_none=True)
    
    weight = fields.Int(required=False, allow_none=True)
    
    volumetric_weight = fields.Int(required=False, allow_none=True)
    
    transport_type = fields.Str(required=False, allow_none=True)
    


class ShipmentsArticles(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(ArticleSet, required=False)
    
    sla = fields.Str(required=False)
    
    meta = fields.Nested(ShipmentArticleMeta, required=False)
    
    department_id = fields.Int(required=False)
    
    category_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    group_info = fields.Dict(required=False)
    
    group_info_ids = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ArticleReturnReason(BaseSchema):
    # Logistic swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    


class ArticleDeliverySlots(BaseSchema):
    # Logistic swagger.json

    
    delivery_date = fields.Str(required=False)
    
    min_slot = fields.Str(required=False)
    
    max_slot = fields.Str(required=False)
    


class ArticleSet(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ArticleSizeDistribution, required=False)
    


class ArticleDimension(BaseSchema):
    # Logistic swagger.json

    
    height = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class ArticleAttributes(BaseSchema):
    # Logistic swagger.json

    
    battery_operated = fields.Str(required=False)
    
    is_flammable = fields.Str(required=False)
    


class ArticleWeight(BaseSchema):
    # Logistic swagger.json

    
    shipping = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class ServiceabilityLocation(BaseSchema):
    # Logistic swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    


class Shipments(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    ewaybill_enabled = fields.Boolean(required=False, allow_none=True)
    
    mps = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    count = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticles, required=False), required=False)
    
    courier_partners = fields.List(fields.Nested(ShipmentCourierPartners, required=False), required=False)
    
    promise = fields.Nested(PromiseObject, required=False)
    
    tags = fields.List(fields.Dict(required=False), required=False)
    
    is_mto = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_locked = fields.Boolean(required=False)
    
    packaging = fields.Nested(Packaging, required=False)
    
    delivery_slots = fields.Nested(ArticleDeliverySlots, required=False)
    
    weight = fields.Float(required=False)
    
    volumetric_weight = fields.Float(required=False)
    
    is_auto_assign = fields.Boolean(required=False)
    
    shipment_type = fields.Str(required=False)
    
    from_serviceability = fields.Dict(required=False)
    
    error = fields.Nested(ShipmentError, required=False)
    


class ShipmentError(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class LocationDetailsArticle(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    group_id = fields.Str(required=False)
    
    group_info = fields.Dict(required=False)
    
    group_info_ids = fields.List(fields.Str(required=False), required=False)
    
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
    


class LocationDetailsServiceability(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    location = fields.Nested(ServiceabilityLocation, required=False)
    


class GenerateShipmentsLocationArticles(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_serviceability = fields.Nested(LocationDetailsServiceability, required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Nested(LocationDetailsArticle, required=False), required=False)
    
    ewaybill_enabled = fields.Boolean(required=False)
    
    is_home_delivery = fields.Boolean(required=False)
    


class GenerateShipmentsRequest(BaseSchema):
    # Logistic swagger.json

    
    to_serviceability = fields.Nested(LocationDetailsServiceability, required=False)
    
    location_articles = fields.List(fields.Nested(GenerateShipmentsLocationArticles, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class GenerateShipmentsAndCourierPartnerResponse(BaseSchema):
    # Logistic swagger.json

    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    is_cod_available = fields.Boolean(required=False)
    


class ListViewResponseV2(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(ListViewItemsV2, required=False), required=False)
    
    page = fields.Nested(ZoneDataItem, required=False)
    


class ListViewItemsV2(BaseSchema):
    # Logistic swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Nested(GeoArea, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stores = fields.Nested(ListViewProductV2, required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    is_public_opted = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProductV2, required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    summary = fields.Nested(Summary, required=False)
    


class GeoArea(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ListViewProductV2(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class Summary(BaseSchema):
    # Logistic swagger.json

    
    stores_count = fields.Int(required=False)
    
    products_count = fields.Int(required=False)
    
    regions = fields.List(fields.Nested(RegionSchema, required=False), required=False)
    


class RegionSchema(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ZoneDataItem(BaseSchema):
    # Logistic swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class Region(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    parent_uid = fields.Str(required=False)
    


class GeoAreaGetResponseBody(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(GeoAreaItemResponse, required=False), required=False)
    
    page = fields.Nested(Page2, required=False)
    


class GeoAreaItemResponse(BaseSchema):
    # Logistic swagger.json

    
    geoarea_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    region_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(AreaExpandedV2, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    


class Page2(BaseSchema):
    # Logistic swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class AreaExpandedV2(BaseSchema):
    # Logistic swagger.json

    
    country = fields.Nested(Country, required=False)
    
    regions = fields.List(fields.Nested(RegionV2, required=False), required=False)
    


class RegionV2(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class Country(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class ServiceabilityZoneErrorResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.List(fields.Nested(ServiceabilityErrorResponse, required=False), required=False)
    


class ServiceabilityErrorResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


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
    
    name = fields.Str(required=False, allow_none=True)
    
    phone = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    country_iso_code = fields.Str(required=False)
    


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
    


class PincodeLatLongData(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


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
    
    request_uuid = fields.Str(required=False, allow_none=True)
    
    stormbreaker_uuid = fields.Str(required=False, allow_none=True)
    


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
    
    country_iso_code = fields.Str(required=False)
    


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
    


class CountryMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    phone_code = fields.Str(required=False)
    
    parent_id = fields.Str(required=False, allow_none=True)
    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    


class CountryEntityResponse(BaseSchema):
    # Logistic swagger.json

    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    parent_id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    lat_long = fields.Dict(required=False)
    
    meta = fields.Nested(CountryMetaResponse, required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    


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

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


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
    
    pre_fill = fields.Str(required=False)
    
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
    
    total = fields.Int(required=False)
    


class Localities(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


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
    


class ErrorObject(BaseSchema):
    # Logistic swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


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
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ErrorResponseV2(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    


class ErrorResponseV3(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorObject, required=False)
    


class StandardError(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    


class ShipmentRequest(BaseSchema):
    # Logistic swagger.json

    
    to_serviceability = fields.Nested(ServiceabilityNew, required=False)
    
    location_articles = fields.List(fields.Nested(LocationArticle, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class LocationArticle(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    from_serviceability = fields.Nested(ServiceabilityNew, required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Nested(Article, required=False), required=False)
    


class Article(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    attributes = fields.Nested(Attributes, required=False)
    
    category_id = fields.Int(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    brand_id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(Set, required=False)
    
    set_quantity = fields.Int(required=False)
    
    delivery_slots = fields.Nested(DeliverySlots, required=False)
    


class Weight(BaseSchema):
    # Logistic swagger.json

    
    shipping = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class Attributes(BaseSchema):
    # Logistic swagger.json

    
    battery_operated = fields.Str(required=False)
    
    is_flammable = fields.Str(required=False)
    


class Dimension(BaseSchema):
    # Logistic swagger.json

    
    height = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Int(required=False)
    


class Set(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    


class DeliverySlots(BaseSchema):
    # Logistic swagger.json

    
    delivery_date = fields.Str(required=False)
    
    min_slot = fields.Str(required=False)
    
    max_slot = fields.Str(required=False)
    


class ServiceabilityNew(BaseSchema):
    # Logistic swagger.json

    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    location = fields.Nested(Location, required=False)
    
    pincode = fields.Str(required=False)
    


class Location(BaseSchema):
    # Logistic swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    


class ShipmentResponse(BaseSchema):
    # Logistic swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    is_cod_available = fields.Boolean(required=False)
    


class Meta(BaseSchema):
    # Logistic swagger.json

    
    shipment_cost = fields.Float(required=False)
    


class ShipmentItem(BaseSchema):
    # Logistic swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    from_serviceability = fields.Nested(ServiceabilityNew, required=False)
    
    articles = fields.List(fields.Nested(Article, required=False), required=False)
    
    courier_partners = fields.List(fields.Nested(CourierPartner, required=False), required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_mto = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_locked = fields.Boolean(required=False)
    
    packaging = fields.Nested(Packaging, required=False)
    
    delivery_slots = fields.Nested(DeliverySlots, required=False)
    
    count = fields.Int(required=False)
    
    volumetric_weight = fields.Float(required=False)
    
    ewaybill_enabled = fields.Str(required=False)
    
    mps = fields.Boolean(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    weight = fields.Int(required=False)
    
    shipment_type = fields.Str(required=False)
    
    is_auto_assign = fields.Boolean(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    


class TAT(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class CourierPartner(BaseSchema):
    # Logistic swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    area_code = fields.Nested(AreaCode, required=False)
    
    tat = fields.Nested(TAT, required=False)
    
    display_name = fields.Str(required=False)
    
    is_qc_enabled = fields.Boolean(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    forward_pickup_cutoff = fields.Str(required=False)
    
    reverse_pickup_cutoff = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Logistic swagger.json

    
    customer_promise = fields.Nested(PromiseDetails, required=False)
    
    meta = fields.Nested(PromiseMeta, required=False)
    


class PromiseDetails(BaseSchema):
    # Logistic swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class Packaging(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    dimension = fields.Nested(PackagingDimension, required=False)
    


class StorePromise(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    promise = fields.Nested(PromiseDetails, required=False)
    


class GetPromiseDetails(BaseSchema):
    # Logistic swagger.json

    
    items = fields.List(fields.Nested(StorePromise, required=False), required=False)
    
    promise = fields.Nested(PromiseDetails, required=False)
    
    page = fields.Nested(Page, required=False)
    


