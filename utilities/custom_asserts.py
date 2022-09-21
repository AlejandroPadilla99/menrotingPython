
def assert_validate_dic(dic_response: dict, dic_correct : dict) -> None:
    failures = list()
    for key, value in dic_correct:
        if value != dic_response[key]:
            failures.append(value + ' != ' + dic_response[key])

    
    assert (failures == [], str(failures))