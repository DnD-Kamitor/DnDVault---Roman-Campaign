#!/usr/bin/env python3
"""Generate print-ready PDFs for all handouts, one page per handout, sized to
each handout's actual rendered content instead of a fixed A4 sheet.

Every handout is a physical prop (a torn note, a small card, a scroll) at its
own intentional width. Printing that at A4 with wkhtmltopdf left most of the
page blank -- a narrow strip of content on a mostly-empty sheet. This script
uses Playwright/Chromium instead: it neutralizes the on-screen
full-viewport-centering trick each handout uses for browser display, measures
the content's natural size, and sizes the PDF page to match exactly. No
wasted paper, no distorted scaling, no per-file special-casing.
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

PX_TO_IN = 1 / 96  # Playwright/Chromium CSS px -> inches for PDF page size

HANDOUTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "handouts")
PDF_DIR = os.path.join(HANDOUTS_DIR, "pdf")


def generate_one(page, html_path, out_path):
    page.goto(f"file://{os.path.abspath(html_path)}")
    page.wait_for_load_state("networkidle")
    # Measure under print media, not screen media -- several handouts have a
    # `@media print` rule (e.g. width: 100%) that reflows text differently
    # than the screen layout, so measuring in screen mode undercounts height.
    page.emulate_media(media="print")
    box = page.evaluate(
        """() => {
            // body is a block-level flex container that stretches to fill the
            // viewport by default -- shrink-wrap it to its content instead so
            // getBoundingClientRect reflects the prop's actual size, not the
            // viewport's.
            document.body.style.minHeight = '0';
            document.body.style.height = 'auto';
            document.body.style.display = 'inline-flex';
            const r = document.body.getBoundingClientRect();
            return {width: Math.ceil(r.width), height: Math.ceil(r.height)};
        }"""
    )
    # +2px safety margin: sub-pixel rounding between the measured box and
    # Chromium's actual print layout can otherwise spill a near-empty second
    # page.
    width_in = (max(box["width"], 100) + 2) * PX_TO_IN
    height_in = (max(box["height"], 100) + 2) * PX_TO_IN
    page.pdf(
        path=out_path,
        width=f"{width_in:.3f}in",
        height=f"{height_in:.3f}in",
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
    )


def main():
    os.makedirs(PDF_DIR, exist_ok=True)
    files = sorted(
        glob.glob(os.path.join(HANDOUTS_DIR, "handout_*.html"))
        + glob.glob(os.path.join(HANDOUTS_DIR, "s2_*.html"))
    )
    ok, fail = 0, 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for html in files:
            name = os.path.splitext(os.path.basename(html))[0]
            out = os.path.join(PDF_DIR, f"{name}.pdf")
            try:
                generate_one(page, html, out)
                print(f"  OK  {out}")
                ok += 1
            except Exception as exc:  # noqa: BLE001 -- report and keep going
                print(f"FAIL  {html}: {exc}")
                fail += 1
        browser.close()

    print(f"\nDone: {ok} PDF(s) generated in handouts/pdf/")
    if fail:
        print(f"      {fail} file(s) failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
