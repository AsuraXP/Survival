#!/usr/bin/env python3
"""
qc.py — mechanical frame QC for long_cold_video.
Costs zero image-generation budget. Run before every commit.

Checks:
  1. Coverage      — which of the 289 CSV rows have a frame, which are missing.
  2. Naming        — every file must map to an existing CSV row (orphans flagged).
  3. Consistency   — resolution uniformity, aspect ratio drift.
  4. Near-dupes    — dHash hamming distance vs the PREVIOUS frame; too-similar = framing repeat.
  5. Palette       — per-frame mean warmth; flags frames that break the ochre/slate balance.

Usage:  python3 qc.py            # full report
        python3 qc.py --strict   # exit 1 if any FAIL
"""
import csv, os, sys, glob
from PIL import Image

CSV = 'visuals.csv'
FRAMES = 'frames'
DUPE_HAMMING = 6          # <= this = suspiciously similar neighbours
WARMTH_ABS_MIN = 0.55    # R/B floor: colder than this is off-palette even for night
WARMTH_DEV = 0.30        # max deviation from the batch median warmth


def dhash(path, size=8):
    im = Image.open(path).convert('L').resize((size + 1, size), Image.LANCZOS)
    px = list(im.getdata())
    bits = 0
    for row in range(size):
        for col in range(size):
            i = row * (size + 1) + col
            bits = (bits << 1) | (1 if px[i] > px[i + 1] else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count('1')


def warmth(path):
    im = Image.open(path).convert('RGB').resize((64, 36), Image.LANCZOS)
    px = list(im.getdata())
    r = sum(p[0] for p in px) / len(px)
    b = sum(p[2] for p in px) / len(px)
    return r / max(b, 1e-6)


def main():
    rows = list(csv.DictReader(open(CSV)))
    expected = [f"beat{int(r['slide_id']):02d}m{int(r['moment']):02d}" for r in rows]
    have = {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(f'{FRAMES}/beat*.png')}

    fails, warns = [], []

    missing = [e for e in expected if e not in have]
    orphans = [h for h in have if h not in expected]

    print(f"CSV rows      : {len(expected)}")
    print(f"frames present: {len(have)}")
    print(f"missing       : {len(missing)}")
    if orphans:
        print(f"ORPHANS       : {orphans}")
        fails.append(f"{len(orphans)} orphan frame(s) with no CSV row")

    # resolution consistency
    sizes, warmth_by = {}, {}
    for name, path in sorted(have.items()):
        im = Image.open(path)
        sizes.setdefault(im.size, []).append(name)
        warmth_by[name] = warmth(path)
    print(f"\nresolutions   : {len(sizes)} distinct")
    for s, names in sizes.items():
        ar = s[0] / s[1]
        tag = 'OK' if 1.60 <= ar <= 2.05 else 'ODD'
        print(f"  {s[0]}x{s[1]}  ar={ar:.3f} [{tag}]  x{len(names)}")
        if tag == 'ODD':
            warns.append(f"aspect {ar:.3f} on {names[:3]}")

    # sequential near-dupe + palette scan in CSV order
    seq = [e for e in expected if e in have]
    prev_hash = None
    prev_name = None
    dupe_report, warm_report = [], []
    for name in seq:
        h = dhash(have[name])
        if prev_hash is not None:
            d = hamming(h, prev_hash)
            if d <= DUPE_HAMMING:
                dupe_report.append((prev_name, name, d))
        prev_hash, prev_name = h, name
        w = warmth_by[name]
        warm_report.append((name, w))
    warm_vals = sorted(v for _, v in warm_report) or [1.0]
    median_w = warm_vals[len(warm_vals) // 2]
    warm_report = [(n, w) for n, w in warm_report
                   if w < WARMTH_ABS_MIN or abs(w - median_w) > WARMTH_DEV]

    print(f"\nnear-dupe cuts : {len(dupe_report)}  (hamming <= {DUPE_HAMMING})")
    for a, b, d in dupe_report:
        print(f"  {a} -> {b}   distance {d}  <- framing repeat, re-roll one")
        fails.append(f"framing repeat {a}->{b}")

    print(f"palette outliers: {len(warm_report)}  (batch median R/B {median_w:.2f}, tolerance +/-{WARMTH_DEV}, floor {WARMTH_ABS_MIN})")
    for n, w in warm_report:
        print(f"  {n}  warmth {w:.2f}")
        warns.append(f"palette drift on {n} ({w:.2f})")

    print("\n" + "=" * 60)
    if fails:
        print(f"FAIL ({len(fails)})")
        for f in fails:
            print("  -", f)
    else:
        print("PASS — no mechanical failures")
    if warns:
        print(f"WARN ({len(warns)})")
        for w in warns:
            print("  -", w)
    print("=" * 60)
    print("Mechanical checks only. Human gate still required: does each frame show its")
    print("moment_text, two dot eyes or no face, ink line + flat wash, no text, no extras?")

    if '--strict' in sys.argv and fails:
        sys.exit(1)


if __name__ == '__main__':
    main()
