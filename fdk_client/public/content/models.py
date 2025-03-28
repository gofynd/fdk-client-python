"""Content Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class BasicDetailsPayloadSchema(BaseSchema):
    pass


class WhatsNew(BaseSchema):
    pass


class Features(BaseSchema):
    pass


class BusinessAccount(BaseSchema):
    pass


class SellerSupport(BaseSchema):
    pass


class MenuSchema(BaseSchema):
    pass


class MenusSchema(BaseSchema):
    pass


class MenuTypeSchema(BaseSchema):
    pass


class CompanyLevelMenuItemSchema(BaseSchema):
    pass


class ApplicationLevelMenuItemSchema(BaseSchema):
    pass


class VisibleOnSchema(BaseSchema):
    pass


class SalesChannelSchema(BaseSchema):
    pass


class OtherSellerSchema(BaseSchema):
    pass


class FooterContentSchema(BaseSchema):
    pass


class AnalyticsTagsSchema(BaseSchema):
    pass


class CustomPageBySlugSchema(BaseSchema):
    pass


class ItemSchema(BaseSchema):
    pass


class CreateCustomPageSeoSchema(BaseSchema):
    pass


class RawHtmlContentSchema(BaseSchema):
    pass


class FooterSchema(BaseSchema):
    pass


class HomePageContentSchema(BaseSchema):
    pass


class NavItemSchema(BaseSchema):
    pass


class NavbarSchema(BaseSchema):
    pass


class MediaSchema(BaseSchema):
    pass


class CreatedBySchema(BaseSchema):
    pass


class PricingBannerSchema(BaseSchema):
    pass


class TagsSchema(BaseSchema):
    pass


class CustomItemSchema(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class CredentialSchema(BaseSchema):
    pass


class ConfigurationSchema(BaseSchema):
    pass


class CredentialsSchema(BaseSchema):
    pass


class SDKLinksResponseSchema(BaseSchema):
    pass


class SDKLinkObjectSchema(BaseSchema):
    pass


class SDKbyTypeResponseSchema(BaseSchema):
    pass


class ContentAPIError(BaseSchema):
    pass





class BasicDetailsPayloadSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    logo_url = fields.Str(required=False)
    
    favicon_url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    meta_title = fields.Str(required=False)
    
    meta_description = fields.Str(required=False)
    
    meta_image = fields.Str(required=False)
    
    whats_new = fields.List(fields.Nested(WhatsNew, required=False), required=False)
    
    features = fields.List(fields.Nested(Features, required=False), required=False)
    
    authentication = fields.Dict(required=False)
    
    business_account = fields.Nested(BusinessAccount, required=False)
    
    seller_support = fields.Nested(SellerSupport, required=False)
    
    copyright = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    documentation_url = fields.Str(required=False)
    
    faq_url = fields.Str(required=False)
    
    facebook_url = fields.Str(required=False)
    
    instagram_url = fields.Str(required=False)
    
    privacy_url = fields.Str(required=False)
    
    twitter_url = fields.Str(required=False)
    
    termsofservice_url = fields.Str(required=False)
    


class WhatsNew(BaseSchema):
    # Content swagger.json

    
    description = fields.Str(required=False)
    


class Features(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    list = fields.List(fields.Str(required=False), required=False)
    
    image = fields.Str(required=False)
    


class BusinessAccount(BaseSchema):
    # Content swagger.json

    
    is_limit = fields.Boolean(required=False)
    
    threshold = fields.Int(required=False)
    


class SellerSupport(BaseSchema):
    # Content swagger.json

    
    email = fields.Str(required=False)
    
    phone_number = fields.Int(required=False)
    


class MenuSchema(BaseSchema):
    # Content swagger.json

    
    sales_channel = fields.Nested(SalesChannelSchema, required=False)
    
    other_seller = fields.Nested(OtherSellerSchema, required=False)
    
    footer_content = fields.Nested(FooterContentSchema, required=False)
    
    can_create_business_account = fields.Boolean(required=False)
    
    company_level = fields.List(fields.Nested(CompanyLevelMenuItemSchema, required=False), required=False)
    
    application_level = fields.List(fields.Nested(ApplicationLevelMenuItemSchema, required=False), required=False)
    


class MenusSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    desktop = fields.Nested(MenuTypeSchema, required=False)
    
    mobile = fields.Nested(MenuTypeSchema, required=False)
    
    __v = fields.Float(required=False)
    


class MenuTypeSchema(BaseSchema):
    # Content swagger.json

    
    menu = fields.Nested(MenuSchema, required=False)
    


class CompanyLevelMenuItemSchema(BaseSchema):
    # Content swagger.json

    
    visible_on = fields.Nested(VisibleOnSchema, required=False)
    
    display = fields.Str(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    is_disabled = fields.Boolean(required=False)
    
    child = fields.List(fields.Nested(lambda: CompanyLevelMenuItemSchema(exclude=('child')), required=False), required=False)
    


class ApplicationLevelMenuItemSchema(BaseSchema):
    # Content swagger.json

    
    visible_on = fields.Nested(VisibleOnSchema, required=False)
    
    display = fields.Str(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    is_disabled = fields.Boolean(required=False)
    
    child = fields.List(fields.Nested(lambda: ApplicationLevelMenuItemSchema(exclude=('child')), required=False), required=False)
    


class VisibleOnSchema(BaseSchema):
    # Content swagger.json

    
    web = fields.Boolean(required=False)
    
    ios = fields.Boolean(required=False)
    
    android = fields.Boolean(required=False)
    


class SalesChannelSchema(BaseSchema):
    # Content swagger.json

    
    can_add = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    


class OtherSellerSchema(BaseSchema):
    # Content swagger.json

    
    is_visible = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    


class FooterContentSchema(BaseSchema):
    # Content swagger.json

    
    is_visible = fields.Boolean(required=False)
    
    line_one = fields.Str(required=False)
    
    line_two = fields.Str(required=False)
    


class AnalyticsTagsSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    body_code = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    header_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CustomPageBySlugSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    content = fields.List(fields.Nested(ItemSchema, required=False), required=False)
    
    seo = fields.Nested(CreateCustomPageSeoSchema, required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    modified_by = fields.Nested(CreatedBySchema, required=False)
    
    archived = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class ItemSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CreateCustomPageSeoSchema(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class RawHtmlContentSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class FooterSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    content = fields.List(fields.Nested(RawHtmlContentSchema, required=False), required=False)
    
    footer_meta = fields.List(fields.Raw(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    modified_by = fields.Nested(CreatedBySchema, required=False)
    
    archived = fields.Boolean(required=False)
    
    __v = fields.Int(required=False)
    


class HomePageContentSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    archived = fields.Boolean(required=False)
    
    page_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class NavItemSchema(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    
    href = fields.Str(required=False)
    


class NavbarSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    items = fields.List(fields.Nested(NavItemSchema, required=False), required=False)
    
    __v = fields.Float(required=False)
    
    modified_by = fields.Nested(CreatedBySchema, required=False)
    


class MediaSchema(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    alt = fields.Str(required=False)
    
    anchor_link = fields.Str(required=False)
    


class CreatedBySchema(BaseSchema):
    # Content swagger.json

    
    user_id = fields.Str(required=False)
    


class PricingBannerSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    web_banner = fields.Nested(MediaSchema, required=False)
    
    mobile_banner = fields.Nested(MediaSchema, required=False)
    
    published = fields.Boolean(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    modified_by = fields.Nested(CreatedBySchema, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class TagsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomItemSchema, required=False), required=False)
    
    page = fields.Nested(PageSchema, required=False)
    


class CustomItemSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class PageSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Float(required=False)
    
    size = fields.Float(required=False)
    
    item_total = fields.Float(required=False)
    
    has_next = fields.Boolean(required=False)
    


class UserSchema(BaseSchema):
    # Content swagger.json

    
    user_id = fields.Str(required=False)
    


class CredentialSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    entity_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_enable = fields.Boolean(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class ConfigurationSchema(BaseSchema):
    # Content swagger.json

    
    token = fields.Str(required=False)
    
    host = fields.Str(required=False)
    


class CredentialsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CredentialSchema, required=False), required=False)
    


class SDKLinksResponseSchema(BaseSchema):
    # Content swagger.json

    
    readmes = fields.List(fields.Nested(SDKLinkObjectSchema, required=False), required=False)
    


class SDKLinkObjectSchema(BaseSchema):
    # Content swagger.json

    
    owner = fields.Str(required=False)
    
    repo = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class SDKbyTypeResponseSchema(BaseSchema):
    # Content swagger.json

    
    readme_content = fields.Str(required=False)
    


class ContentAPIError(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


