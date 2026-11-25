# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Student and subject averages',
        '1\nAna\n60 50 70\n',
        [
            'Ana: total 180, average 60.00',
            'Ana - total 180',
            'Maths: 60.00',
            'Physics: 50.00 - low average',
            'Python: 70.00',
        ],
        [],
    ),
    (
        'Tied top performers',
        '2\nAna\n100 0 80\nBala\n60 60 60\n',
        [
            'Ana - total 180\nBala - total 180',
            'Maths: 80.00',
            'Physics: 30.00 - low average',
        ],
        [],
    ),
    (
        'Invalid record skipped',
        '2\nBad\n101 80 90\nGood\n80 90 100\n',
        [
            'Invalid record',
            'Good: total 270, average 90.00',
            'Maths: 80.00',
        ],
        [
            'Bad: total',
        ],
    ),
    (
        'No valid records',
        '1\n\n20 30 40\n',
        [
            'Invalid record',
            'No valid student records.',
        ],
        [],
    ),
    (
        'Invalid student count',
        '0\n',
        [
            'Enter a number from 1 to 20.',
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
