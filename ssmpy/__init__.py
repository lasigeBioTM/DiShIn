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
    information_content,
    information_content_intrinsic,
    information_content_extrinsic,
    get_ancestors,
    num_paths,
    shared_ic_dca,
    shared_ic_mica,
    shared_ic,
)

name = "ssmpy"
__all__ = [
    "semantic_base",
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
    "information_content",
    "information_content_intrinsic",
    "information_content_extrinsic",
    "get_ancestors",
    "num_paths",
    "shared_ic_dca",
    "shared_ic_mica",
    "shared_ic",
]
