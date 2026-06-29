"""Catalog integrity + book-reference link validation."""
from pathlib import Path

import pytest

import catalog

ROOT = Path(__file__).resolve().parent.parent
NUMS = list(range(1, 32))


def test_catalog_has_31_unique_agents():
    nums = [s.num for s in catalog.CATALOG]
    assert sorted(nums) == NUMS
    assert len({s.cls for s in catalog.CATALOG}) == 31
    assert len({s.file for s in catalog.CATALOG}) == 31


@pytest.mark.parametrize("num", NUMS)
def test_agent_module_file_exists(num):
    spec = catalog.by_number(num)
    assert (ROOT / spec.file).is_file()


@pytest.mark.parametrize("num", NUMS)
def test_enrichment_present(num):
    assert catalog.TECHNIQUES.get(num), f"missing TECHNIQUES for agent {num}"
    assert catalog.USE_CASES.get(num), f"missing USE_CASES for agent {num}"


@pytest.mark.parametrize("num", NUMS)
def test_book_reference_paths_exist(num):
    ref = catalog.reference(num, prefix="book-repo")
    for key in ("readme", "usecase", "agents_md", "notebook"):
        assert (ROOT / ref[key]).is_file(), f"agent {num}: missing {key} -> {ref[key]}"
