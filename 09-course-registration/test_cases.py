# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Valid prerequisites',
        '1\nR1\nCS101 CS201 CS301\n',
        [
            'R1 VALID',
            'Valid: 1 | Invalid: 0',
        ],
        [],
    ),
    (
        'Missing prerequisites and conflict',
        '1\nR2\nCS301 PHY101 PHY102\n',
        [
            'CS301 requires CS201',
            'CS301 requires CS101',
            'PHY101 and PHY102 cannot be combined',
            'R2 INVALID',
        ],
        [],
    ),
    (
        'Duplicate and unknown course',
        '1\nR3\nCS101 CS101 ABC\n',
        [
            'duplicate course CS101',
            'unknown course ABC',
            'Students with violations: R3',
        ],
        [],
    ),
    (
        'Course count limit',
        '1\nR4\nCS101 CS201 CS301 MATH101 PHY101 ENG101\n',
        [
            'more than 5 courses',
        ],
        [],
    ),
    (
        'Empty course list',
        '1\nR5\n\n',
        [
            'at least one course is required',
        ],
        [],
    ),
    (
        'Duplicate student record',
        '2\nR1\nCS101\nR1\nMATH101\n',
        [
            'R1 VALID',
            'duplicate student record',
            'Valid: 1 | Invalid: 1',
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
