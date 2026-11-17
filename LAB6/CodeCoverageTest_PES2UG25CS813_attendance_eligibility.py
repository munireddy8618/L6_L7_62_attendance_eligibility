import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)

@pytest.mark.parametrize("attended,total,medical,expected", [
    (30, 40, 0, 75),
    (20, 40, 7, 62),
    (39, 40, 5, 100),
    (0, 10, 0, 0),
])
def test_attendance_percent_valid(attended, total, medical, expected):
    assert attendance_percent(attended, total, medical) == expected


@pytest.mark.parametrize("attended,total,medical,error", [
    (10, 0, 0, "invalid total"),
    (10, -1, 0, "invalid total"),
    (-1, 10, 0, "invalid attended count"),
    (11, 10, 0, "invalid attended count"),
])
def test_attendance_percent_invalid(attended, total, medical, error):
    with pytest.raises(ValueError, match=error):
        attendance_percent(attended, total, medical)


def test_exam_eligibility():
    assert exam_eligibility(80, False, False) == "fees pending"
    assert exam_eligibility(75, False, True) == "eligible"
    assert exam_eligibility(70, True, True) == "eligible"
    assert exam_eligibility(70, False, True) == "condonation required"
    assert exam_eligibility(64, True, True) == "detained"


def test_attendance_warning():
    assert attendance_warning(85, 1) is None
    assert attendance_warning(80, 1) == "reminder"
    assert attendance_warning(74, 5) == "critical"
    assert attendance_warning(74, 4) == "final notice"
