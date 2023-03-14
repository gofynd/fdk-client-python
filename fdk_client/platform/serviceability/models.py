"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class ApplicationServiceabilityConfig(BaseSchema):
    pass


class ApplicationServiceabilityResponse(BaseSchema):
    pass


class ServiceabilityErrorResponse(BaseSchema):
    pass


class ApplicationServiceabilityConfigResponse(BaseSchema):
    pass


class EntityRegionViewRequest(BaseSchema):
    pass


class EntityRegionViewItems(BaseSchema):
    pass


class EntityRegionViewError(BaseSchema):
    pass


class EntityRegionViewPage(BaseSchema):
    pass


class EntityRegionViewResponse(BaseSchema):
    pass


class ListViewChannels(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
    pass


class ListViewItems(BaseSchema):
    pass


class ListViewSummary(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
    pass


class ListViewResponse(BaseSchema):
    pass


class CompanyStoreView_PageItems(BaseSchema):
    pass


class CompanyStoreView_Response(BaseSchema):
    pass


class GetZoneDataViewChannels(BaseSchema):
    pass


class ZoneProductTypes(BaseSchema):
    pass


class ZoneMappingType(BaseSchema):
    pass


class GetZoneDataViewItems(BaseSchema):
    pass


class GetSingleZoneDataViewResponse(BaseSchema):
    pass


class UpdateZoneData(BaseSchema):
    pass


class ZoneUpdateRequest(BaseSchema):
    pass


class ZoneSuccessResponse(BaseSchema):
    pass


class CreateZoneData(BaseSchema):
    pass


class ZoneRequest(BaseSchema):
    pass


class ZoneResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    pass





class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    


class ApplicationServiceabilityResponse(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    serviceability_type = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ServiceabilityErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(ApplicationServiceabilityResponse, required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    success = fields.Boolean(required=False)
    


class EntityRegionViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    sub_type = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionViewItems(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    


class EntityRegionViewError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionViewPage(BaseSchema):
    # Serviceability swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class EntityRegionViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.List(fields.Nested(EntityRegionViewItems, required=False), required=False)
    
    error = fields.Nested(EntityRegionViewError, required=False)
    
    page = fields.Nested(EntityRegionViewPage, required=False)
    
    success = fields.Boolean(required=False)
    


class ListViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ListViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    zone_id = fields.Str(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    pincodes_count = fields.Int(required=False)
    


class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_active_zones = fields.Int(required=False)
    
    total_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    


class ZoneDataItem(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class ListViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Serviceability swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class CompanyStoreView_Response(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    


class GetZoneDataViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ZoneProductTypes(BaseSchema):
    # Serviceability swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.List(fields.Str(required=False), required=False)
    
    state = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    


class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    pincodes_count = fields.Int(required=False)
    


class GetSingleZoneDataViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    


class UpdateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    


class ZoneUpdateRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(UpdateZoneData, required=False)
    
    identifier = fields.Str(required=False)
    


class ZoneSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class CreateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    


class ZoneRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(CreateZoneData, required=False)
    
    identifier = fields.Str(required=False)
    


class ZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    


