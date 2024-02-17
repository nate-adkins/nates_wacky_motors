

class MyActuatorCanCommand():

    def __init__(self):
        self.name: str
        self.input_parameters: dict[(str,int)]
        self.output: function
        self.ouput_parameters: dict[(str,int)]


class MultiBytePopulator():

    def __init__(self):
        self.integer_value: int
        self.start_index_in_byte_array: int
        self.num_bytes_populated: int 

    