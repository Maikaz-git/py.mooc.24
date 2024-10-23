def run(program):
    registers = {'A': 0, 'B': 0, 'C': 0, 'Z': 0}
    result = []
    pc = 0

    while pc < len(program):
        line = program[pc]
        tokens = line.split()
        opcode = tokens[0]

        if opcode == 'MOV':
            reg = tokens[1]
            val = int(tokens[2])
            registers[reg] = val

        elif opcode == 'ADD':
            reg1 = tokens[1]
            reg2 = tokens[2]
            registers[reg1] += registers[reg2]

        elif opcode == 'SUB':
            reg1 = tokens[1]
            reg2 = tokens[2]
            registers[reg1] -= registers[reg2]

        elif opcode == 'MUL':
            reg1 = tokens[1]
            reg2 = tokens[2]
            registers[reg1] *= registers[reg2]

        elif opcode == 'PRINT':
            reg = tokens[1]
            result.append(registers[reg])

        elif opcode == 'IF':
            reg = tokens[2]
            cond = tokens[1]
            if cond == '==':
                if registers[reg] == 0:
                    pc += 1
                else:
                    label = tokens[3]
                    for i, line in enumerate(program):
                        if line.startswith(label):
                            pc = i
                            break
            elif cond == '>':
                if registers[reg] > 0:
                    pc += 1
                else:
                    label = tokens[3]
                    for i, line in enumerate(program):
                        if line.startswith(label):
                            pc = i
                            break

        elif opcode == 'JUMP':
            label = tokens[1]
            for i, line in enumerate(program):
                if line.startswith(label):
                    pc = i
                    break

        elif opcode == 'END':
            break

        pc += 1

    return result

print(run(['MOV A 10', 'start:', 'PRINT A', 'SUB A 1', 'IF A > 0 JUMP start', 'END']))