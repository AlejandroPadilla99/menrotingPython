import pytest
from dataclasses import dataclass, field


# "Selenium functions"
def finder(step_type, key, do_something=None):
    obj = dict(type=step_type, key=key)
    if do_something: do_something(obj)
    return True

def click_something(item=None):
    print("CLicked or inserted data")


# Root abstraction that populates factory.
@dataclass
class Action:
    label: str
    func: str
    params: tuple

    def exec(self):
        if len(self.params) > 2:
            res = self.func(self.params[0], self.params[1], self.params[2])
        else:
            res = self.func(self.params[0], self.params[1])
        return res


# Holds the factory
@dataclass
class Actions:
    factory: list = field(default_factory=list)

    def enroll(self, label, func, params):
        action = Action(label, func, params)
        self.factory.append(action)

# Defines Factory behavior
@dataclass
class Page:
    url: str = "url"
    flows: Actions = Actions()

# Top-level implementation
store = Page()
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere", lambda obj: click_something(obj)))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere", lambda obj: click_something(obj)))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere", lambda obj: click_something(obj)))
store.flows.enroll("username", finder, ("By.NAME", "/div/to/somewhere"))


@pytest.mark.parametrize("flow", store.flows.factory)
def test_factory(flow):
    assert flow.exec()