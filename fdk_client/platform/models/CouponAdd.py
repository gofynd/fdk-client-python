"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .CouponAction import CouponAction

from .Ownership import Ownership



from .State import State



from .Rule import Rule

from .Identifier import Identifier

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Validation import Validation



from .CouponSchedule import CouponSchedule

from .RuleDefinition import RuleDefinition


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    code = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    

