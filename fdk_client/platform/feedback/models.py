"""Feedback Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class Activity(BaseSchema):
    pass


class ActivityDump(BaseSchema):
    pass


class AddMediaListRequest(BaseSchema):
    pass


class AddMediaRequest(BaseSchema):
    pass


class ApproveRequest(BaseSchema):
    pass


class Attribute(BaseSchema):
    pass


class AttributeObject(BaseSchema):
    pass


class CreatedBy(BaseSchema):
    pass


class CursorGetResponse(BaseSchema):
    pass


class DateMeta(BaseSchema):
    pass


class DeviceMeta(BaseSchema):
    pass


class Entity(BaseSchema):
    pass


class EntityRequest(BaseSchema):
    pass


class FeedbackAttributes(BaseSchema):
    pass


class FeedbackError(BaseSchema):
    pass


class FeedbackState(BaseSchema):
    pass


class GetResponse(BaseSchema):
    pass


class GetReviewResponse(BaseSchema):
    pass


class InsertResponse(BaseSchema):
    pass


class MediaMeta(BaseSchema):
    pass


class MediaMetaRequest(BaseSchema):
    pass


class NumberGetResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class PageCursor(BaseSchema):
    pass


class PageNumber(BaseSchema):
    pass


class Rating(BaseSchema):
    pass


class RatingRequest(BaseSchema):
    pass


class ReportAbuseRequest(BaseSchema):
    pass


class Review(BaseSchema):
    pass


class ReviewFacet(BaseSchema):
    pass


class ReviewRequest(BaseSchema):
    pass


class SaveAttributeRequest(BaseSchema):
    pass


class SortMethod(BaseSchema):
    pass


class TagMeta(BaseSchema):
    pass


class Template(BaseSchema):
    pass


class TemplateGetResponse(BaseSchema):
    pass


class TemplateRequest(BaseSchema):
    pass


class TemplateRequestList(BaseSchema):
    pass


class UI(BaseSchema):
    pass


class UIIcon(BaseSchema):
    pass


class UpdateAttributeRequest(BaseSchema):
    pass


class UpdateResponse(BaseSchema):
    pass


class UpdateReviewRequest(BaseSchema):
    pass


class UpdateTemplateRequest(BaseSchema):
    pass


class UpdateTemplateStatusRequest(BaseSchema):
    pass





class Activity(BaseSchema):
    # Feedback swagger.json

    
    current_state = fields.Dict(required=False)
    
    document_id = fields.Str(required=False)
    
    previous_state = fields.Dict(required=False)
    


class ActivityDump(BaseSchema):
    # Feedback swagger.json

    
    activity = fields.Nested(Activity, required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class AddMediaListRequest(BaseSchema):
    # Feedback swagger.json

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_list = fields.List(fields.Nested(AddMediaRequest, required=False), required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    


class AddMediaRequest(BaseSchema):
    # Feedback swagger.json

    
    cloud_id = fields.Str(required=False)
    
    cloud_name = fields.Str(required=False)
    
    cloud_provider = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_url = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    thumbnail_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApproveRequest(BaseSchema):
    # Feedback swagger.json

    
    approve = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    


class Attribute(BaseSchema):
    # Feedback swagger.json

    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    


class AttributeObject(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class CreatedBy(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    


class CursorGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class DateMeta(BaseSchema):
    # Feedback swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class DeviceMeta(BaseSchema):
    # Feedback swagger.json

    
    app_version = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    


class Entity(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EntityRequest(BaseSchema):
    # Feedback swagger.json

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    


class FeedbackAttributes(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class FeedbackError(BaseSchema):
    # Feedback swagger.json

    
    code = fields.Dict(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class FeedbackState(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    media = fields.Str(required=False)
    
    qna = fields.Boolean(required=False)
    
    rating = fields.Boolean(required=False)
    
    review = fields.Boolean(required=False)
    


class GetResponse(BaseSchema):
    # Feedback swagger.json

    
    data = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetReviewResponse(BaseSchema):
    # Feedback swagger.json

    
    facets = fields.List(fields.Nested(ReviewFacet, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort = fields.List(fields.Nested(SortMethod, required=False), required=False)
    


class InsertResponse(BaseSchema):
    # Feedback swagger.json

    
    count = fields.Int(required=False)
    


class MediaMeta(BaseSchema):
    # Feedback swagger.json

    
    max_count = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class MediaMetaRequest(BaseSchema):
    # Feedback swagger.json

    
    max_count = fields.Int(required=False)
    
    size = fields.Int(required=False)
    


class NumberGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Feedback swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class PageCursor(BaseSchema):
    # Feedback swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class PageNumber(BaseSchema):
    # Feedback swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class Rating(BaseSchema):
    # Feedback swagger.json

    
    attributes = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    attributes_slugs = fields.List(fields.Str(required=False), required=False)
    
    ui = fields.Nested(UI, required=False)
    


class RatingRequest(BaseSchema):
    # Feedback swagger.json

    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    ui = fields.Nested(UI, required=False)
    


class ReportAbuseRequest(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    


class Review(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(MediaMeta, required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(MediaMeta, required=False)
    
    vote_allowed = fields.Boolean(required=False)
    


class ReviewFacet(BaseSchema):
    # Feedback swagger.json

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ReviewRequest(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(MediaMetaRequest, required=False)
    
    is_vote_allowed = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(MediaMetaRequest, required=False)
    


class SaveAttributeRequest(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class SortMethod(BaseSchema):
    # Feedback swagger.json

    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class TagMeta(BaseSchema):
    # Feedback swagger.json

    
    media = fields.List(fields.Nested(MediaMeta, required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Template(BaseSchema):
    # Feedback swagger.json

    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Nested(Rating, required=False)
    
    review = fields.Nested(Review, required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    


class TemplateGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Template, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class TemplateRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    enable_media_type = fields.Str(required=False)
    
    enable_qna = fields.Boolean(required=False)
    
    enable_rating = fields.Boolean(required=False)
    
    enable_review = fields.Boolean(required=False)
    
    entity = fields.Nested(EntityRequest, required=False)
    
    rating = fields.Nested(RatingRequest, required=False)
    
    review = fields.Nested(ReviewRequest, required=False)
    


class TemplateRequestList(BaseSchema):
    # Feedback swagger.json

    
    template_list = fields.List(fields.Nested(TemplateRequest, required=False), required=False)
    


class UI(BaseSchema):
    # Feedback swagger.json

    
    feedback_question = fields.List(fields.Str(required=False), required=False)
    
    icon = fields.Nested(UIIcon, required=False)
    
    text = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class UIIcon(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Str(required=False)
    
    inactive = fields.Str(required=False)
    
    selected = fields.List(fields.Str(required=False), required=False)
    


class UpdateAttributeRequest(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class UpdateResponse(BaseSchema):
    # Feedback swagger.json

    
    count = fields.Int(required=False)
    


class UpdateReviewRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    application = fields.Str(required=False)
    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    attributes_rating = fields.List(fields.Nested(AttributeObject, required=False), required=False)
    
    description = fields.Str(required=False)
    
    device_meta = fields.Nested(DeviceMeta, required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_resource = fields.List(fields.Nested(MediaMeta, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    review_id = fields.Str(required=False)
    
    template_id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class UpdateTemplateRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    enable_media_type = fields.Str(required=False)
    
    enable_qna = fields.Boolean(required=False)
    
    enable_rating = fields.Boolean(required=False)
    
    enable_review = fields.Boolean(required=False)
    
    entity = fields.Nested(EntityRequest, required=False)
    
    rating = fields.Nested(RatingRequest, required=False)
    
    review = fields.Nested(ReviewRequest, required=False)
    


class UpdateTemplateStatusRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    


