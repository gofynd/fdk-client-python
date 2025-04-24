"""Catalog Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class TaxonomyItemAttributeSchemaObject(BaseSchema):
    pass


class TaxonomyItemAttributesResponseSchema(BaseSchema):
    pass


class TaxonomyItemResponseSchema(BaseSchema):
    pass


class TaxonomyResponseSchema(BaseSchema):
    pass


class ValidationErrors(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass





class TaxonomyItemAttributeSchemaObject(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    mandatory = fields.Boolean(required=False)
    


class TaxonomyItemAttributesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    schema = fields.Nested(TaxonomyItemAttributeSchemaObject, required=False)
    


class TaxonomyItemResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    attributes = fields.List(fields.Nested(TaxonomyItemAttributesResponseSchema, required=False), required=False)
    
    product_template_slug = fields.Str(required=False)
    
    product_template_name = fields.Str(required=False)
    


class TaxonomyResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(TaxonomyItemResponseSchema, required=False), required=False)
    


class ValidationErrors(BaseSchema):
    # Catalog swagger.json

    
    errors = fields.List(fields.Nested(ValidationError, required=False), required=False)
    


class ValidationError(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


