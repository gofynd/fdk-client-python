"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class RewardsArticle(BaseSchema):
    pass


class CatalogueOrderResponse(BaseSchema):
    pass


class CatalogueOrderRequest(BaseSchema):
    pass


class PointsResponse(BaseSchema):
    pass


class ReferralDetailsUser(BaseSchema):
    pass


class Offer(BaseSchema):
    pass


class Schedule(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class Asset(BaseSchema):
    pass


class ShareMessages(BaseSchema):
    pass


class ReferralDetailsResponse(BaseSchema):
    pass


class OrderDiscountRequest(BaseSchema):
    pass


class OrderDiscountRuleBucket(BaseSchema):
    pass


class DiscountProperties(BaseSchema):
    pass


class OrderDiscountResponse(BaseSchema):
    pass


class RedeemReferralCodeRequest(BaseSchema):
    pass


class RedeemReferralCodeResponse(BaseSchema):
    pass


class PointsHistoryResponse(BaseSchema):
    pass


class PointsHistory(BaseSchema):
    pass


class Page(BaseSchema):
    pass



class RewardsArticle(BaseSchema):
    # Rewards swagger.json

    
    id = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    price = fields.Float(required=False)
    


class CatalogueOrderResponse(BaseSchema):
    # Rewards swagger.json

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    


class CatalogueOrderRequest(BaseSchema):
    # Rewards swagger.json

    
    articles = fields.List(fields.Nested(RewardsArticle, required=False), required=False)
    


class PointsResponse(BaseSchema):
    # Rewards swagger.json

    
    points = fields.Float(required=False)
    


class ReferralDetailsUser(BaseSchema):
    # Rewards swagger.json

    
    blocked = fields.Boolean(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referral_code = fields.Str(required=False)
    


class Offer(BaseSchema):
    # Rewards swagger.json

    
    _schedule = fields.Nested(Schedule, required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    banner_image = fields.Nested(Asset, required=False)
    
    created_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rule = fields.Dict(required=False)
    
    share = fields.Nested(ShareMessages, required=False)
    
    sub_text = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Schedule(BaseSchema):
    # Rewards swagger.json

    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    


class Error(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Int(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class Asset(BaseSchema):
    # Rewards swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class ShareMessages(BaseSchema):
    # Rewards swagger.json

    
    email = fields.Int(required=False)
    
    facebook = fields.Str(required=False)
    
    fallback = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    messenger = fields.Str(required=False)
    
    sms = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    twitter = fields.Str(required=False)
    
    whatsapp = fields.Str(required=False)
    


class ReferralDetailsResponse(BaseSchema):
    # Rewards swagger.json

    
    referral = fields.Nested(Offer, required=False)
    
    share = fields.Nested(ShareMessages, required=False)
    
    user = fields.Nested(ReferralDetailsUser, required=False)
    
    referrer_info = fields.Str(required=False)
    
    terms_conditions_link = fields.Str(required=False)
    


class OrderDiscountRequest(BaseSchema):
    # Rewards swagger.json

    
    order_amount = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class OrderDiscountRuleBucket(BaseSchema):
    # Rewards swagger.json

    
    high = fields.Float(required=False)
    
    low = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    value_type = fields.Str(required=False)
    


class DiscountProperties(BaseSchema):
    # Rewards swagger.json

    
    absolute = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    display_absolute = fields.Str(required=False)
    
    display_percent = fields.Str(required=False)
    
    percent = fields.Float(required=False)
    


class OrderDiscountResponse(BaseSchema):
    # Rewards swagger.json

    
    order_amount = fields.Float(required=False)
    
    points = fields.Float(required=False)
    
    discount = fields.Nested(DiscountProperties, required=False)
    
    base_discount = fields.Nested(DiscountProperties, required=False)
    
    applied_rule_bucket = fields.Nested(OrderDiscountRuleBucket, required=False)
    


class RedeemReferralCodeRequest(BaseSchema):
    # Rewards swagger.json

    
    device_id = fields.Str(required=False)
    
    referral_code = fields.Str(required=False)
    


class RedeemReferralCodeResponse(BaseSchema):
    # Rewards swagger.json

    
    redeemed = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    referrer_info = fields.Str(required=False)
    
    referrer_id = fields.Str(required=False)
    
    points = fields.Float(required=False)
    


class PointsHistoryResponse(BaseSchema):
    # Rewards swagger.json

    
    items = fields.List(fields.Nested(PointsHistory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PointsHistory(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    claimed = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    points = fields.Float(required=False)
    
    remaining_points = fields.Float(required=False)
    
    text_1 = fields.Str(required=False)
    
    text_2 = fields.Str(required=False)
    
    text_3 = fields.Str(required=False)
    
    txn_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class Page(BaseSchema):
    # Rewards swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


