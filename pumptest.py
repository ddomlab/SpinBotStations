from matterlab_pumps import RunzePump

pump = RunzePump(
    com_port='/dev/ttyUSB0',
    address=1,
    syringe_volume=5e-3,
    num_valve_port=12,
    pump_model='SY01C',
)

pump.draw(
    valve_port=1, 
    volume=5, 
    speed=0.5
)

pump.dispense(
    valve_port=2, 
    volume=2.5, 
    speed=0.5
)

pump.dispense(
    valve_port=3, 
    volume=2.5, 
    speed=0.5
)