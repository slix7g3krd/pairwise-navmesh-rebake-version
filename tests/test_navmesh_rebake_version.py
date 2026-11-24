import pytest
import gameplay.navmesh_rebake_version as mod

CASES = [
    ("queue_during_rebake", (1,)),
    ("version_tag", (1,)),
    ("validate_generation", (1,)),
    ("bake_avoidance", (1,)),
    ("stable_bake_input", (1,)),
    ("incremental_swap", (1,)),
    ("notify_destroy", (1,)),
    ("rebuild", (1,)),
    ("path", (1,)),
    ("apply_result", (1,)),
    ("validate_navmesh", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
