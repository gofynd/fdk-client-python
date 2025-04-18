"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema


from .enums import *



class AllAvailablePageSchema(BaseSchema):
    pass


class AvailablePageSchema(BaseSchema):
    pass


class AvailablePageSectionMetaAttributes(BaseSchema):
    pass


class SEOMetaItem(BaseSchema):
    pass


class SEOMetaItems(BaseSchema):
    pass


class SEOSitemap(BaseSchema):
    pass


class SEObreadcrumb(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class AvailablePageSeo(BaseSchema):
    pass


class AvailablePageSchemaSections(BaseSchema):
    pass


class SectionSource(BaseSchema):
    pass


class AvailablePagePredicate(BaseSchema):
    pass


class AvailablePageScreenPredicate(BaseSchema):
    pass


class AvailablePageUserPredicate(BaseSchema):
    pass


class AvailablePageRoutePredicate(BaseSchema):
    pass


class AvailablePageSchedulePredicate(BaseSchema):
    pass


class ThemesSchema(BaseSchema):
    pass


class Font(BaseSchema):
    pass


class FontVariants(BaseSchema):
    pass


class FontVariant(BaseSchema):
    pass


class Config(BaseSchema):
    pass


class ThemeConfiguration(BaseSchema):
    pass


class ThemeMeta(BaseSchema):
    pass


class ThemePayment(BaseSchema):
    pass


class Release(BaseSchema):
    pass


class Images(BaseSchema):
    pass


class Assets(BaseSchema):
    pass


class UMDJs(BaseSchema):
    pass


class CommonJS(BaseSchema):
    pass


class CSS(BaseSchema):
    pass


class SectionItem(BaseSchema):
    pass


class GlobalSchema(BaseSchema):
    pass


class SectionPreset(BaseSchema):
    pass


class ImagePickerProp(BaseSchema):
    pass


class Block(BaseSchema):
    pass


class BlockProps(BaseSchema):
    pass


class UrlProp(BaseSchema):
    pass


class Prop(BaseSchema):
    pass


class AvailablePagePlatformPredicate(BaseSchema):
    pass


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    pass


class BlitzkriegApiErrorSchema(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass





class AllAvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


class AvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sections = fields.List(fields.Nested(AvailablePageSchemaSections, required=False), required=False)
    
    sections_meta = fields.List(fields.Nested(AvailablePageSectionMetaAttributes, required=False), required=False)
    
    theme = fields.Str(required=False)
    
    seo = fields.Nested(AvailablePageSeo, required=False)
    
    props = fields.List(fields.Dict(required=False), required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class AvailablePageSectionMetaAttributes(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Dict(required=False)
    


class SEOMetaItem(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(SEOMetaItems, required=False), required=False)
    


class SEOMetaItems(BaseSchema):
    # Theme swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SEOSitemap(BaseSchema):
    # Theme swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class SEObreadcrumb(BaseSchema):
    # Theme swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    


class Action(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    


class AvailablePageSeo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    canonical_url = fields.Str(required=False)
    
    meta_tags = fields.List(fields.Nested(SEOMetaItem, required=False), required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(SEObreadcrumb, required=False), required=False)
    
    _id = fields.Str(required=False)
    


class AvailablePageSchemaSections(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    
    __source = fields.Nested(SectionSource, required=False)
    


class SectionSource(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    bundle_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    
    schedule = fields.Nested(AvailablePageSchedulePredicate, required=False)
    
    platform = fields.Nested(AvailablePagePlatformPredicate, required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class AvailablePageScreenPredicate(BaseSchema):
    # Theme swagger.json

    
    mobile = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    
    tablet = fields.Boolean(required=False)
    


class AvailablePageUserPredicate(BaseSchema):
    # Theme swagger.json

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    


class AvailablePageRoutePredicate(BaseSchema):
    # Theme swagger.json

    
    selected = fields.Str(required=False)
    
    exact_url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    


class AvailablePageSchedulePredicate(BaseSchema):
    # Theme swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class ThemesSchema(BaseSchema):
    # Theme swagger.json

    
    font = fields.Nested(Font, required=False)
    
    config = fields.Nested(Config, required=False)
    
    applied = fields.Boolean(required=False)
    
    is_private = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    marketplace_theme_id = fields.Str(required=False)
    
    meta = fields.Nested(ThemeMeta, required=False)
    
    name = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    styles = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    assets = fields.Nested(Assets, required=False)
    
    available_sections = fields.List(fields.Nested(SectionItem, required=False), required=False)
    
    theme_type = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    src = fields.Str(required=False)
    
    global_sections = fields.List(fields.Dict(required=False), required=False)
    


class Font(BaseSchema):
    # Theme swagger.json

    
    variants = fields.Nested(FontVariants, required=False)
    
    family = fields.Str(required=False)
    


class FontVariants(BaseSchema):
    # Theme swagger.json

    
    light = fields.Nested(FontVariant, required=False)
    
    regular = fields.Nested(FontVariant, required=False)
    
    medium = fields.Nested(FontVariant, required=False)
    
    semi_bold = fields.Nested(FontVariant, required=False)
    
    bold = fields.Nested(FontVariant, required=False)
    


class FontVariant(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Config(BaseSchema):
    # Theme swagger.json

    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ThemeConfiguration, required=False), required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    preset = fields.Dict(required=False)
    


class ThemeConfiguration(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Str(required=False), required=False)
    


class ThemeMeta(BaseSchema):
    # Theme swagger.json

    
    payment = fields.Nested(ThemePayment, required=False)
    
    description = fields.Str(required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    release = fields.Nested(Release, required=False)
    
    images = fields.Nested(Images, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ThemePayment(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class Release(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class Images(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class Assets(BaseSchema):
    # Theme swagger.json

    
    umd_js = fields.Nested(UMDJs, required=False)
    
    common_js = fields.Nested(CommonJS, required=False)
    
    css = fields.Nested(CSS, required=False)
    


class UMDJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class CommonJS(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class CSS(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class SectionItem(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Dict(required=False), required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Nested(SectionPreset, required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    


class GlobalSchema(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Dict(required=False), required=False)
    


class SectionPreset(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Block, required=False), required=False)
    


class ImagePickerProp(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class Block(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.Nested(BlockProps, required=False)
    


class BlockProps(BaseSchema):
    # Theme swagger.json

    
    image = fields.Nested(ImagePickerProp, required=False)
    
    slide_link = fields.Nested(UrlProp, required=False)
    


class UrlProp(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class Prop(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    info = fields.Str(required=False)
    


class AvailablePagePlatformPredicate(BaseSchema):
    # Theme swagger.json

    
    ios = fields.Boolean(required=False)
    
    android = fields.Boolean(required=False)
    
    web = fields.Boolean(required=False)
    


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegApiErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class ActionPage(BaseSchema):
    # Theme swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


