from solution import ListUtil


def test_check_create_class():
    solution = ListUtil()
    assert solution is not None


def test_method_getlist():
    solution = ListUtil()
    numberList = solution.getList()
    assert len(numberList) == 0


def test_getList_after_addnumbers():
    solution = ListUtil()
    result = solution.addNumbers(10)
    numberList = solution.getList()
    assert len(numberList) > 0


def test_return_method_addnumbers():
    solution = ListUtil()
    result = solution.addNumbers(10)
    assert result == 45
