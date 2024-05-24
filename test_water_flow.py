from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

from pytest import approx
import pytest


def test_water_column_height():

    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():

    assert pressure_gain_from_water_height(0, 0) == 0.001
    assert pressure_gain_from_water_height(30.2, 295.628) == 0.001
    assert pressure_gain_from_water_height(50, 489.450) == 0.001


def pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == 0
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == -113.008
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == -100.462
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == -61.576
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == -110.884

"""
                                            Expected     approx
Pipe        Pipe    Friction   Fluid       Pressure     Absolute
Diameter	Length  Factor     Velocity    Loss         Tolerance
0.048692	0	    0.018	    1.75	    0	        0.001	
0.048692	200	    0	        1.75	    0	        0.001
0.048692	200	    0.018	    0	        0	        0.001	
0.048692	200	    0.018	    1.75	    -113.008	0.001
0.048692	200	    0.018	    1.65	    -100.462	0.001
0.28687	    1000	0.013	    1.65	    -61.576	    0.001
0.28687	    1800.75	0.013	    1.65	    -110.884	0.001	
"""





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
