"""Logistics Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class BulkRegionServiceabilityTatDetails(BaseSchema):
    pass


class BulkRegionServiceabilityTatResultItemData(BaseSchema):
    pass


class ErrorResult(BaseSchema):
    pass


class FailureResult(BaseSchema):
    pass


class BulkRegionServiceabilityTatResult(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CourierAccountUpdateDetails(BaseSchema):
    pass


class RegionTatItemResult(BaseSchema):
    pass


class RegionServiceabilityItemResult(BaseSchema):
    pass


class ServiceabilityDetailsResult(BaseSchema):
    pass


class ServiceabilityDetails(BaseSchema):
    pass


class RegionServiceabilityResult(BaseSchema):
    pass


class RegionServiceabilityDetails(BaseSchema):
    pass


class RegionTatDetails(BaseSchema):
    pass


class RegionTatUpdateDetails(BaseSchema):
    pass


class RegionTatResult(BaseSchema):
    pass


class BulkRegionJobDetails(BaseSchema):
    pass


class BulkRegionResultItemData(BaseSchema):
    pass


class BulkRegionResult(BaseSchema):
    pass


class CourierAccount(BaseSchema):
    pass


class CourierAccountDetailsBody(BaseSchema):
    pass


class CourierPartnerAccountFailureResult(BaseSchema):
    pass


class CompanyCourierPartnerAccountListResult(BaseSchema):
    pass


class CourierAccountResult(BaseSchema):
    pass


class CourierPartnerSchemeModel(BaseSchema):
    pass


class CourierPartnerSchemeDetailsModel(BaseSchema):
    pass


class CourierPartnerSchemeFeatures(BaseSchema):
    pass


class ArithmeticOperations(BaseSchema):
    pass


class CourierPartnerSchemeUpdateDetails(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass


class GetCountriesItems(BaseSchema):
    pass


class HierarchyItems(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass





class BulkRegionServiceabilityTatDetails(BaseSchema):
    # Logistics swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkRegionServiceabilityTatResultItemData(BaseSchema):
    # Logistics swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    


class ErrorResult(BaseSchema):
    # Logistics swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class FailureResult(BaseSchema):
    # Logistics swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResult, required=False), required=False)
    


class BulkRegionServiceabilityTatResult(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(BulkRegionServiceabilityTatResultItemData, required=False), required=False)
    
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
    


class CourierAccountUpdateDetails(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class RegionTatItemResult(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(RegionTatResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class RegionServiceabilityItemResult(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(RegionServiceabilityResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ServiceabilityDetailsResult(BaseSchema):
    # Logistics swagger.json

    
    first_mile = fields.Boolean(required=False)
    
    last_mile = fields.Boolean(required=False)
    
    cod_limit = fields.Float(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    doorstep_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False)
    
    installation = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class ServiceabilityDetails(BaseSchema):
    # Logistics swagger.json

    
    first_mile = fields.Boolean(required=False)
    
    last_mile = fields.Boolean(required=False)
    
    cod_limit = fields.Float(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    doorstep_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False)
    
    installation = fields.Boolean(required=False)
    


class RegionServiceabilityResult(BaseSchema):
    # Logistics swagger.json

    
    country_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    first_mile = fields.Boolean(required=False)
    
    last_mile = fields.Boolean(required=False)
    
    cod_limit = fields.Float(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    doorstep_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False)
    
    installation = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class RegionServiceabilityDetails(BaseSchema):
    # Logistics swagger.json

    
    country_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    first_mile = fields.Boolean(required=False)
    
    last_mile = fields.Boolean(required=False)
    
    cod_limit = fields.Float(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    doorstep_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False)
    
    installation = fields.Boolean(required=False)
    


class RegionTatDetails(BaseSchema):
    # Logistics swagger.json

    
    from_country_code = fields.Str(required=False)
    
    from_state_code = fields.Str(required=False)
    
    from_city_code = fields.Str(required=False)
    
    from_sector_code = fields.Str(required=False)
    
    from_pincode = fields.Str(required=False)
    
    to_country_code = fields.Str(required=False)
    
    to_state_code = fields.Str(required=False)
    
    to_city_code = fields.Str(required=False)
    
    to_sector_code = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    max_delivery_time = fields.Int(required=False)
    
    min_delivery_time = fields.Int(required=False)
    


class RegionTatUpdateDetails(BaseSchema):
    # Logistics swagger.json

    
    max_delivery_time = fields.Int(required=False)
    
    min_delivery_time = fields.Int(required=False)
    


class RegionTatResult(BaseSchema):
    # Logistics swagger.json

    
    from_country_code = fields.Str(required=False)
    
    from_state_code = fields.Str(required=False)
    
    from_city_code = fields.Str(required=False)
    
    from_sector_code = fields.Str(required=False)
    
    from_pincode = fields.Str(required=False)
    
    to_country_code = fields.Str(required=False)
    
    to_state_code = fields.Str(required=False)
    
    to_city_code = fields.Str(required=False)
    
    to_sector_code = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    max_delivery_time = fields.Int(required=False)
    
    min_delivery_time = fields.Int(required=False)
    
    id = fields.Str(required=False)
    


class BulkRegionJobDetails(BaseSchema):
    # Logistics swagger.json

    
    file_path = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    region = fields.Str(required=False)
    


class BulkRegionResultItemData(BaseSchema):
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
    


class BulkRegionResult(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(BulkRegionResultItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CourierAccount(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class CourierAccountDetailsBody(BaseSchema):
    # Logistics swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class CourierPartnerAccountFailureResult(BaseSchema):
    # Logistics swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResult, required=False), required=False)
    


class CompanyCourierPartnerAccountListResult(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(CourierAccountResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CourierAccountResult(BaseSchema):
    # Logistics swagger.json

    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierPartnerSchemeModel, required=False)
    


class CourierPartnerSchemeModel(BaseSchema):
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
    


class CourierPartnerSchemeDetailsModel(BaseSchema):
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
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    


class ArithmeticOperations(BaseSchema):
    # Logistics swagger.json

    
    lt = fields.Int(required=False, allow_none=True)
    
    gt = fields.Int(required=False, allow_none=True)
    
    lte = fields.Int(required=False, allow_none=True)
    
    gte = fields.Int(required=False, allow_none=True)
    


class CourierPartnerSchemeUpdateDetails(BaseSchema):
    # Logistics swagger.json

    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class GetCountries(BaseSchema):
    # Logistics swagger.json

    
    items = fields.List(fields.Nested(GetCountriesItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetCountriesItems(BaseSchema):
    # Logistics swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(HierarchyItems, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    has_next_hierarchy = fields.Boolean(required=False)
    


class HierarchyItems(BaseSchema):
    # Logistics swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class ValidationError(BaseSchema):
    # Logistics swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class StandardError(BaseSchema):
    # Logistics swagger.json

    
    message = fields.Str(required=False)
    


