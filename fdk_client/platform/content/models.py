"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema



from .enums import *



class ApplicationLegal(BaseSchema):
    pass


class ApplicationLegalFAQ(BaseSchema):
    pass


class PathMappingSchema(BaseSchema):
    pass


class SeoComponent(BaseSchema):
    pass


class SeoSchema(BaseSchema):
    pass


class CustomMetaTag(BaseSchema):
    pass


class Detail(BaseSchema):
    pass


class AnnouncementPageSchema(BaseSchema):
    pass


class EditorMeta(BaseSchema):
    pass


class AnnouncementAuthorSchema(BaseSchema):
    pass


class AdminAnnouncementSchema(BaseSchema):
    pass


class ScheduleSchema(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class AnnouncementSchema(BaseSchema):
    pass


class ScheduleStartSchema(BaseSchema):
    pass


class BlogGetResponse(BaseSchema):
    pass


class ResourceContent(BaseSchema):
    pass


class Asset(BaseSchema):
    pass


class Author(BaseSchema):
    pass


class BlogSchema(BaseSchema):
    pass


class SEO(BaseSchema):
    pass


class SEOImage(BaseSchema):
    pass


class DateMeta(BaseSchema):
    pass


class BlogRequest(BaseSchema):
    pass


class GetAnnouncementListSchema(BaseSchema):
    pass


class CreateAnnouncementSchema(BaseSchema):
    pass


class DataLoaderResponseSchema(BaseSchema):
    pass


class DataLoaderResetResponseSchema(BaseSchema):
    pass


class Navigation(BaseSchema):
    pass


class LocaleLanguage(BaseSchema):
    pass


class Language(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass


class NavigationReference(BaseSchema):
    pass


class SubNavigationReference(BaseSchema):
    pass


class LandingPage(BaseSchema):
    pass


class ConfigurationSchema(BaseSchema):
    pass


class SlideshowMedia(BaseSchema):
    pass


class Slideshow(BaseSchema):
    pass


class AnnouncementsResponseSchema(BaseSchema):
    pass


class FaqResponseSchema(BaseSchema):
    pass


class UpdateHandpickedSchema(BaseSchema):
    pass


class HandpickedTagSchema(BaseSchema):
    pass


class RemoveHandpickedSchema(BaseSchema):
    pass


class CreateTagSchema(BaseSchema):
    pass


class CreateTagRequestSchema(BaseSchema):
    pass


class DataLoaderSchema(BaseSchema):
    pass


class DataLoaderSourceSchema(BaseSchema):
    pass


class DataLoadersSchema(BaseSchema):
    pass


class TagDeleteSuccessResponse(BaseSchema):
    pass


class ContentAPIError(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class CategorySchema(BaseSchema):
    pass


class ChildrenSchema(BaseSchema):
    pass


class CategoryRequestSchema(BaseSchema):
    pass


class FAQCategorySchema(BaseSchema):
    pass


class FaqSchema(BaseSchema):
    pass


class FAQ(BaseSchema):
    pass


class CreateFaqResponseSchema(BaseSchema):
    pass


class CreateFaqSchema(BaseSchema):
    pass


class GetFaqSchema(BaseSchema):
    pass


class UpdateFaqCategoryRequestSchema(BaseSchema):
    pass


class CreateFaqCategoryRequestSchema(BaseSchema):
    pass


class CreateFaqCategorySchema(BaseSchema):
    pass


class GetFaqCategoriesSchema(BaseSchema):
    pass


class GetFaqCategoryBySlugSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class LandingPageGetResponse(BaseSchema):
    pass


class LandingPageSchema(BaseSchema):
    pass


class DefaultNavigationResponse(BaseSchema):
    pass


class NavigationGetResponse(BaseSchema):
    pass


class Orientation(BaseSchema):
    pass


class NavigationSchema(BaseSchema):
    pass


class NavigationRequest(BaseSchema):
    pass


class CustomPageSchema(BaseSchema):
    pass


class ContentSchema(BaseSchema):
    pass


class CustomPage(BaseSchema):
    pass


class FeatureImage(BaseSchema):
    pass


class PageGetResponse(BaseSchema):
    pass


class PageSpec(BaseSchema):
    pass


class PageSpecParam(BaseSchema):
    pass


class PageSpecItem(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class CreatedBySchema(BaseSchema):
    pass


class PageContent(BaseSchema):
    pass


class PageMeta(BaseSchema):
    pass


class PageRequest(BaseSchema):
    pass


class CronSchedule(BaseSchema):
    pass


class PagePublishRequest(BaseSchema):
    pass


class PageMetaSchema(BaseSchema):
    pass


class SlideshowGetResponse(BaseSchema):
    pass


class SlideshowSchema(BaseSchema):
    pass


class SlideshowRequest(BaseSchema):
    pass


class Support(BaseSchema):
    pass


class PhoneProperties(BaseSchema):
    pass


class PhoneSchema(BaseSchema):
    pass


class EmailProperties(BaseSchema):
    pass


class EmailSchema(BaseSchema):
    pass


class ContactSchema(BaseSchema):
    pass


class TagsSchema(BaseSchema):
    pass


class TagSchema(BaseSchema):
    pass


class TagSourceSchema(BaseSchema):
    pass





class ApplicationLegal(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    tnc = fields.Str(required=False)
    
    policy = fields.Str(required=False)
    
    shipping = fields.Str(required=False)
    
    returns = fields.Str(required=False)
    
    faq = fields.List(fields.Nested(ApplicationLegalFAQ, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class ApplicationLegalFAQ(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    


class PathMappingSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    


class SeoComponent(BaseSchema):
    # Content swagger.json

    
    seo = fields.Nested(SeoSchema, required=False)
    


class SeoSchema(BaseSchema):
    # Content swagger.json

    
    app = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    robots_txt = fields.Str(required=False)
    
    sitemap_enabled = fields.Boolean(required=False)
    
    custom_meta_tags = fields.List(fields.Dict(required=False), required=False)
    
    details = fields.Nested(Detail, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomMetaTag(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class Detail(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class AnnouncementPageSchema(BaseSchema):
    # Content swagger.json

    
    page_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EditorMeta(BaseSchema):
    # Content swagger.json

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    


class AnnouncementAuthorSchema(BaseSchema):
    # Content swagger.json

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class AdminAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    announcement = fields.Str(required=False)
    
    pages = fields.List(fields.Nested(AnnouncementPageSchema, required=False), required=False)
    
    editor_meta = fields.Nested(EditorMeta, required=False)
    
    author = fields.Nested(AnnouncementAuthorSchema, required=False)
    
    created_at = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    


class ScheduleSchema(BaseSchema):
    # Content swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Float(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    


class NextSchedule(BaseSchema):
    # Content swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class AnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    announcement = fields.Str(required=False)
    
    schedule = fields.Nested(ScheduleStartSchema, required=False)
    


class ScheduleStartSchema(BaseSchema):
    # Content swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class BlogGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ResourceContent(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class Asset(BaseSchema):
    # Content swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class Author(BaseSchema):
    # Content swagger.json

    
    designation = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class BlogSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    title = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    


class SEO(BaseSchema):
    # Content swagger.json

    
    description = fields.Str(required=False)
    
    image = fields.Nested(SEOImage, required=False)
    
    title = fields.Str(required=False)
    


class SEOImage(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    


class DateMeta(BaseSchema):
    # Content swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class BlogRequest(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    


class GetAnnouncementListSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(AdminAnnouncementSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(AdminAnnouncementSchema, required=False)
    


class DataLoaderResponseSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    __source = fields.Nested(DataLoaderSourceSchema, required=False)
    


class DataLoaderResetResponseSchema(BaseSchema):
    # Content swagger.json

    
    reset = fields.Str(required=False)
    


class Navigation(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    orientation = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    navigation = fields.Nested(NavigationReference, required=False)
    


class LocaleLanguage(BaseSchema):
    # Content swagger.json

    
    hi = fields.Nested(Language, required=False)
    
    ar = fields.Nested(Language, required=False)
    
    en_us = fields.Nested(Language, required=False)
    


class Language(BaseSchema):
    # Content swagger.json

    
    display = fields.Str(required=False)
    


class Action(BaseSchema):
    # Content swagger.json

    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    


class ActionPage(BaseSchema):
    # Content swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Nested(PageType, required=False)
    


class NavigationReference(BaseSchema):
    # Content swagger.json

    
    acl = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Nested(LocaleLanguage, required=False)
    
    image = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    active = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    sort_order = fields.Int(required=False)
    
    sub_navigation = fields.List(fields.Nested(SubNavigationReference, required=False), required=False)
    


class SubNavigationReference(BaseSchema):
    # Content swagger.json

    
    acl = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Nested(LocaleLanguage, required=False)
    
    image = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    active = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    sort_order = fields.Int(required=False)
    
    sub_navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    


class LandingPage(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(LandingPageSchema, required=False)
    
    success = fields.Boolean(required=False)
    


class ConfigurationSchema(BaseSchema):
    # Content swagger.json

    
    sleep_time = fields.Int(required=False)
    
    start_on_launch = fields.Boolean(required=False)
    
    duration = fields.Int(required=False)
    
    slide_direction = fields.Str(required=False)
    


class SlideshowMedia(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    auto_decide_duration = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    


class Slideshow(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(SlideshowSchema, required=False)
    
    success = fields.Boolean(required=False)
    


class AnnouncementsResponseSchema(BaseSchema):
    # Content swagger.json

    
    announcements = fields.Dict(required=False)
    
    refresh_rate = fields.Int(required=False)
    
    refresh_pages = fields.List(fields.Str(required=False), required=False)
    


class FaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    


class UpdateHandpickedSchema(BaseSchema):
    # Content swagger.json

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    


class HandpickedTagSchema(BaseSchema):
    # Content swagger.json

    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    


class RemoveHandpickedSchema(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    


class CreateTagSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    content = fields.Str(required=False)
    


class CreateTagRequestSchema(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    


class DataLoaderSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    __source = fields.Nested(DataLoaderSourceSchema, required=False)
    
    _id = fields.Str(required=False)
    


class DataLoaderSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class DataLoadersSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(DataLoaderSchema, required=False), required=False)
    


class TagDeleteSuccessResponse(BaseSchema):
    # Content swagger.json

    
    success = fields.Boolean(required=False)
    


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
    


class CommonError(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    


class CategorySchema(BaseSchema):
    # Content swagger.json

    
    index = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    children = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    icon_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class ChildrenSchema(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class CategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class FAQCategorySchema(BaseSchema):
    # Content swagger.json

    
    index = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    children = fields.List(fields.Nested(ChildrenSchema, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    icon_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class FaqSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class FAQ(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    


class CreateFaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FaqSchema, required=False)
    


class CreateFaqSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    


class GetFaqSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    


class UpdateFaqCategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    


class CreateFaqCategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    


class CreateFaqCategorySchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    


class GetFaqCategoriesSchema(BaseSchema):
    # Content swagger.json

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    


class GetFaqCategoryBySlugSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(FAQCategorySchema, required=False)
    


class Page(BaseSchema):
    # Content swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class LandingPageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(LandingPageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class LandingPageSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class DefaultNavigationResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    


class NavigationGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Orientation(BaseSchema):
    # Content swagger.json

    
    portrait = fields.List(fields.Str(required=False), required=False)
    
    landscape = fields.List(fields.Str(required=False), required=False)
    


class NavigationSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    version = fields.Float(required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    


class NavigationRequest(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    


class CustomPageSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    orientation = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    


class ContentSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class CustomPage(BaseSchema):
    # Content swagger.json

    
    data = fields.Nested(CustomPageSchema, required=False)
    


class FeatureImage(BaseSchema):
    # Content swagger.json

    
    secure_url = fields.Str(required=False)
    


class PageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PageSpec(BaseSchema):
    # Content swagger.json

    
    specifications = fields.List(fields.Dict(required=False), required=False)
    


class PageSpecParam(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    


class PageSpecItem(BaseSchema):
    # Content swagger.json

    
    page_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    params = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    
    query = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    


class PageSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    component_ids = fields.List(fields.Str(required=False), required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    content_path = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    page_meta = fields.List(fields.Dict(required=False), required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    visibility = fields.Dict(required=False)
    
    archived = fields.Boolean(required=False)
    


class CreatedBySchema(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    


class PageContent(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class PageMeta(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class PageRequest(BaseSchema):
    # Content swagger.json

    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    application = fields.Str(required=False)
    
    author = fields.Nested(Author, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    title = fields.Str(required=False)
    


class CronSchedule(BaseSchema):
    # Content swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Float(required=False)
    


class PagePublishRequest(BaseSchema):
    # Content swagger.json

    
    publish = fields.Boolean(required=False)
    


class PageMetaSchema(BaseSchema):
    # Content swagger.json

    
    system_pages = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    custom_pages = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    application_id = fields.Str(required=False)
    


class SlideshowGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(SlideshowSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SlideshowSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    application = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.List(fields.Nested(SlideshowMedia, required=False), required=False)
    
    active = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class SlideshowRequest(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.Nested(SlideshowMedia, required=False)
    
    active = fields.Boolean(required=False)
    


class Support(BaseSchema):
    # Content swagger.json

    
    created = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    contact = fields.Nested(ContactSchema, required=False)
    


class PhoneProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    


class PhoneSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    phone = fields.List(fields.Nested(PhoneProperties, required=False), required=False)
    


class EmailProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class EmailSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    email = fields.List(fields.Nested(EmailProperties, required=False), required=False)
    


class ContactSchema(BaseSchema):
    # Content swagger.json

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    


class TagsSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagSchema, required=False), required=False)
    


class TagSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    content = fields.Str(required=False)
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    


class TagSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


