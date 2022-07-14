"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DocumentObject import DocumentObject

from .DocumentObject import DocumentObject


class RestrictedCategoryMetricsResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    food = fields.Nested(DocumentObject, required=False)
    
    drug = fields.Nested(DocumentObject, required=False)
    

