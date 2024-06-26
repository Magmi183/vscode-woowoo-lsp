"""Implementation of tool support over LSP."""

from __future__ import annotations

import logging
import logging.config
import os
import pathlib
import site
import sys

BUNDLE_DIR = pathlib.Path(__file__).parent.parent
logger = logging.getLogger(__name__)


def update_sys_path(path_to_add: str) -> None:
    """Add given path to `sys.path`."""
    if os.path.isdir(path_to_add):
        # The `site` module adds the directory at the end, if not yet present; we want
        # it to be at the beginning, so that it takes precedence over any other
        # installed versions.
        sys.path.insert(0, path_to_add)

        # Allow development versions of libraries to be imported.
        site.addsitedir(path_to_add)


def main():
    # inspired by: https://github.com/astral-sh/ruff-vscode/tree/main
    from woowoo_pygls import server

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "simple": {"format": "%(asctime)s %(levelname)-4s %(message)s"}
            },
            "handlers": {
                "stderr": {
                    "class": "logging.StreamHandler",
                    "formatter": "simple",
                },
            },
            "root": {"level": "INFO", "handlers": ["stderr"]},
            "loggers": {
                # Don't repeat every message
                "pygls.protocol": {
                    "level": "WARN",
                    "handlers": ["stderr"],
                    "propagate": False,
                },
            },
        }
    )

    
    server.start()


# Start the server.
if __name__ == "__main__":
    # Ensure that we can import LSP libraries, and other bundled libraries.
    update_sys_path(os.fspath(BUNDLE_DIR / "libs"))

    server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'woowoo_pygls')
    update_sys_path(server_path)

    main()
