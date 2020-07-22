# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.python.subsystems.python_tool_base import PythonToolBase
from pants.option.custom_types import file_option, shell_str


class Isort(PythonToolBase):
    """The Python import sorter tool (https://timothycrosley.github.io/isort/)."""

    options_scope = "isort"
    default_version = "isort>=5.0.0,<6.0"
    default_extra_requirements = ["setuptools<45"]  # NB: `<45` is for Python 2 support
    default_entry_point = "isort.main"

    @classmethod
    def register_options(cls, register):
        super().register_options(register)
        register(
            "--skip",
            type=bool,
            default=False,
            help="Don't use isort when running `./pants fmt` and `./pants lint`",
        )
        register(
            "--args",
            type=list,
            member_type=shell_str,
            help="Arguments to pass directly to isort, e.g. "
            '`--isort-args="--case-sensitive --trailing-comma"`',
        )
        register(
            "--config",
            type=list,
            member_type=file_option,
            help="Path to `isort.cfg` or alternative isort config file(s)",
        )
