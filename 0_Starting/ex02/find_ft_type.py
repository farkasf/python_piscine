def all_thing_is_obj(object: any) -> int:

    type_dict = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }
    o_type = type(object)

    if o_type in type_dict:
        print(f"{type_dict[o_type]} : {o_type}")
    elif o_type is str:
        print(f"{object} is in the kitchen : {o_type}")
    else:
        print("Type not found")

    return 42
