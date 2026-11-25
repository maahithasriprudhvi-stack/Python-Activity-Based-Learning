# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Repeated runs',
        'aaaaabb\n',
        [
            'Encoded: a5b2',
            'Original length: 7',
            'Encoded length: 4',
            'Compression is beneficial.',
        ],
        [],
    ),
    (
        'No repeated runs',
        'python\n',
        [
            'Encoded: p1y1t1h1o1n1',
            'Original length: 6',
            'Encoded length: 12',
            'Compression is not beneficial.',
        ],
        [],
    ),
    (
        'Equal lengths',
        'aabb\n',
        [
            'Encoded: a2b2',
            'Original length: 4',
            'Encoded length: 4',
            'Compression is not beneficial.',
        ],
        [],
    ),
    (
        'Two-digit run',
        'aaaaaaaaaaaa\n',
        [
            'Encoded: a12',
            'Original length: 12',
            'Encoded length: 3',
        ],
        [],
    ),
    (
        'Empty text',
        '\n',
        [
            'Original length: 0',
            'Encoded length: 0',
            'Compression is not beneficial.',
        ],
        [],
    ),
    (
        'Digits not allowed',
        'aa11\n',
        [
            'Invalid input: use letters only.',
        ],
        [],
    ),
    (
        'Case sensitivity',
        'AAaa\n',
        [
            'Encoded: A2a2',
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
