"""Share Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ClickStatsResponse(BaseSchema):
    pass


class ClickStatsItem(BaseSchema):
    pass


class RedirectDevice(BaseSchema):
    pass


class WebRedirect(BaseSchema):
    pass


class Redirects(BaseSchema):
    pass


class CampaignShortLink(BaseSchema):
    pass


class Attribution(BaseSchema):
    pass


class SocialMediaTags(BaseSchema):
    pass


class ShortLinkReq(BaseSchema):
    pass


class UrlInfo(BaseSchema):
    pass


class ShortLinkRes(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ShortLinkList(BaseSchema):
    pass


class ErrorRes(BaseSchema):
    pass





class ClickStatsResponse(BaseSchema):
    # Share swagger.json

    
    click_stats = fields.List(fields.Nested(ClickStatsItem, required=False), required=False)
    


class ClickStatsItem(BaseSchema):
    # Share swagger.json

    
    display = fields.Str(required=False)
    
    total = fields.Int(required=False)
    


class RedirectDevice(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class WebRedirect(BaseSchema):
    # Share swagger.json

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Redirects(BaseSchema):
    # Share swagger.json

    
    ios = fields.Nested(RedirectDevice, required=False)
    
    android = fields.Nested(RedirectDevice, required=False)
    
    web = fields.Nested(WebRedirect, required=False)
    
    force_web = fields.Boolean(required=False)
    


class CampaignShortLink(BaseSchema):
    # Share swagger.json

    
    source = fields.Str(required=False)
    
    medium = fields.Str(required=False)
    


class Attribution(BaseSchema):
    # Share swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    


class SocialMediaTags(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    


class ShortLinkReq(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    expire_at = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    personalized = fields.Boolean(required=False)
    
    campaign = fields.Nested(CampaignShortLink, required=False)
    
    redirects = fields.Nested(Redirects, required=False)
    
    attribution = fields.Nested(Attribution, required=False)
    
    social_media_tags = fields.Nested(SocialMediaTags, required=False)
    
    count = fields.Int(required=False)
    


class UrlInfo(BaseSchema):
    # Share swagger.json

    
    original = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    


class ShortLinkRes(BaseSchema):
    # Share swagger.json

    
    title = fields.Str(required=False)
    
    url = fields.Nested(UrlInfo, required=False)
    
    created_by = fields.Str(required=False)
    
    app_redirect = fields.Boolean(required=False)
    
    fallback = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    expire_at = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    updated_at = fields.Str(required=False)
    
    personalized = fields.Boolean(required=False)
    
    campaign = fields.Nested(CampaignShortLink, required=False)
    
    redirects = fields.Nested(Redirects, required=False)
    
    attribution = fields.Nested(Attribution, required=False)
    
    social_media_tags = fields.Nested(SocialMediaTags, required=False)
    
    count = fields.Int(required=False)
    


class Page(BaseSchema):
    # Share swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class ShortLinkList(BaseSchema):
    # Share swagger.json

    
    items = fields.List(fields.Nested(ShortLinkRes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ErrorRes(BaseSchema):
    # Share swagger.json

    
    message = fields.Str(required=False)
    


