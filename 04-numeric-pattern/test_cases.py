# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Height 5',
        '5\n',
        [
            '  1\n 2 2\n3   3\n 2 2\n  1\n',
        ],
        [],
    ),
    (
        'Smallest height',
        '3\n',
        [
            ' 1\n2 2\n 1\n',
        ],
        [],
    ),
    (
        'Largest height',
        '9\n',
        [
            '5       5',
        ],
        [],
    ),
    (
        'Even height',
        '6\n',
        [
            'Invalid height',
        ],
        [],
    ),
    (
        'Non-numeric height',
        'abc\n',
        [
            'Invalid height',
        ],
        [],
    ),
    (
        'Out-of-range height',
        '11\n',
        [
            'Invalid height',
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
