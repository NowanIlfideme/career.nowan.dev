"""Make the resume.

Pre-requisites:

1. npm is installed:

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

2. resumed is installed

    npm install resumed jsonresume-theme-stackoverflow
"""

from pathlib import Path
import subprocess
from typing import Any
import yaml

from pydantic import RootModel


class Resume(RootModel[dict[str, Any]]):
    """Resume model is just a dict."""


if __name__ == "__main__":
    """

    "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json",
    """
    dir_out = Path("output").resolve()
    f_json = Path("resume.json")
    f_pdf = dir_out / "resume.pdf"
    with Path("resume.yaml").open() as f_in:
        raw = yaml.load(f_in, yaml.SafeLoader)
    resume = Resume(raw)
    f_json.write_text(resume.model_dump_json(indent=2))
    subprocess.run(
        [
            "npx",
            "resume",  # not resumed because it's buggy :(
            "export",
            "--theme",
            "stackoverflow",
            str(f_pdf),
        ],
    )
    f_json.unlink()
