"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rule import Rule



from .DisplayMeta import DisplayMeta

from .RuleDefinition import RuleDefinition

from .CouponSchedule import CouponSchedule

from .Validity import Validity

from .Restrictions import Restrictions



from .Validation import Validation



from .CouponAction import CouponAction

from .State import State

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .Ownership import Ownership


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    

