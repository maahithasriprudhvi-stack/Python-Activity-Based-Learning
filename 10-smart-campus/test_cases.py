# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Full session and shared resources',
        (
            '1\nR1\nAnu\n2\nR1\n9\n10\n3\nR1\n70 80 90\n4\nR1\nSports\n5\nC'
            'lub A\n6\n5\nClub B\n5\n6\n0\n'
        ),
        [
            'Student added: R1 Anu',
            'Attendance: 90.00%',
            'Average: 80.00',
            'Event registered: R1 SPORTS',
            'Allocated 6. Available: 4',
            'Not enough laptops. Available: 4',
            'Students: 1',
            'Event registrations: 1',
            'Laptops remaining: 4',
            'Session ended.',
        ],
        [
            'Club B - 5 laptops',
        ],
    ),
    (
        'Duplicate student does not consume menu input',
        '1\nR1\nAnu\n1\nR1\n6\n0\n',
        [
            'Student already exists.',
            'Students: 1',
            'Session ended.',
        ],
        [],
    ),
    (
        'Unknown student',
        '2\nUNKNOWN\n0\n',
        [
            'Student not found.',
            'Session ended.',
        ],
        [],
    ),
    (
        'Attendance and marks validation',
        '1\nR1\nAnu\n2\nR1\n3\n0\n3\nR1\n80 101 90\n6\n0\n',
        [
            'Invalid attendance values.',
            'Enter 3 whole-number marks from 0 to 100.',
            'Attendance: not recorded',
            'Marks: not recorded',
        ],
        [],
    ),
    (
        'Duplicate event',
        '1\nR1\nAnu\n4\nR1\nSports\n4\nR1\nsports\n6\n0\n',
        [
            'Already registered for this event.',
            'Event registrations: 1',
        ],
        [],
    ),
    (
        'Exact resource capacity',
        '5\nClub\n10\n5\nOther\n1\n6\n0\n',
        [
            'Allocated 10. Available: 0',
            'Not enough laptops. Available: 0',
            'Laptops remaining: 0',
        ],
        [],
    ),
    (
        'Invalid option and quantity',
        '9\n5\nClub\n-1\n0\n',
        [
            'Invalid choice.',
            'Enter a positive whole number.',
            'Session ended.',
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
