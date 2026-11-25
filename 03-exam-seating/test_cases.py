# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Empty room',
        '0\n',
        [
            'Positions: 20 | Reserved: 2 | Blocked: 9',
            'Available student seats: 9',
            'Assigned: 0 | Unseated: 0',
        ],
        [],
    ),
    (
        'Some students',
        '3\n',
        [
            'S01',
            'S02',
            'S03',
            'Assigned: 3 | Unseated: 0',
        ],
        [
            'S04',
        ],
    ),
    (
        'Exact capacity',
        '9\n',
        [
            'Assigned: 9 | Unseated: 0',
            'S09',
        ],
        [
            'S10',
        ],
    ),
    (
        'Over capacity',
        '12\n',
        [
            'Assigned: 9 | Unseated: 3',
        ],
        [],
    ),
    (
        'Invalid count',
        '-1\n',
        [
            'Enter a non-negative whole number.',
        ],
        [],
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
