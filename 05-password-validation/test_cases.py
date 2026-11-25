# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Valid at minimum length',
        'Abcd!123\n',
        [
            'VALID',
        ],
        [
            'INVALID',
        ],
    ),
    (
        'Several missing rules',
        'abc\n',
        [
            'INVALID',
            'minimum length is 8',
            'missing uppercase letter',
            'missing digit',
            'missing special character',
        ],
        [],
    ),
    (
        'Prohibited word',
        'Password1!\n',
        [
            'INVALID',
            'contains prohibited text: password',
        ],
        [],
    ),
    (
        'Repeated characters',
        'Aaaa!234\n',
        [
            'INVALID',
            'three identical consecutive characters',
        ],
        [],
    ),
    (
        'Prohibited digits',
        'Zebra!123456\n',
        [
            'contains prohibited text: 123456',
        ],
        [],
    ),
    (
        'Empty password',
        '\n',
        [
            'minimum length is 8',
            'missing uppercase letter',
            'missing lowercase letter',
            'missing digit',
            'missing special character',
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
