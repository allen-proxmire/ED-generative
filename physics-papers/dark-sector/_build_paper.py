r"""Build Paper_ED_DarkSector .pdf/.tex in the corpus report style:
pandoc + xelatex, main=Cambria, mono=Consolas, math=Latin Modern Math (unicode-math),
rendering source Unicode DIRECTLY. Glyphs the mono/main font lacks inside code spans map
to a Latin Modern Math fallback via \symbol (works in \texttt, unlike \ensuremath).

Strips the 6-line md title block and passes title/author/date as metadata for a centered
\maketitle (paper convention). Outputs: PDF next to the .md AND to the Zenodo folder; TeX to
the tex folder.
"""
import subprocess, os, sys, shutil

FOLDER = r"C:\Users\allen\GitHub\ED Generative\physics-papers\dark-sector"
SRC = "Paper_ED_DarkSector.md"
BASE = "Paper_ED_DarkSector"
TITLE = ("The Event Density Dark Sector: MOND as Horizon Interference, a Warm Relic "
         "for the Cosmic Web, and a Falsifiable Bet Against Cold Dark Matter")
ZENODO = r"C:\Users\allen\Desktop\ED Important\ED_pdf_files"
TEXDIR = r"C:\Users\allen\Desktop\ED Important\ED_tex_files"

HEADER = r"""
\usepackage{fontspec}
\usepackage{unicode-math}
\usepackage{newunicodechar}
\setmainfont{Cambria}
\setmonofont{Consolas}[Scale=0.92]
\setmathfont{Latin Modern Math}
\newfontfamily\symfb{Latin Modern Math}
\providecommand{\tightlist}{}
\usepackage{longtable,booktabs}
% glyphs the mono/main font may lack inside inline-code spans -> Latin Modern Math via \symbol
\newunicodechar{∇}{{\symfb\symbol{"2207}}}
\newunicodechar{∝}{{\symfb\symbol{"221D}}}
\newunicodechar{√}{{\symfb\symbol{"221A}}}
\newunicodechar{⟹}{{\symfb\symbol{"27F9}}}
\newunicodechar{→}{{\symfb\symbol{"2192}}}
\newunicodechar{↔}{{\symfb\symbol{"2194}}}
\newunicodechar{∈}{{\symfb\symbol{"2208}}}
"""

def build(body):
    open("_paper_header.tex", "w", encoding="utf-8").write(HEADER)
    open("_body.md", "w", encoding="utf-8").write(body)
    common = ["--include-in-header=_paper_header.tex", "-V", "geometry:margin=1in",
              "-V", "fontsize=11pt", "-V", "title=" + TITLE,
              "-V", "author=Allen Proxmire", "-V", "date=July 2026"]
    # .tex
    r = subprocess.run(["pandoc", "_body.md", "-s"] + common + ["-o", BASE + ".tex"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("PANDOC(tex) FAIL:", (r.stderr or "")[-800:]); return False
    # pdf via two xelatex passes on the .tex
    log = ""
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", BASE + ".tex"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        log = r.stdout or ""
    ok = os.path.exists(BASE + ".pdf") and r.returncode == 0
    miss = sorted(set(l for l in log.splitlines() if "Missing character" in l))
    dollar = [l for l in log.splitlines() if "Missing $ inserted" in l]
    if miss:
        sys.stdout.buffer.write(b"MISSING GLYPHS:\n" + "\n".join(miss[:25]).encode("utf-8", "replace") + b"\n")
    if dollar:
        print(f"MISSING-$ errors: {len(dollar)} (code-span math gotcha)")
    if not ok:
        i = log.find("\n!"); print("XELATEX FAIL:\n" + (log[i:i+900] if i >= 0 else log[-900:]))
    return ok and not miss and not dollar

def main():
    os.chdir(FOLDER)
    raw = open(SRC, encoding="utf-8").read().splitlines()
    body = "\n".join(raw[6:])  # drop the 6-line title block (title/author/date)
    ok = build(body)
    if ok:
        for d in (ZENODO,):
            shutil.copyfile(BASE + ".pdf", os.path.join(d, BASE + ".pdf"))
        shutil.copyfile(BASE + ".tex", os.path.join(TEXDIR, BASE + ".tex"))
        print(f"OK  {BASE}.pdf  ({os.path.getsize(BASE + '.pdf')//1024} KB)  "
              f"-> repo + Zenodo; .tex -> {TEXDIR}")
    for f in [BASE + e for e in (".aux", ".out", ".toc", ".log")] + ["_paper_header.tex", "_body.md", "_charaudit.txt"]:
        if os.path.exists(f):
            try: os.remove(f)
            except OSError: pass
    # keep BASE.tex in the folder only transiently; the canonical tex is in TEXDIR
    if ok and os.path.exists(BASE + ".tex"):
        os.remove(BASE + ".tex")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
