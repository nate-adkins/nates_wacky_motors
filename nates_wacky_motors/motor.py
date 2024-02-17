
import can

def _ensure_can_message_and_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        found_can_message = False
        found_function = False

        for item in result:
            if isinstance(item, can.Message):
                found_can_message = True
            if callable(item) and isinstance(item([0]*8), (list, tuple)) and len(item([0]*8)) == 8:
                found_function = True

        if not found_can_message:
            raise TypeError(f"Function {func.__name__} must return a can.Message object.")
        if not found_function:
            raise TypeError(f"Function {func.__name__} must return a function that takes in an 8-element list.")
        
        return result
    return wrapper

@_ensure_can_message_and_function
def return_format(can_id):
    pass

@_ensure_can_message_and_function
def create_can_command(can_id):
    pass

@_ensure_can_message_and_function
def read_pid(can_id):
    pass

@_ensure_can_message_and_function
def write_pid_ram(can_id):
    pass

@_ensure_can_message_and_function
def write_pid_rom(can_id):
    pass
@_ensure_can_message_and_function
def read_acceleration(can_id):
    pass

@_ensure_can_message_and_function
def write_acceleration(can_id):
    pass

@_ensure_can_message_and_function
def read_encoder_position(can_id):
    pass

@_ensure_can_message_and_function
def read_encoder_original_position(can_id):
    pass

@_ensure_can_message_and_function
def read_encoder_zero_offset(can_id):
    pass

@_ensure_can_message_and_function
def write_encoder_zero_offset(can_id):
    pass

@_ensure_can_message_and_function
def write_current_position_as_zero_offset(can_id):
    pass

@_ensure_can_message_and_function
def read_single_turn_encoder_position(can_id):
    pass

@_ensure_can_message_and_function
def read_multi_turn_angle(can_id):
    pass

@_ensure_can_message_and_function
def read_temp_volt_errors(can_id):
    pass

@_ensure_can_message_and_function
def read_temp_speed_encoder_position(can_id):
    pass

@_ensure_can_message_and_function
def read_temp_and_phase_current(can_id):
    pass

@_ensure_can_message_and_function
def write_shutdown(can_id):
    pass

@_ensure_can_message_and_function
def write_stop(can_id):
    pass

@_ensure_can_message_and_function
def write_torque_control(can_id):
    pass

@_ensure_can_message_and_function
def write_speed_control(can_id):
    pass

@_ensure_can_message_and_function
def write_position_control_multi_turn(can_id):
    pass

@_ensure_can_message_and_function
def write_position_control_single_turn(can_id):
    pass

@_ensure_can_message_and_function
def write_position_control_incremental_single_turn(can_id):
    pass

@_ensure_can_message_and_function
def read_operating_mode(can_id):
    pass

@_ensure_can_message_and_function
def read_power_draw(can_id):
    pass

@_ensure_can_message_and_function
def write_reset(can_id): # need to clear buffer after sending this 
    pass

@_ensure_can_message_and_function
def write_break_release(can_id):
    pass

@_ensure_can_message_and_function
def write_break_lock(can_id):
    pass

@_ensure_can_message_and_function
def read_runtime_length(can_id):
    pass

@_ensure_can_message_and_function
def read_software_version(can_id):
    pass

@_ensure_can_message_and_function
def write_timeout_length(can_id):
    pass

@_ensure_can_message_and_function
def write_baudrate(can_id):
    pass

@_ensure_can_message_and_function
def read_motor_model(can_id):
    pass

# 2 part can message kinda
@_ensure_can_message_and_function
def write_clear_multi_turn(can_id):
    pass

@_ensure_can_message_and_function
def write_enable_can_id_filter(can_id):
    pass

@_ensure_can_message_and_function
def write_multi_motor(can_id):
    pass

@_ensure_can_message_and_function
def write_canid_settings(can_id):
    pass
