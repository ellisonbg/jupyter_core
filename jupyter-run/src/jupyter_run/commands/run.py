import logging

from jupyter_core.application import JupyterApp, base_aliases, base_flags
from jupyter_core.paths import jupyter_runtime_dir

from traitlets import (
    Any,
    Bool,
    Bytes,
    Dict,
    Float,
    Instance,
    Integer,
    List,
    TraitError,
    Type,
    Unicode,
    Union,
    default,
    observe,
    validate,
)
from traitlets.config import Config
from traitlets.config.application import boolean_flag, catch_config_error


# -----------------------------------------------------------------------------
# App variables Aliases
# -----------------------------------------------------------------------------

_examples = """
jupyter run --help                      # Show the CLI help
"""

flags = dict(base_flags)

# flags["allow-root"] = (
#     {"ServerApp": {"allow_root": True}},
#     _i18n("Allow the server to be run from root user."),
# )

aliases = dict(base_aliases)

# aliases.update(
#     {
#         "ip": "ServerApp.ip",
#     }
# )

# -----------------------------------------------------------------------------
# ServerApp
# -----------------------------------------------------------------------------


class JupyterRunApp(JupyterApp):
    """The Jupyter Run application class."""

    name = "jupyter-run"
    description: str = """Run Jupyter on the cloud provider of your choice."""
    examples = _examples

    flags = Dict(flags)  # type:ignore[assignment]
    aliases = Dict(aliases)  # type:ignore[assignment]

    classes = [
    ]

    # subcommands: dict[str, t.Any] = {
    #     "list": (
    #         JupyterServerListApp,
    #         JupyterServerListApp.description.splitlines()[0],
    #     ),
    #     "stop": (
    #         JupyterServerStopApp,
    #         JupyterServerStopApp.description.splitlines()[0],
    #     ),
    #     "password": (
    #         JupyterPasswordApp,
    #         JupyterPasswordApp.description.splitlines()[0],
    #     ),
    #     "extension": (
    #         ServerExtensionApp,
    #         ServerExtensionApp.description.splitlines()[0],
    #     ),
    # }

    @default("log_level")
    def _default_log_level(self) -> int:
        return logging.INFO


main = JupyterRunApp.launch_instance
