from collections import defaultdict
import re
class Instruction:
    def __init__(self, path):
        self.path = path
    def getInstructions(self):
        instructions = defaultdict()
        with open(self.path) as instFile:
            for num, line in enumerate(instFile):
                line = line.strip().lower()
                if ':' in line:
                    line = line.split(':')[1].strip()
                instBreakdown = line.split(' ', 1)
                instType = instBreakdown[0].strip()
                if len(instBreakdown) == 1:
                    operands = ''
                elif instType in ['beq','bne','j']:
                    operands = list()
                    opT = instBreakdown[1].strip().split(',')

                    for t in opT:
                        operands.append(t.strip())
                else:
                    operands = list()
                    opT = instBreakdown[1].strip().split(',')
                    self.getOperands(operands, opT)

                instructions[str(num)] = defaultdict(None, {"opcode": instType, "operands": operands})
        return instructions

    def getLabels(self):
        labels = defaultdict()
        with open(self.path) as instFile:
            for num, line in enumerate(instFile):
                line = line.strip().lower()
                if ':' in line:
                    label = line.split(':')[0].strip()
                    labels[label] = str(num)
        return labels


    def getInstructionMapping(self):
        instructionMap = defaultdict()
        no_ex = ['hlt','j','beq','bne']
        int_unit = ['dadd','daddi','dsub','dsubi','and','andi','or','ori']
        mem = ['lw','sw','l.d','s.d']
        for i in no_ex:
            instructionMap[i] = 'NO_EX'
        for j in int_unit:
            instructionMap[j] = 'INT'
        for k in mem:
            instructionMap[k] = 'MEM'
        instructionMap['add.d'] = 'FP_ADD'
        instructionMap['sub.d'] = 'FP_ADD'
        instructionMap['mul.d'] = 'FP_MUL'
        instructionMap['div.d'] = 'FP_DIV'

        return instructionMap

    def getOperands(self, operands, opT):
        for t in opT:
            operand = t.strip()
            if re.search("[r,f]\d+", operand):
                operands.append(re.search("[r,f]\d+", operand).group(0).strip('('))
            if re.search('^\d*\(', operand):
                operands.append(re.search("[r,f]\d+", operand).group(0).strip('('))
            if re.search('^\d*$', operand):
                operands.append(re.search('^\d*$', operand).group(0).strip('('))

