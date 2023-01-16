"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class AppUser(BaseSchema):
    pass


class Asset(BaseSchema):
    pass


class E(BaseSchema):
    pass


class Giveaway(BaseSchema):
    pass


class GiveawayResponse(BaseSchema):
    pass


class HistoryPretty(BaseSchema):
    pass


class HistoryRes(BaseSchema):
    pass


class Offer(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class Points(BaseSchema):
    pass


class Referral(BaseSchema):
    pass


class RewardUser(BaseSchema):
    pass


class RewardsAudience(BaseSchema):
    pass


class RewardsRule(BaseSchema):
    pass


class Schedule(BaseSchema):
    pass


class ShareMessages(BaseSchema):
    pass


class UserRes(BaseSchema):
    pass



class AppUser(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    block_reason = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class Asset(BaseSchema):
    # Rewards swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class E(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Dict(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class Giveaway(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    audience = fields.Nested(RewardsAudience, required=False)
    
    banner_image = fields.Nested(Asset, required=False)
    
    created_at = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rule = fields.Nested(RewardsRule, required=False)
    
    title = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class GiveawayResponse(BaseSchema):
    # Rewards swagger.json

    
    items = fields.List(fields.Nested(Giveaway, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class HistoryPretty(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    claimed = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    remaining_points = fields.Float(required=False)
    
    text_1 = fields.Str(required=False)
    
    text_2 = fields.Str(required=False)
    
    text_3 = fields.Str(required=False)
    
    txn_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class HistoryRes(BaseSchema):
    # Rewards swagger.json

    
    items = fields.List(fields.Nested(HistoryPretty, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    points = fields.Float(required=False)
    


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
    


class Page(BaseSchema):
    # Rewards swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class Points(BaseSchema):
    # Rewards swagger.json

    
    available = fields.Float(required=False)
    


class Referral(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Str(required=False)
    


class RewardUser(BaseSchema):
    # Rewards swagger.json

    
    _id = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    referral = fields.Nested(Referral, required=False)
    
    uid = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_block_reason = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class RewardsAudience(BaseSchema):
    # Rewards swagger.json

    
    header_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class RewardsRule(BaseSchema):
    # Rewards swagger.json

    
    amount = fields.Float(required=False)
    


class Schedule(BaseSchema):
    # Rewards swagger.json

    
    cron = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    


class ShareMessages(BaseSchema):
    # Rewards swagger.json

    
    email = fields.Str(required=False)
    
    facebook = fields.Str(required=False)
    
    fallback = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    messenger = fields.Str(required=False)
    
    sms = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    twitter = fields.Str(required=False)
    
    whatsapp = fields.Str(required=False)
    


class UserRes(BaseSchema):
    # Rewards swagger.json

    
    points = fields.Nested(Points, required=False)
    
    user = fields.Nested(RewardUser, required=False)
    

