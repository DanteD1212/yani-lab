import math

import pytest

from app.models.ph import PHRequest, PHCalculationType, PHError
from app.services.ph_service import PHService

def test_strong_acid_ph_calculation():
    request = PHRequest(
        calculation_type=PHCalculationType.STRONG_ACID,
        concentration_m=0.01,
        equivalents=1.0,
        kw=1e-14,
    )

    result = PHService.calculate(request)

    assert math.isclose(result.ph, 2.0, rel_tol=1e-4)
    assert math.isclose(result.poh, 12.0, rel_tol=1e-4)
    assert math.isclose(result.hydronium, 0.01, rel_tol=1e-9)
    assert math.isclose(result.hydroxide, 1e-12, rel_tol=1e-9)
    assert result.notes is None

def test_strong_base_ph_calculation():
    request = PHRequest(
        calculation_type=PHCalculationType.STRONG_BASE,
        concentration_m=0.05,
        equivalents=2.0,
        kw=1e-14,
    )

    result = PHService.calculate(request)

    assert math.isclose(result.poh, 1.0, rel_tol=1e-4)
    assert math.isclose(result.ph, 13.0, rel_tol=1e-4)
    assert math.isclose(result.hydroxide, 0.1, rel_tol=1e-9)
    assert math.isclose(result.hydronium, 1e-13, rel_tol=1e-9)

def test_very_dilute_solution_adds_note():
    request = PHRequest(
        calculation_type=PHCalculationType.STRONG_ACID,
        concentration_m=1e-15,
        equivalents=1.0,
        kw=1e-14,
    )

    result = PHService.calculate(request)

    assert result.notes is not None
    assert result.hydronium == pytest.approx(PHService.MIN_CONCENTRATION)

def test_invalid_concentration_raises_error():
    request = PHRequest(
        calculation_type=PHCalculationType.STRONG_BASE,
        concentration_m=-0.1,
        equivalents=1.0,
        kw=1e-14,
    )

    with pytest.raises(PHError):
        PHService.calculate(request)
