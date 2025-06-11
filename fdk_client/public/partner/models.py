"""Partner Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class CategoryL1(BaseSchema):
    pass


class CategoryL2(BaseSchema):
    pass


class CategoryCommon(BaseSchema):
    pass


class ContactInfo(BaseSchema):
    pass


class ExtensionUsingSlug(BaseSchema):
    pass


class Organization(BaseSchema):
    pass


class ListingInfo(BaseSchema):
    pass


class Benefits(BaseSchema):
    pass


class Screenshots(BaseSchema):
    pass


class Details(BaseSchema):
    pass


class Support(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class Plans(BaseSchema):
    pass


class Recurring(BaseSchema):
    pass





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
    


class CategoryCommon(BaseSchema):
    # Partner swagger.json

    
    category_l1 = fields.List(fields.Nested(CategoryL1, required=False), required=False)
    
    category_l2 = fields.List(fields.Nested(CategoryL2, required=False), required=False)
    


class ContactInfo(BaseSchema):
    # Partner swagger.json

    
    support = fields.Nested(Support, required=False)
    


class ExtensionUsingSlug(BaseSchema):
    # Partner swagger.json

    
    category = fields.Nested(CategoryCommon, required=False)
    
    contact_info = fields.Nested(ContactInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    details = fields.Nested(Details, required=False)
    
    extension_id = fields.Str(required=False)
    
    is_coming_soon = fields.Boolean(required=False)
    
    listing_info = fields.Nested(ListingInfo, required=False)
    
    modified_at = fields.Str(required=False)
    
    organization = fields.Nested(Organization, required=False)
    
    organization_id = fields.Str(required=False)
    
    plan_type = fields.Str(required=False)
    
    plans = fields.List(fields.Nested(Plans, required=False), required=False)
    
    plans_url = fields.Str(required=False)
    
    review_instructions = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class Organization(BaseSchema):
    # Partner swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class ListingInfo(BaseSchema):
    # Partner swagger.json

    
    icon = fields.Str(required=False)
    
    keywords = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    tagline = fields.Str(required=False)
    


class Benefits(BaseSchema):
    # Partner swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Screenshots(BaseSchema):
    # Partner swagger.json

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    mobile = fields.List(fields.Str(required=False), required=False)
    


class Details(BaseSchema):
    # Partner swagger.json

    
    benefits = fields.List(fields.Nested(Benefits, required=False), required=False)
    
    demo_url = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    integration = fields.List(fields.Str(required=False), required=False)
    
    video_url = fields.List(fields.Dict(required=False), required=False)
    
    youtube = fields.List(fields.Str(required=False), required=False)
    
    screenshots = fields.Nested(Screenshots, required=False)
    


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
    


class Plans(BaseSchema):
    # Partner swagger.json

    
    additional_charges = fields.Str(required=False)
    
    features = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    trial_days = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    price = fields.Nested(Price, required=False)
    
    recurring = fields.Nested(Recurring, required=False)
    


class Recurring(BaseSchema):
    # Partner swagger.json

    
    recurring_time = fields.Float(required=False)
    
    yearly_amount = fields.Float(required=False)
    
    type = fields.Str(required=False)
    


