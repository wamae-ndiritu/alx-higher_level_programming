#!/usr/bin/python3

import dis

def print_name_in_pyc(filename):
    with open(filename, 'rb') as pyc_file:
        magic = pyc_file.read(4)
        timestamp = pyc_file.read(4)
        pyc_file.read()

        code_object = pyc_file.read()

        # Disassemble the bytecode and print names

        try:
            code = compile(code_object, '', 'exec')
            names = set()
            for instruction in dis.get_instructions(code):
                if instruction.opname == 'LOAD_CONST':
                    const_index = instruction.arg
                    const_value = code.co_consts[const_index]
                    if isinstance(const_value, str):
                        names.add(instruction.argval)
            return names
        except:
            print("Error disassembling the bytecode.")


extracted_names = print_name_in_pyc('hidden_4.pyc')
for name in extracted_names:
    print(name)
