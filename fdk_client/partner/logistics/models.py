"""Logistics Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class ErrorResponseV1(BaseSchema):
    pass


class BulkRegionServiceabilityTatRequest(BaseSchema):
    pass


class BulkRegionServiceabilityTatResponseItemData(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class FailureResponse(BaseSchema):
    pass


class BulkRegionServiceabilityTatResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class BulkRegionJobSerializer(BaseSchema):
    pass


class BulkRegionResponseItemData(BaseSchema):
    pass


class BulkRegionResponse(BaseSchema):
    pass


class CourierAccount(BaseSchema):
    pass


class CourierPartnerAccountFailureResponse(BaseSchema):
    pass


class CompanyCourierPartnerAccountListResponse(BaseSchema):
    pass


class CourierAccountSchemeResponse(BaseSchema):
    pass


class CourierAccountResponse(BaseSchema):
    pass


class CourierPartnerSchemeModel(BaseSchema):
    pass


class CourierPartnerSchemeFeatures(BaseSchema):
    pass


class ArithmeticOperations(BaseSchema):
    pass


class CourierPartnerSchemeUpdateRequest(BaseSchema):
    pass


class CountryHierarchy(BaseSchema):
    pass


class CurrencyObject(BaseSchema):
    pass


class CountryObject(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass





class ErrorResponseV1(BaseSchema):
    # Logistics swagger.json

    
    error = fields.Str(required=False)
    


class BulkRegionServiceabilityTatRequest(BaseSchema):
    # Logistics swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkRegionServiceabilityTatResponseItemData(BaseSchema):
    # Logistics swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    


class ErrorResponse(BaseSchema):
    # Logistics swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class FailureResponse(BaseSchema):
    # Logistics swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class BulkRegionServiceabilityTatResponse(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(BulkRegionServiceabilityTatResponseItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Logistics swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class BulkRegionJobSerializer(BaseSchema):
    # Logistics swagger.json

    
    file_path = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    region = fields.Str(required=False)
    


class BulkRegionResponseItemData(BaseSchema):
    # Logistics swagger.json

    
    file_path = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    action = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    success = fields.Int(required=False)
    
    region = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    error_file_path = fields.Str(required=False)
    


class BulkRegionResponse(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(BulkRegionResponseItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CourierAccount(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class CourierPartnerAccountFailureResponse(BaseSchema):
    # Logistics swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class CompanyCourierPartnerAccountListResponse(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(CourierAccountResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CourierAccountSchemeResponse(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierAccountResponse(BaseSchema):
    # Logistics swagger.json

    
    company_id = fields.Int(required=False)
    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierAccountSchemeResponse, required=False)
    


class CourierPartnerSchemeModel(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierPartnerSchemeFeatures(BaseSchema):
    # Logistics swagger.json

    
    doorstep_qc = fields.Boolean(required=False)
    
    qr = fields.Boolean(required=False)
    
    mps = fields.Boolean(required=False)
    
    ndr = fields.Boolean(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    dangerous_goods = fields.Boolean(required=False)
    
    fragile_goods = fields.Boolean(required=False)
    
    restricted_goods = fields.Boolean(required=False)
    
    cold_storage_goods = fields.Boolean(required=False)
    
    doorstep_exchange = fields.Boolean(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    product_installation = fields.Boolean(required=False)
    
    openbox_delivery = fields.Boolean(required=False)
    
    status_updates = fields.Str(required=False)
    
    multi_pick_single_drop = fields.Boolean(required=False)
    
    single_pick_multi_drop = fields.Boolean(required=False)
    
    multi_pick_multi_drop = fields.Boolean(required=False)
    
    ewaybill = fields.Boolean(required=False)
    


class ArithmeticOperations(BaseSchema):
    # Logistics swagger.json

    
    lt = fields.Int(required=False, allow_none=True)
    
    gt = fields.Int(required=False, allow_none=True)
    
    lte = fields.Int(required=False, allow_none=True)
    
    gte = fields.Int(required=False, allow_none=True)
    


class CourierPartnerSchemeUpdateRequest(BaseSchema):
    # Logistics swagger.json

    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CountryHierarchy(BaseSchema):
    # Logistics swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class CurrencyObject(BaseSchema):
    # Logistics swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CountryObject(BaseSchema):
    # Logistics swagger.json

    
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
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(CountryObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


