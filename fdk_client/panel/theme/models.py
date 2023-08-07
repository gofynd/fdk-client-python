"""Theme Panel Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PanelModel import BaseSchema




class MarketplaceThemeResponseBody(BaseSchema):
    pass


class MarketplaceTheme(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class ContactInfo(BaseSchema):
    pass


class CatalogSize(BaseSchema):
    pass


class MarketplaceThemeImages(BaseSchema):
    pass


class CarouselItem(BaseSchema):
    pass


class ExploreInfo(BaseSchema):
    pass


class Feature(BaseSchema):
    pass


class FeatureItem(BaseSchema):
    pass


class Highlight(BaseSchema):
    pass


class Variation(BaseSchema):
    pass


class Documentation(BaseSchema):
    pass


class Comments(BaseSchema):
    pass


class Release(BaseSchema):
    pass


class ThemeSlugResponse(BaseSchema):
    pass


class Organization(BaseSchema):
    pass


class OrganizationMeta(BaseSchema):
    pass


class ThemeCreator(BaseSchema):
    pass


class PhoneNumber(BaseSchema):
    pass


class Email(BaseSchema):
    pass


class ThemeAndUserDetailsResponse(BaseSchema):
    pass


class PaginationSchema(BaseSchema):
    pass





class MarketplaceThemeResponseBody(BaseSchema):
    # Theme swagger.json

    
    items = fields.List(fields.Nested(MarketplaceTheme, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class MarketplaceTheme(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    payment = fields.Nested(PaymentInfo, required=False)
    
    contact = fields.Nested(ContactInfo, required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    is_update = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    tagline = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    catalog_size = fields.Nested(CatalogSize, required=False)
    
    images = fields.Nested(MarketplaceThemeImages, required=False)
    
    carousel = fields.List(fields.Nested(CarouselItem, required=False), required=False)
    
    src = fields.Str(required=False)
    
    explore = fields.Nested(ExploreInfo, required=False)
    
    features = fields.List(fields.Nested(Feature, required=False), required=False)
    
    highlights = fields.List(fields.Nested(Highlight, required=False), required=False)
    
    variations = fields.List(fields.Nested(Variation, required=False), required=False)
    
    documentation = fields.Nested(Documentation, required=False)
    
    status = fields.Str(required=False)
    
    step = fields.Int(required=False)
    
    comments = fields.Nested(Comments, required=False)
    
    release = fields.Nested(Release, required=False)
    
    slug = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    


class PaymentInfo(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class ContactInfo(BaseSchema):
    # Theme swagger.json

    
    developer_contact = fields.List(fields.Str(required=False), required=False)
    
    seller_contact = fields.Str(required=False)
    


class CatalogSize(BaseSchema):
    # Theme swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class MarketplaceThemeImages(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class CarouselItem(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class ExploreInfo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Feature(BaseSchema):
    # Theme swagger.json

    
    category = fields.Str(required=False)
    
    list = fields.List(fields.Nested(FeatureItem, required=False), required=False)
    


class FeatureItem(BaseSchema):
    # Theme swagger.json

    
    label = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Highlight(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    


class Variation(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    demo_url = fields.Str(required=False)
    
    images = fields.Nested(MarketplaceThemeImages, required=False)
    


class Documentation(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Comments(BaseSchema):
    # Theme swagger.json

    
    developer_remark = fields.Str(required=False)
    
    reviewer_feedback = fields.Str(required=False)
    


class Release(BaseSchema):
    # Theme swagger.json

    
    version = fields.Str(required=False)
    
    notes = fields.Str(required=False)
    


class ThemeSlugResponse(BaseSchema):
    # Theme swagger.json

    
    theme = fields.Nested(MarketplaceTheme, required=False)
    
    organization = fields.Nested(Organization, required=False)
    
    user = fields.List(fields.Nested(ThemeCreator, required=False), required=False)
    


class Organization(BaseSchema):
    # Theme swagger.json

    
    meta = fields.Nested(OrganizationMeta, required=False)
    
    _id = fields.Str(required=False)
    


class OrganizationMeta(BaseSchema):
    # Theme swagger.json

    
    ecomm_platform_used = fields.List(fields.Str(required=False), required=False)
    
    goals = fields.List(fields.Str(required=False), required=False)
    


class ThemeCreator(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    phone_numbers = fields.List(fields.Nested(PhoneNumber, required=False), required=False)
    
    emails = fields.List(fields.Nested(Email, required=False), required=False)
    


class PhoneNumber(BaseSchema):
    # Theme swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class Email(BaseSchema):
    # Theme swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    


class ThemeAndUserDetailsResponse(BaseSchema):
    # Theme swagger.json

    
    themes = fields.List(fields.Nested(MarketplaceTheme, required=False), required=False)
    
    user = fields.List(fields.Nested(ThemeCreator, required=False), required=False)
    


class PaginationSchema(BaseSchema):
    # Theme swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


