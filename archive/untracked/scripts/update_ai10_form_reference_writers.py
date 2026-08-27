from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "rahul_gupta_ai10_nomination_form.docx"
DEST = ROOT / "output" / "ai10_yang_packet" / "rahul_gupta_ai10_nomination_form_for_yang.docx"

REPLACEMENTS = {
    "Kai-Wei Chang": "Kush R. Varshney",
    "Professor of Computer Science, UCLA; Amazon Scholar, Amazon AGI": (
        "IBM Fellow, IBM Research; IEEE Fellow; leader in human-centered trustworthy AI"
    ),
    "Email: [insert email]": "Email: [insert email]",
}


def replace_in_docx(src: Path, dest: Path) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        with ZipFile(src, "r") as zin:
            zin.extractall(tmp)

        for xml_path in (tmp / "word").glob("*.xml"):
            text = xml_path.read_text(encoding="utf-8")
            original = text
            for old, new in REPLACEMENTS.items():
                text = text.replace(old, new)
            if text != original:
                xml_path.write_text(text, encoding="utf-8")

        dest.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(dest, "w", ZIP_DEFLATED) as zout:
            for path in tmp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp))


if __name__ == "__main__":
    replace_in_docx(SRC, DEST)
