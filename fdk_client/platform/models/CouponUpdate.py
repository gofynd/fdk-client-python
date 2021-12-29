"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule



from .Identifier import Identifier

from .Rule import Rule

from .Validation import Validation



from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions



from .Ownership import Ownership

from .State import State

from .RuleDefinition import RuleDefinition

from .CouponAction import CouponAction


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    

