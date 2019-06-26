from .semanticbase import create as create_semantic_base

from .annotations import get_uniprot_annotations

from .ssm import (
    semantic_base,
    ssm_multiple,
    get_id,
    ssm_resnik,
    ssm_lin,
    ssm_jiang_conrath,
)

name = "ssmpy"
__all__ = [
    "create_semantic_base",
    "get_uniprot_annotations",
    "intrinsic",
    "mica",
    "get_id",
    "ssm_resnik",
    "ssm_lin",
    "ssm_jiang_conrath",
]
