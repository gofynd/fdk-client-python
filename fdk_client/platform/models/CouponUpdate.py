"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponDateMeta import CouponDateMeta

from .CouponAuthor import CouponAuthor

from .Validity import Validity

from .Ownership import Ownership



from .CouponAction import CouponAction

from .CouponSchedule import CouponSchedule



from .Rule import Rule



from .Validation import Validation

from .Restrictions import Restrictions

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta

from .RuleDefinition import RuleDefinition

from .State import State


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    

