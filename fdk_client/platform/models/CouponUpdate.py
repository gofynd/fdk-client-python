"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership import Ownership



from .CouponAuthor import CouponAuthor

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .Rule import Rule



from .Restrictions import Restrictions

from .Identifier import Identifier

from .RuleDefinition import RuleDefinition

from .Validation import Validation

from .CouponAction import CouponAction



from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta

from .State import State


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    state = fields.Nested(State, required=False)
    

