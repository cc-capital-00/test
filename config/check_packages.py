import importlib.metadata
import subprocess
import sys
from pathlib import Path


def check_and_install():
    requirements_file = (
        Path(__file__).resolve().parent.parent / "requirements.txt"
    )

    try:
        from packaging.requirements import Requirement
    except ImportError:
        print("Installing packaging for requirement checks...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "packaging"
        ])
        from packaging.requirements import Requirement

    missing = []

    for line in requirements_file.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        req = Requirement(line)

        if req.marker is not None and not req.marker.evaluate():
            continue

        try:
            version = importlib.metadata.version(req.name)

            if req.specifier.contains(version, prereleases=True):
                print(f"[OK] {req.name}: {version}")
            else:
                print(f"[UPDATE] {req.name}: {version}")
                missing.append(req.name)

        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {req.name}")
            missing.append(req.name)

    if missing:
        print("Installing dependencies from requirements.txt...")
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements_file),
        ])
    else:
        print("All requirements are satisfied.")

