def NULL_not_found(object: any) -> int:
    null_dict = {
        None: "Nothing",
        int(0): "Zero",
        '': "Empty",
    }

    o_type = type(object)

    if o_type is float and object != object:
        print(f"Cheese: {object} {o_type}")
    elif o_type is bool:
        print(f"Fake: {object} {o_type}")
    elif object in null_dict:
        print(f"{null_dict[object]}: {object} {o_type}")
    else:
        print("Type not found")
        return 1

    return 0
