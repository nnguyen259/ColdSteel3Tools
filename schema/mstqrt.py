MasterQuartzStatus = {
    "pattern_id" : "b",
    "level" : "s",
    "hp" : "s",
    "ep" : "s",
    "str" : "s",
    "def" : "s",
    "ats" : "s",
    "adf" : "s",
    "spd" : "s",
    "sub_hp" : "s",
    "sub_ep" : "s",
    "sub_str" : "s",
    "sub_def" : "s",
    "sub_ats" : "s",
    "sub_adf" : "s",
    "sub_spd" : "s"
}

MasterQuartzBase = {
    "item_id" : "s",
    "id" : "s",
    "unknown" : "s",
    "hp_pattern" : "s",
    "ep_pattern" : "s",
    "str_pattern" : "s",
    "def_pattern" : "s",
    "ats_pattern" : "s",
    "adf_pattern" : "s",
    "spd_pattern" : "s",
    "mq_data" : "MasterQuartzData",
    "mq_memo" : "MasterQuartzMemo"
}

MasterQuartzData = {
    "size" : 7,
    "uid" : "#0",
    "item_id" : "s",
    "mq_level" : "s",
    "effect_1" : "f",
    "effect_2" : "f",
    "effect_3" : "f",
    "effect_4" : "f",
    "effect_5" : "f",
    "effect_6" : "f",
    "effect_7" : "f",
    "effect_8" : "f",
    "effect_9" : "f",
    "art_1_id" : "s",
    "art_2_id" : "s",
    "memo_1_id" : "s",
    "memo_2_id" : "s",
    "memo_3_id" : "s",
    "memo_4_id" : "s",
    "memo_5_id" : "s",
    "memo_6_id" : "s",
    "memo_7_id" : "s",
    "memo_8_id" : "s",
    "memo_9_id" : "s"
}

MasterQuartzMemo = {
    "size" : "?",
    "uid" : "#0",
    "item_id" : "s",
    "memo_id" : "s",
    "memo" : "t"
}

MasterQuartzDummy = {
    "dummy_id" : "s",
    "original_id" : "s"
}

headers = ["MasterQuartzStatus", "MasterQuartzBase", "MasterQuartzDummy"]