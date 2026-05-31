from __future__ import print_function

import importlib.util
import os
import re
import sys


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPT_MD = os.path.join(ROOT, "align", "academic_figure_prompt_v0.md")
OUT_DIR = os.path.join(ROOT, "assets", "generated")
OUT_IMAGE = os.path.join(OUT_DIR, "slide3_image2_v0.png")
OUT_EVENTS = os.path.join(OUT_DIR, "slide3_image2_v0.events.jsonl")
CLI_PATH = r"C:\Users\Administrator\.codex\skills\openrouter-icu-image\scripts\openrouter_icu_image.py"


def extract_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "stage_status: confirmed" not in text:
        raise RuntimeError("academic figure prompt is not confirmed")
    match = re.search(r"```text\s*(.*?)\s*```", text, re.S)
    if not match:
        raise RuntimeError("prompt text fence not found")
    return match.group(1).strip()


def load_cli(path):
    spec = importlib.util.spec_from_file_location("openrouter_icu_image_cli", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load OpenRouter ICU image CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    prompt = extract_prompt(PROMPT_MD)
    cli = load_cli(CLI_PATH)
    args = [
        "generate",
        "--prompt",
        prompt,
        "--output",
        OUT_IMAGE,
        "--model",
        "gpt-image-2",
        "--size",
        "1536x864",
        "--quality",
        "medium",
        "--output-format",
        "png",
        "--stream",
        "true",
        "--partial-images",
        "2",
        "--events-output",
        OUT_EVENTS,
    ]
    rc = cli.main(args)
    if rc != 0:
        raise SystemExit(rc)
    print("image:", OUT_IMAGE)
    print("events:", OUT_EVENTS)


if __name__ == "__main__":
    main()
