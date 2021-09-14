item = {
    "id" : "s",
    "character_restriction" : "s",
    "flags" : "t",
    "type" : "s",
    "subtype" : "s",

    "element": "b",

    "slash": "b",
    "thrust": "b",
    "pierce": "b",
    "strike": "b",
    "byte_1": "b", # some weapon attribute
    "target_type": "b",
    "range": "f",
    "area": "b",

    "float_1": "f",
    "float_2": "f",
    "float_3": "f",

    "effect1_id" : "s",
    "effect1_data1" : "i",
    "effect1_data2" : "i",
    "effect1_data3" : "i",
    "effect2_id" : "s",
    "effect2_data1" : "i",
    "effect2_data2" : "i",
    "effect2_data3" : "i",
    "effect3_id" : "s",
    "effect3_data1" : "i",
    "effect3_data2" : "i",
    "effect3_data3" : "i",
    "effect4_id" : "s",
    "effect4_data1" : "i",
    "effect4_data2" : "i",
    "effect4_data3" : "i",
    "effect5_id" : "s",
    "effect5_data1" : "i",
    "effect5_data2" : "i",
    "effect5_data3" : "i",

    "str": "S",
    "def": "S",
    "ats": "S",
    "adf": "S",
    "acc": "S",
    "eva": "S",
    "spd": "S",
    "mov": "S",
    "hp": "S",
    "ep": "S",

    "price": "i",
    "carry_limit": "b",
    "sort_id": "s",
    "short_1": "s",
    "name": "t",
    "description": "t",
    "zeros": "d"
}

item_q = {
    "id" : "s",
    "short_1" : "s", # not character restriction. unused?
    "flags" : "t",
    "type" : "s",
    "subtype" : "s",
    "element": "b",

    "zeros_1": "d5",

    "quartz_type": "b", # normal/status/breaker
    "rating": "f",
    "byte_1": "b",

    "zeros_2": "d12",

    "effect1_id" : "s",
    "effect1_data1" : "i",
    "effect1_data2" : "i",
    "effect1_data3" : "i",
    "effect2_id" : "s",
    "effect2_data1" : "i",
    "effect2_data2" : "i",
    "effect2_data3" : "i",
    "effect3_id" : "s",
    "effect3_data1" : "i",
    "effect3_data2" : "i",
    "effect3_data3" : "i",
    "effect4_id" : "s",
    "effect4_data1" : "i",
    "effect4_data2" : "i",
    "effect4_data3" : "i",
    "effect5_id" : "s",
    "effect5_data1" : "i",
    "effect5_data2" : "i",
    "effect5_data3" : "i",

    "str": "S",
    "def": "S",
    "ats": "S",
    "adf": "S",
    "acc": "S",
    "eva": "S",
    "spd": "S",
    "mov": "S",
    "hp": "S",
    "ep": "S",

    "price": "i", # mira obtained from selling times four. (not sepith cost)
    "carry_limit": "b",
    "sort_id": "s",
    "short_2": "s",
    "name": "t",
    "description": "t",

    # used for auto-equip
    "prio_balanced": "s",
    "prio_phys": "s",
    "prio_mag": "s",
    "prio_spd": "s",

    "art1_id": "s",
    "art2_id": "s",
    "art3_id": "s",
    "art4_id": "s",
    "art5_id": "s",
    "art6_id": "s",
}

headers = ["item", "item_q"]