"""MetaAgent routing sanity checks."""
import pytest

from meta_agent import MetaAgent

CASES = [
    ("answer questions from our help-center knowledge base", 4),
    ("extract the total and invoice date from this PDF invoice", 5),
    ("fact-check this statistical claim against trusted sources", 11),
    ("write a function and make the unit tests pass", 13),
    ("recommend books for a science-fiction fan", 18),
]


@pytest.fixture(scope="module")
def meta():
    return MetaAgent()


def test_router_loads_catalog(meta):
    assert len(meta._index) == 31


@pytest.mark.parametrize("task,expected_num", CASES)
def test_routing_picks_expected_agent(meta, task, expected_num):
    ranked = meta.rank(task)
    top = ranked[0].spec
    assert top.num == expected_num, (
        f"task {task!r} routed to #{top.num} {top.name}, expected #{expected_num}"
    )


@pytest.mark.parametrize("num", list(range(1, 32)))
def test_every_agent_class_loads(num):
    cls = MetaAgent.load(num)
    assert isinstance(cls, type)
