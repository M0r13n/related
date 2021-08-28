import related


@related.immutable
class Child(object):
    name = related.StringField()
    values_list = related.SequenceField(str, key="values", convert_scalar=False)
    values_list_scalar = related.SequenceField(str, key="values", convert_scalar=True)
    values_set = related.SetField(str, key="values", convert_scalar=False)
    values_set_scalar = related.SetField(str, key="values", convert_scalar=True)


def test_single_value():
    value = {
        "name": "FooBar 2000",
        "values": "187"
    }
    child = related.to_model(Child, value)

    assert child.name == "FooBar 2000"
    assert child.values_list == ['1', '8', '7']
    assert child.values_list_scalar == ["187", ]

    assert child.values_set == {'1', '8', '7'}
    assert child.values_set_scalar == {"187", }


def test_multiple_values():
    value = {
        "name": "FooBar 2000",
        "values": ["42", "1337", "69"]
    }
    child = related.to_model(Child, value)

    assert child.name == "FooBar 2000"
    assert child.values_list == ["42", "1337", "69"]
    assert child.values_list_scalar == ["42", "1337", "69"]

    assert child.values_set == {"42", "1337", "69"}
    assert child.values_set_scalar == {"42", "1337", "69"}
