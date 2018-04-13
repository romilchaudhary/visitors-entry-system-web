import pytest
from visitors_entry_system.visitor_records.models import VisitorDetail
from datetime import datetime

pytestmark = pytest.mark.django_db


def test_visitor_records():
    exit_time = datetime.now()
    visitor_details = VisitorDetail.objects.create(name="romil", email="romil@gmail.com",
                                                   mobile_number=0, exit_time=exit_time)

    assert visitor_details.name == "romil"
    assert str(visitor_details) == "romil"
    assert visitor_details.email == "romil@gmail.com"
    assert visitor_details.mobile_number == 0
    assert visitor_details.exit_time == exit_time
