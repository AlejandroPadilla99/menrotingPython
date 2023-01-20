#lib
from assertpy import soft_assertions, assert_that

def assert_validate_dic(dic_response: dict, dic_correct : dict) -> None:
    failures = list()
    with soft_assertions():
        for key, value in dic_correct.items():
            assert_that(dic_response[key]).is_equal_to(value)
