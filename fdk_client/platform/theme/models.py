"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class AvailablePageSchema(BaseSchema):
    pass


class AvailablePageSectionMetaAttributes(BaseSchema):
    pass


class AvailablePageSeo(BaseSchema):
    pass


class AvailablePageSchemaSections(BaseSchema):
    pass


class AvailablePageScreenPredicate(BaseSchema):
    pass


class AvailablePageUserPredicate(BaseSchema):
    pass


class AvailablePageRoutePredicate(BaseSchema):
    pass


class AvailablePagePredicate(BaseSchema):
    pass


class AllAvailablePageSchema(BaseSchema):
    pass


class PaginationSchema(BaseSchema):
    pass


class ThemesListingResponseSchema(BaseSchema):
    pass


class AddThemeRequestSchema(BaseSchema):
    pass


class UpgradableThemeSchema(BaseSchema):
    pass


class FontsSchema(BaseSchema):
    pass


class BlitzkriegApiErrorSchema(BaseSchema):
    pass


class BlitzkriegNotFoundSchema(BaseSchema):
    pass


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    pass


class FontsSchemaItems(BaseSchema):
    pass


class FontsSchemaItemsFiles(BaseSchema):
    pass


class ThemesSchema(BaseSchema):
    pass


class availableSectionSchema(BaseSchema):
    pass


class Information(BaseSchema):
    pass


class Images(BaseSchema):
    pass


class Src(BaseSchema):
    pass


class AssetsSchema(BaseSchema):
    pass


class UmdJs(BaseSchema):
    pass


class CommonJs(BaseSchema):
    pass


class Css(BaseSchema):
    pass


class Sections(BaseSchema):
    pass


class Config(BaseSchema):
    pass


class Preset(BaseSchema):
    pass


class GlobalSchema(BaseSchema):
    pass


class ListSchemaItem(BaseSchema):
    pass


class Colors(BaseSchema):
    pass


class Custom(BaseSchema):
    pass


class ConfigPage(BaseSchema):
    pass


class Font(BaseSchema):
    pass


class Variants(BaseSchema):
    pass


class Medium(BaseSchema):
    pass


class SemiBold(BaseSchema):
    pass


class Bold(BaseSchema):
    pass


class Light(BaseSchema):
    pass


class Regular(BaseSchema):
    pass


class Blocks(BaseSchema):
    pass


class GlobalSchemaProps(BaseSchema):
    pass


class BlocksProps(BaseSchema):
    pass





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
    
    _id = fields.Str(required=False)
    


class AvailablePageSectionMetaAttributes(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Dict(required=False)
    


class AvailablePageSeo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class AvailablePageSchemaSections(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    


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
    


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    


class AllAvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


class PaginationSchema(BaseSchema):
    # Theme swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class ThemesListingResponseSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.List(fields.Nested(ThemesSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class AddThemeRequestSchema(BaseSchema):
    # Theme swagger.json

    
    theme_id = fields.Str(required=False)
    


class UpgradableThemeSchema(BaseSchema):
    # Theme swagger.json

    
    parent_theme = fields.Str(required=False)
    
    applied_theme = fields.Str(required=False)
    
    upgrade = fields.Boolean(required=False)
    


class FontsSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.Nested(FontsSchemaItems, required=False)
    
    kind = fields.Str(required=False)
    


class BlitzkriegApiErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegNotFoundSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class FontsSchemaItems(BaseSchema):
    # Theme swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.List(fields.Str(required=False), required=False)
    
    subsets = fields.List(fields.Str(required=False), required=False)
    
    version = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    files = fields.Nested(FontsSchemaItemsFiles, required=False)
    
    category = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    


class FontsSchemaItemsFiles(BaseSchema):
    # Theme swagger.json

    
    regular = fields.Str(required=False)
    
    italic = fields.Str(required=False)
    
    bold = fields.Str(required=False)
    


class ThemesSchema(BaseSchema):
    # Theme swagger.json

    
    application = fields.Str(required=False)
    
    applied = fields.Boolean(required=False)
    
    customized = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    parent_theme_version = fields.Str(required=False)
    
    parent_theme = fields.Str(required=False)
    
    information = fields.Nested(Information, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    src = fields.Nested(Src, required=False)
    
    assets = fields.Nested(AssetsSchema, required=False)
    
    available_sections = fields.List(fields.Nested(availableSectionSchema, required=False), required=False)
    
    styles = fields.Dict(required=False)
    
    config = fields.Nested(Config, required=False)
    
    font = fields.Nested(Font, required=False)
    
    _id = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    colors = fields.Nested(Colors, required=False)
    


class availableSectionSchema(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Blocks, required=False), required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    


class Information(BaseSchema):
    # Theme swagger.json

    
    images = fields.Nested(Images, required=False)
    
    features = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Images(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    android = fields.List(fields.Str(required=False), required=False)
    
    ios = fields.List(fields.Str(required=False), required=False)
    
    thumbnail = fields.List(fields.Str(required=False), required=False)
    


class Src(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class AssetsSchema(BaseSchema):
    # Theme swagger.json

    
    umd_js = fields.Nested(UmdJs, required=False)
    
    common_js = fields.Nested(CommonJs, required=False)
    
    css = fields.Nested(Css, required=False)
    


class UmdJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class CommonJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class Css(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class Sections(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Str(required=False)
    


class Config(BaseSchema):
    # Theme swagger.json

    
    preset = fields.Nested(Preset, required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ListSchemaItem, required=False), required=False)
    


class Preset(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


class GlobalSchema(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    


class ListSchemaItem(BaseSchema):
    # Theme swagger.json

    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ConfigPage, required=False), required=False)
    
    name = fields.Str(required=False)
    


class Colors(BaseSchema):
    # Theme swagger.json

    
    bg_color = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    


class Custom(BaseSchema):
    # Theme swagger.json

    
    props = fields.Dict(required=False)
    


class ConfigPage(BaseSchema):
    # Theme swagger.json

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    


class Font(BaseSchema):
    # Theme swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    


class Variants(BaseSchema):
    # Theme swagger.json

    
    medium = fields.Nested(Medium, required=False)
    
    semi_bold = fields.Nested(SemiBold, required=False)
    
    bold = fields.Nested(Bold, required=False)
    
    light = fields.Nested(Light, required=False)
    
    regular = fields.Nested(Regular, required=False)
    


class Medium(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class SemiBold(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Bold(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Light(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Regular(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Blocks(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    


class GlobalSchemaProps(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    


class BlocksProps(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


