"""Partner Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ExtensionResponse(BaseSchema):
    pass


class ExtensionListItems(BaseSchema):
    pass


class ExtensionCommon(BaseSchema):
    pass


class ExtensionList(BaseSchema):
    pass


class ExtensionItems(BaseSchema):
    pass


class Scope(BaseSchema):
    pass


class Pagination(BaseSchema):
    pass


class ExtensionSuggestionList(BaseSchema):
    pass


class OrganizationBasicInfo(BaseSchema):
    pass


class ExtensionSuggestion(BaseSchema):
    pass


class Plan(BaseSchema):
    pass


class ListingInfo(BaseSchema):
    pass


class Callback(BaseSchema):
    pass


class Logo(BaseSchema):
    pass


class Category(BaseSchema):
    pass


class CommingSoon(BaseSchema):
    pass


class ContactInfo(BaseSchema):
    pass


class Benefits(BaseSchema):
    pass


class Screenshots(BaseSchema):
    pass


class ExtensionDetails(BaseSchema):
    pass


class Plans(BaseSchema):
    pass


class PublicExtension(BaseSchema):
    pass


class CategoryL1(BaseSchema):
    pass


class CategoryL2(BaseSchema):
    pass


class Support(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class UninstallExtension(BaseSchema):
    pass


class SubscriptionRequest(BaseSchema):
    pass


class SubscriptionRes(BaseSchema):
    pass


class PartnerInviteDetails(BaseSchema):
    pass


class ApprovedPermissions(BaseSchema):
    pass


class RequestedPermissions(BaseSchema):
    pass


class ModifyPartnerReq(BaseSchema):
    pass


class ApprovedPermissionsInfo(BaseSchema):
    pass


class ApplicationPermissions(BaseSchema):
    pass


class PartnerRequestList(BaseSchema):
    pass


class PartnerList(BaseSchema):
    pass


class SetupProductRes(BaseSchema):
    pass


class AddProxyReq(BaseSchema):
    pass


class AddProxyResponse(BaseSchema):
    pass


class getProxyPathRes(BaseSchema):
    pass


class RemoveProxyResponse(BaseSchema):
    pass


class APIError(BaseSchema):
    pass





class ExtensionResponse(BaseSchema):
    # Partner swagger.json

    
    items = fields.List(fields.Nested(ExtensionListItems, required=False), required=False)
    
    page = fields.Nested(Pagination, required=False)
    


class ExtensionListItems(BaseSchema):
    # Partner swagger.json

    
    base_url = fields.Str(required=False)
    
    callbacks = fields.Nested(Callback, required=False)
    
    contact_email = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    developed_by_name = fields.Str(required=False)
    
    ext_version = fields.Str(required=False)
    
    extention_type = fields.Str(required=False)
    
    is_application_level = fields.Boolean(required=False)
    
    is_coming_soon = fields.Boolean(required=False)
    
    is_saleschannel = fields.Boolean(required=False)
    
    logo = fields.Nested(Logo, required=False)
    
    name = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    modified_at = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    whitelisted_urls = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    


class ExtensionCommon(BaseSchema):
    # Partner swagger.json

    
    base_url = fields.Str(required=False)
    
    callbacks = fields.Nested(Callback, required=False)
    
    contact_email = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    developed_by_name = fields.Str(required=False)
    
    ext_version = fields.Str(required=False)
    
    extention_type = fields.Str(required=False)
    
    is_application_level = fields.Boolean(required=False)
    
    is_coming_soon = fields.Boolean(required=False)
    
    is_saleschannel = fields.Boolean(required=False)
    
    logo = fields.Nested(Logo, required=False)
    
    name = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    


class ExtensionList(BaseSchema):
    # Partner swagger.json

    
    items = fields.List(fields.Nested(ExtensionItems, required=False), required=False)
    
    page = fields.Nested(Pagination, required=False)
    


class ExtensionItems(BaseSchema):
    # Partner swagger.json

    
    base_url = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    developed_by_name = fields.Str(required=False)
    
    ext_version = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    extention_type = fields.Str(required=False)
    
    installed = fields.Boolean(required=False)
    
    is_saleschannel = fields.Boolean(required=False)
    
    launch_url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Logo, required=False)
    
    scope = fields.List(fields.Nested(Scope, required=False), required=False)
    


class Scope(BaseSchema):
    # Partner swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Pagination(BaseSchema):
    # Partner swagger.json

    
    current = fields.Float(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Float(required=False)
    
    size = fields.Float(required=False)
    
    type = fields.Str(required=False)
    


class ExtensionSuggestionList(BaseSchema):
    # Partner swagger.json

    
    items = fields.List(fields.Nested(ExtensionSuggestion, required=False), required=False)
    


class OrganizationBasicInfo(BaseSchema):
    # Partner swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class ExtensionSuggestion(BaseSchema):
    # Partner swagger.json

    
    listing_info = fields.Nested(ListingInfo, required=False)
    
    organization = fields.Nested(OrganizationBasicInfo, required=False)
    
    organization_id = fields.Str(required=False)
    
    plans = fields.List(fields.Nested(Plan, required=False), required=False)
    
    slug = fields.Str(required=False)
    


class Plan(BaseSchema):
    # Partner swagger.json

    
    additional_charges = fields.Str(required=False)
    
    features = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    trial_days = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(Price, required=False)
    


class ListingInfo(BaseSchema):
    # Partner swagger.json

    
    icon = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tagline = fields.Str(required=False)
    
    keywords = fields.List(fields.Str(required=False), required=False)
    


class Callback(BaseSchema):
    # Partner swagger.json

    
    auth = fields.Str(required=False)
    
    auto_install = fields.Str(required=False)
    
    install = fields.Str(required=False)
    
    setup = fields.Str(required=False)
    
    uninstall = fields.Str(required=False)
    


class Logo(BaseSchema):
    # Partner swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class Category(BaseSchema):
    # Partner swagger.json

    
    category_l1 = fields.List(fields.Nested(CategoryL1, required=False), required=False)
    
    category_l2 = fields.List(fields.Nested(CategoryL2, required=False), required=False)
    


class CommingSoon(BaseSchema):
    # Partner swagger.json

    
    is_coming_soon = fields.Boolean(required=False)
    
    upvote_count = fields.Float(required=False)
    


class ContactInfo(BaseSchema):
    # Partner swagger.json

    
    support = fields.Nested(Support, required=False)
    


class Benefits(BaseSchema):
    # Partner swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Screenshots(BaseSchema):
    # Partner swagger.json

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    mobile = fields.List(fields.Str(required=False), required=False)
    


class ExtensionDetails(BaseSchema):
    # Partner swagger.json

    
    benefits = fields.List(fields.Nested(Benefits, required=False), required=False)
    
    demo_url = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    integration = fields.List(fields.Str(required=False), required=False)
    
    video_url = fields.List(fields.Dict(required=False), required=False)
    
    youtube = fields.List(fields.Str(required=False), required=False)
    
    screenshots = fields.Nested(Screenshots, required=False)
    


class Plans(BaseSchema):
    # Partner swagger.json

    
    additional_charges = fields.Str(required=False)
    
    features = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Nested(Price, required=False)
    
    trial_days = fields.Float(required=False)
    
    type = fields.Str(required=False)
    


class PublicExtension(BaseSchema):
    # Partner swagger.json

    
    category = fields.Nested(Category, required=False)
    
    coming_soon = fields.Nested(CommingSoon, required=False)
    
    contact_info = fields.Nested(ContactInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    details = fields.Nested(ExtensionDetails, required=False)
    
    extension_id = fields.Str(required=False)
    
    is_coming_soon = fields.Boolean(required=False)
    
    listing_info = fields.Nested(ListingInfo, required=False)
    
    modified_at = fields.Str(required=False)
    
    organization = fields.Nested(OrganizationBasicInfo, required=False)
    
    organization_id = fields.Str(required=False)
    
    plan_type = fields.Str(required=False)
    
    plans = fields.List(fields.Nested(Plans, required=False), required=False)
    
    plans_url = fields.Str(required=False)
    
    review_instructions = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class CategoryL1(BaseSchema):
    # Partner swagger.json

    
    description = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    level = fields.Float(required=False)
    
    logo = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class CategoryL2(BaseSchema):
    # Partner swagger.json

    
    parent = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    level = fields.Float(required=False)
    
    slug = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class Support(BaseSchema):
    # Partner swagger.json

    
    email = fields.Str(required=False)
    
    faq_url = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    privacy_policy_url = fields.Str(required=False)
    
    website_url = fields.Str(required=False)
    


class Price(BaseSchema):
    # Partner swagger.json

    
    amount = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class UninstallExtension(BaseSchema):
    # Partner swagger.json

    
    success = fields.Boolean(required=False)
    


class SubscriptionRequest(BaseSchema):
    # Partner swagger.json

    
    approved = fields.Str(required=False)
    
    client_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    credit_balance = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class SubscriptionRes(BaseSchema):
    # Partner swagger.json

    
    redirect_url = fields.Str(required=False)
    


class PartnerInviteDetails(BaseSchema):
    # Partner swagger.json

    
    account_type = fields.Str(required=False)
    
    approved_permissions = fields.Nested(ApprovedPermissions, required=False)
    
    comment = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    company_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    organization_name = fields.Str(required=False)
    
    request_status = fields.Str(required=False)
    
    requested_permissions = fields.Nested(RequestedPermissions, required=False)
    
    user_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class ApprovedPermissions(BaseSchema):
    # Partner swagger.json

    
    application_role = fields.List(fields.Str(required=False), required=False)
    
    company_permissions = fields.List(fields.Str(required=False), required=False)
    
    company_role = fields.List(fields.Str(required=False), required=False)
    


class RequestedPermissions(BaseSchema):
    # Partner swagger.json

    
    application_permissions = fields.List(fields.Str(required=False), required=False)
    
    application_role = fields.List(fields.Str(required=False), required=False)
    
    company_permissions = fields.List(fields.Str(required=False), required=False)
    
    company_role = fields.List(fields.Str(required=False), required=False)
    


class ModifyPartnerReq(BaseSchema):
    # Partner swagger.json

    
    account_type = fields.Str(required=False)
    
    approved_permissions = fields.Nested(ApprovedPermissionsInfo, required=False)
    
    comment = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    company_name = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    organization_name = fields.Str(required=False)
    
    request_status = fields.Str(required=False)
    
    requested_permissions = fields.Nested(RequestedPermissions, required=False)
    
    user_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class ApprovedPermissionsInfo(BaseSchema):
    # Partner swagger.json

    
    application_permissions = fields.Dict(required=False)
    
    company_permissions = fields.List(fields.Str(required=False), required=False)
    


class ApplicationPermissions(BaseSchema):
    # Partner swagger.json

    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    roles = fields.List(fields.Str(required=False), required=False)
    


class PartnerRequestList(BaseSchema):
    # Partner swagger.json

    
    items = fields.Nested(PartnerList, required=False)
    
    page = fields.Nested(Pagination, required=False)
    


class PartnerList(BaseSchema):
    # Partner swagger.json

    
    account_type = fields.Str(required=False)
    
    approved_permissions = fields.Nested(ApprovedPermissionsInfo, required=False)
    
    approver_id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    company_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    organization_name = fields.Str(required=False)
    
    request_status = fields.Str(required=False)
    
    requested_permissions = fields.Nested(RequestedPermissions, required=False)
    
    user_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class SetupProductRes(BaseSchema):
    # Partner swagger.json

    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    next_step = fields.Float(required=False)
    
    cli_wait_time = fields.Float(required=False)
    


class AddProxyReq(BaseSchema):
    # Partner swagger.json

    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    


class AddProxyResponse(BaseSchema):
    # Partner swagger.json

    
    _id = fields.Str(required=False)
    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class getProxyPathRes(BaseSchema):
    # Partner swagger.json

    
    page = fields.Nested(Pagination, required=False)
    
    items = fields.List(fields.Nested(AddProxyResponse, required=False), required=False)
    


class RemoveProxyResponse(BaseSchema):
    # Partner swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


class APIError(BaseSchema):
    # Partner swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


