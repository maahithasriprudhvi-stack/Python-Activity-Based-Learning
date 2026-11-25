# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Cutoffs are inclusive',
        '1\nR01\nMaya\n50 60 70\n75\n500000\n',
        [
            (
                '1. R01 Maya | average 60.00 | attendance 75% | income Rs 50000'
                '0'
            ),
            'Eligible: 1 | Rejected or invalid: 0',
        ],
        [],
    ),
    (
        'Tie rules',
        (
            '4\nR04\nDev\n80 80 80\n90\n200000\nR02\nBen\n80 80 80\n80\n100'
            '000\nR03\nUma\n80 80 80\n90\n300000\nR01\nAna\n80 80 80\n90\n2'
            '00000\n'
        ),
        [
            (
                '1. R01 Ana | average 80.00 | attendance 90% | income Rs 200000'
                '\n2. R04 Dev | average 80.00 | attendance 90% | income Rs 2000'
                '00\n3. R03 Uma | average 80.00 | attendance 90% | income Rs 30'
                '0000\n4. R02 Ben'
            ),
        ],
        [],
    ),
    (
        'All eligibility failures',
        '1\nR10\nSam\n49 40 20\n74\n500001\n',
        [
            'aggregate below 60',
            'a subject is below 50',
            'attendance below 75',
            'income above 500000',
            'Eligible: 0',
        ],
        [],
    ),
    (
        'Invalid mark',
        '1\nR10\nSam\n90 bad 80\n80\n300000\n',
        [
            'Invalid record:',
            'marks must be whole numbers',
            'Rejected or invalid: 1',
        ],
        [],
    ),
    (
        'Duplicate roll',
        (
            '2\nR01\nAna\n80 80 80\n80\n100000\nR01\nAsha\n90 90 90\n90\n10'
            '0000\n'
        ),
        [
            'duplicate roll number',
            'Eligible: 1 | Rejected or invalid: 1',
        ],
        [],
    ),
    (
        'Invalid count',
        '0\n',
        [
            'Enter a positive number of applicants.',
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
