from .set_wizard_config import user_config
from datetime import datetime

style_wrapper = {
    "reset": "\x1b[0m",
    # This lightens the color as a side-effect
    "bold": "\x1b[1m",
    "dim": "\x1b[2m",
    "italic": "\x1b[3m",
    "underscore": "\x1b[4m",
    "blink": "\x1b[5m",
    "reverse": "\x1b[7m",
    "hidden": "\x1b[8m",
    "strike": "\x1b[9m",
    "fg_lack": "\x1b[30m",
    "fg_red": "\x1b[31m",
    "fg_green": "\x1b[32m",
    "fg_yellow": "\x1b[33m",
    "fg_blue": "\x1b[34m",
    "fg_magenta": "\x1b[35m",
    "fg_cyan": "\x1b[36m",
    "fg_white": "\x1b[37m",
    "fg_gray": "\x1b[90m",
    "bg_black": "\x1b[40m",
    "bg_red": "\x1b[41m",
    "bg_green": "\x1b[42m",
    "bg_yellow": "\x1b[43m",
    "bg_blue": "\x1b[44m",
    "bg_magenta": "\x1b[45m",
    "bg_cyan": "\x1b[46m",
    "bg_white": "\x1b[47m",
    "bg_gray": "\x1b[100m",
}


class Helpers:
    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    @staticmethod
    def get_config(override=None):
        if override:
            return {**user_config, **override}
        else:
            return user_config

    @staticmethod
    def get_logging_args(config: dict, options: dict):
        status_text = {
            "error": "ERROR ",
            "warn": "WARN ",
            "info": "INFO ",
            "success": "SUCCESS ",
        }
        status_color = {
            "bg": {
                "error": "bg_red",
                "info": "bg_blue",
                "success": "bg_green",
                "warn": "bg_yellow",
            },
            "fg": {
                "error": "fg_red",
                "info": "fg_blue",
                "success": "fg_green",
                "warn": "fg_yellow",
            },
        }

        args = []
        status_type = options["status_type"]
        status_msg = status_text[status_type]
        fg_color = status_color["fg"][status_type]
        bg_color = status_color["bg"][status_type]

        if config["include_timestamp"]:
            args.append(style_wrapper["fg_gray"])
            args.append(options["timestamp"])
            args.append(style_wrapper["reset"])

        if config["include_status"]:
            args.append(style_wrapper[bg_color])
            args.append(style_wrapper["bold"])
            args.append(status_msg)
            args.append(style_wrapper["reset"])

        args.append(style_wrapper[fg_color])
        args.append(options["msg"])
        args.append(style_wrapper["reset"])

        return args


timestamp = f"[{Helpers.get_timestamp()}]"


class Logger:
    @staticmethod
    def success(msg: str, config_override=None) -> str:
        status_type = "success"
        config = Helpers.get_config(config_override)
        args_list = Helpers.get_logging_args(
            config,
            {
                "status_type": status_type,
                "msg": msg,
                "timestamp": timestamp,
            },
        )

        print("\n")
        print(" ".join(args_list))

    @staticmethod
    def info(msg: str, config_override=None) -> str:
        status_type = "info"
        config = Helpers.get_config(config_override)
        args_list = Helpers.get_logging_args(
            config,
            {
                "status_type": status_type,
                "msg": msg,
                "timestamp": timestamp,
            },
        )
        print("\n")
        print(" ".join(args_list))

    @staticmethod
    def error(msg: str, config_override=None) -> str:
        status_type = "error"
        config = Helpers.get_config(config_override)
        args_list = Helpers.get_logging_args(
            config,
            {
                "status_type": status_type,
                "msg": msg,
                "timestamp": timestamp,
            },
        )

        print("\n")
        print(" ".join(args_list))

    @staticmethod
    def warn(msg: str, config_override=None) -> str:
        status_type = "warn"
        config = Helpers.get_config(config_override)
        args_list = Helpers.get_logging_args(
            config,
            {
                "status_type": status_type,
                "msg": msg,
                "timestamp": timestamp,
            },
        )
        print("\n")
        print(" ".join(args_list))
