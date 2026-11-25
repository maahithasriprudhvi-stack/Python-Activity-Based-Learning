# Automated checks for solution.py (Python standard library only).
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name("solution.py")
cases = [
    (
        'Deposit and withdrawal',
        '1\n2000\n2\n3000\n4\n0\n',
        [
            'Deposited Rs 2000. Balance: Rs 7000',
            'Withdrawn Rs 3000. Balance: Rs 4000',
            'Deposit: Rs 2000 | Balance: Rs 7000',
            'Withdraw: Rs 3000 | Balance: Rs 4000',
            'Closing balance: Rs 4000',
        ],
        [],
    ),
    (
        'Minimum balance boundary',
        '2\n4000\n0\n',
        [
            'Withdrawn Rs 4000. Balance: Rs 1000',
            'Closing balance: Rs 1000',
        ],
        [],
    ),
    (
        'Minimum balance rejection',
        '2\n4100\n4\n0\n',
        [
            'Minimum balance of Rs 1000 must remain.',
            'No successful transactions.',
            'Closing balance: Rs 5000',
        ],
        [],
    ),
    (
        'Limits and denomination',
        '1\n100001\n2\n10100\n2\n150\n0\n',
        [
            'Deposit limit is Rs 100000.',
            'Withdrawal limit is Rs 10000.',
            'Withdrawal must be a multiple of Rs 100.',
            'Closing balance: Rs 5000',
        ],
        [],
    ),
    (
        'Invalid amounts',
        '1\nnan\n1\n-2\n1\n0\n0\n',
        [
            'Enter a positive whole number of rupees.',
            'Closing balance: Rs 5000',
        ],
        [
            'Deposited Rs',
        ],
    ),
    (
        'Unknown option',
        '9\n0\n',
        [
            'Invalid choice.',
            'Closing balance: Rs 5000',
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
