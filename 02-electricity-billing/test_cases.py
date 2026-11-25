# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Slab boundaries',
        '3\nA\n100\nB\n200\nC\n201\n',
        [
            'A: energy Rs 300.00',
            'Bill: Rs 350.00',
            'B: energy Rs 800.00',
            'Bill: Rs 850.00',
            'C: energy Rs 807.00',
            'Bill: Rs 857.00',
        ],
        [],
    ),
    (
        'Surcharge boundary',
        '2\nA\n300\nB\n301\n',
        [
            'A: energy Rs 1500.00, fixed Rs 50.00, surcharge Rs 0.00',
            'B: energy Rs 1507.00, fixed Rs 50.00, surcharge Rs 75.35',
            'Bill: Rs 1632.35',
        ],
        [],
    ),
    (
        'Rebate and bill change',
        '2\nA\n200\nB\n100\n',
        [
            'rebate Rs 15.00',
            'Bill: Rs 335.00',
            'Bill change: -60.59%',
        ],
        [
            'Unusual increase',
        ],
    ),
    (
        'Unusual increase uses bills',
        '2\nA\n100\nB\n200\n',
        [
            'Bill change: +142.86%',
            'Unusual increase: more than 30%',
        ],
        [],
    ),
    (
        'Zero and invalid month',
        '3\nA\n0\nBad\n-4\nB\n1\n',
        [
            'Bill: Rs 50.00',
            'record skipped',
            'Bill: Rs 53.00',
            'Bill change: +6.00%',
        ],
        [
            'Unusual increase',
        ],
    ),
]

for name, data, expected, forbidden in cases:
    result = subprocess.run(
        [sys.executable, str(solution)], input=data, text=True,
        capture_output=True, timeout=10
    )
    assert result.returncode == 0, f"{name}: program failed: {result.stderr}"
    for text in expected:
        assert text in result.stdout, f"{name}: missing {text!r}\n{result.stdout}"
    for text in forbidden:
        assert text not in result.stdout, f"{name}: unexpected {text!r}"
    print("PASS:", name)

print(f"{len(cases)} tests passed.")
