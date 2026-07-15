"""Build the Unification Report PDF (ED_UnifiedFramework_Report.md).

Reuses _build_papers.py's pre-latexify machinery (unicode -> LaTeX before pandoc,
so no font-coverage fights), but keeps the report whole: its own title, subtitle,
and abstract are preserved (unlike the Paper_* builder, which strips a metadata
preamble). Extends the char maps with the report's status emoji and a few extra
math symbols. Usage: python _build_report.py
"""
import subprocess, os, sys, re
import _build_papers as bp

EDG = r"C:\Users\allen\GitHub\ED Generative"
SRC = os.path.join(EDG, "ED_UnifiedFramework_Report.md")
BASE = "ED_UnifiedFramework_Report"

# --- extend the math map with glyphs the report uses that Paper_* did not ---
bp.CMD.update({
    "⟨": r"\langle", "⟩": r"\rangle", "⊗": r"\otimes", "∀": r"\forall",
    "⊊": r"\subsetneq", "≅": r"\cong", "↦": r"\mapsto", "ℂ": r"\mathbb{C}",
    "ℍ": r"\mathbb{H}", "′": r"'", "∅": r"\varnothing", "⊆": r"\subseteq",
    "≪": r"\ll", "≫": r"\gg", "ħ": r"\hbar", "ψ": r"\psi",
    # status marks -> plain math glyphs (amssymb); the §2 legend explains them
    "✅": r"\checkmark", "⚠": r"\triangle", "📏": r"\square", "⭐": r"\bigstar",
})
bp.CODE.update({
    "⟨": "<", "⟩": ">", "⊗": "(x)", "∀": "all ", "⊊": "(c)", "≅": "~=",
    "↦": "|->", "ℂ": "C", "ℍ": "H", "ħ": "hbar", "ψ": "psi", "⊆": "(=",
    "≪": "<<", "≫": ">>", "′": "'",
})
# recompute the math-class set now that CMD grew
bp.MATHCLASS = set(bp.SUP) | set(bp.SUB) | set(bp.CMD)

# raw text chars Latin Modern renders directly (superset of bp.TEXT_OK)
TEXT_OK = set("—–§…öřČéèüïàáçñ")

def coverage(text):
    import unicodedata
    miss = sorted({c for c in text if ord(c) > 127
                   and c not in bp.MATHCLASS and c not in TEXT_OK})
    if miss:
        out = "UNMAPPED: " + "  ".join(
            f"U+{ord(c):04X} {unicodedata.name(c,'?')}" for c in miss)
        sys.stdout.buffer.write((out + "\n").encode("utf-8"))
    return miss

def main():
    text = open(SRC, encoding="utf-8").read()
    text = text.replace("️", "")          # drop emoji variation selectors
    # conjugate-rep notation written with a combining macron in code spans ->
    # proper math (base + U+0304 renders nowhere; \bar{} does)
    text = text.replace("`2 ≅ 2̄`", r"$2 \cong \bar{2}$")
    text = text.replace("`N̄`", r"$\bar{N}$")
    if coverage(text):
        print("  -> add these to bp.CMD/TEXT_OK before building"); sys.exit(2)
    body = bp.latexify(text)                    # unicode -> LaTeX, prose/math/code aware
    work = os.path.join(EDG, "_report_tmp.md")
    open(work, "w", encoding="utf-8", newline="\n").write(body)
    hdr = os.path.join(EDG, "_report_header.tex")
    open(hdr, "w", encoding="utf-8").write(
        "\\usepackage{amsmath}\n\\usepackage{amssymb}\n"
        "\\setcounter{secnumdepth}{-1}\n\\providecommand{\\tightlist}{}\n"
        "\\usepackage{microtype}\n\\usepackage{longtable,booktabs}\n")
    r = subprocess.run(["pandoc", "_report_tmp.md", "-s",
                        "--include-in-header=_report_header.tex",
                        "-V", "geometry:margin=1in", "-V", "fontsize=10pt",
                        "-o", BASE + ".tex"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=EDG)
    if r.returncode != 0:
        print("PANDOC FAIL:", (r.stderr or "")[-500:]); sys.exit(1)
    log = ""
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                            BASE + ".tex"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", cwd=EDG)
        log = r.stdout or ""
    pdf = os.path.join(EDG, BASE + ".pdf")
    ok = os.path.exists(pdf) and r.returncode == 0
    if not ok:
        i = log.find("\n!"); print("XELATEX FAIL:\n" + (log[i:i+700] if i >= 0 else log[-700:]))
    for f in [BASE + ".aux", BASE + ".out", BASE + ".toc", BASE + ".log",
              "_report_tmp.md", "_report_header.tex", BASE + ".tex"]:
        p = os.path.join(EDG, f)
        if os.path.exists(p):
            try: os.remove(p)
            except OSError: pass
    if ok:
        print(f"OK  {BASE}.pdf  ({os.path.getsize(pdf)//1024} KB)")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
