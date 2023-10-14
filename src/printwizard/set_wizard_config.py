__default_config = {
    "include_timestamp": True,
    "include_status": True,
    "include_sn": True,
    "table_border": {
        "corner_tl": "┌",
        "corner_tr": "┐",
        "corner_bl": "└",
        "corner_br": "┘",
        "edge_vertical": "│",
        "edge_horizontal": "─",
        "intersection_tlr": "┴",
        "intersection_blr": "┬",
        "intersection_tbl": "├",
        "intersection_tbr": "┤",
        "intersection_center": "┼",
    },
}

user_config = __default_config


def set_wizard_config(config: dict):
    global user_config
    user_config = {**user_config, **config}
