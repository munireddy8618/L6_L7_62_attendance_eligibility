import pytest
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)

@pytest.mark.parametrize("total", [0, -2])
def test_invalid_total(total):
    with pytest.raises(ValueError, match="invalid total"):
        attendance_percent(0, total, 0)

def test_valid_total():
    assert attendance_percent(5, 10, 0) == 50

def test_attended_below_zero():
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(-1, 10, 0)

def test_attended_above_total():
    with pytest.raises(ValueError, match="invalid attended count"):
        attendance_percent(11, 10, 0)

def test_attended_in_range():
    assert attendance_percent(5, 10, 0) == 50

def test_medical_leave_capped():
    assert attendance_percent(2, 10, 6) == 70

def test_medical_leave_not_capped():
    assert attendance_percent(2, 10, 5) == 70

def test_credited_attendance_capped():
    assert attendance_percent(9, 10, 5) == 100

def test_credited_attendance_not_capped():
    assert attendance_percent(2, 10, 1) == 30

def test_fees_pending():
    assert exam_eligibility(90, True, False) == "fees pending"

def test_75_percent_eligible():
    assert exam_eligibility(75, False, True) == "eligible"

def test_condonation_approved():
    assert exam_eligibility(65, True, True) == "eligible"

def test_condonation_required():
    assert exam_eligibility(65, False, True) == "condonation required"

def test_detained():
    assert exam_eligibility(64, True, True) == "detained"

def test_warning_at_least_85():
    assert attendance_warning(85, 10) is None

def test_warning_reminder():
    assert attendance_warning(75, 10) == "reminder"

def test_warning_critical():
    assert attendance_warning(74, 5) == "critical"

def test_warning_final_notice():
    assert attendance_warning(74, 4) == "final notice"
