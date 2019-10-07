from .semanticbase import create as create_semantic_base

from .annotations import get_uniprot_annotations

from .ssm import (
    semantic_base,
    ssm_multiple,
    intrinsic,
    mica,
    get_id,
    ssm_resnik,
    ssm_lin,
    ssm_jiang_conrath,
    run_query,
    get_name,
    common_ancestors,
    information_content_intrinsic,
    information_content_extrinsic,
    get_ancestors,
)

name = "ssmpy"
__all__ = [
    "create_semantic_base",
    "get_uniprot_annotations",
    "ssm_multiple",
    "intrinsic",
    "mica",
    "get_id",
    "ssm_resnik",
    "ssm_lin",
    "ssm_jiang_conrath",
    "run_query",
    "get_name",
    "common_ancestors",
    "information_content_intrinsic",
    "information_content_extrinsic",
    "get_ancestors",
]
