from InitModules import Configuration
from InitModules import Architecture
from InitModules import Instructions
from Output import Output

import pprint
class Pipeline():
    def __init__(self, instruction_path, register_path, config_path, memory_path):
        pp = pprint.PrettyPrinter(indent=4)
        self.configuration = self.getconfig(config_path)
        self.arch = self.getArch(memory_path, register_path, self.configuration)
        self.instructions = self.getInstructions(instruction_path)
        print(self.instructions)
        self.labels = self.getLabels(instruction_path)
        self.instructionMapping = self.defineInstructions()
        self.OUT = Output()

    def getconfig(self, path):
        conf = Configuration.Config(path)
        cfg = conf.getconfig()
        return cfg

    def getArch(self, memory_path, register_path, config):
        arch = Architecture.Arch(memory_path, register_path, config)
        return arch

    def getInstructions(self, instruction_path):
        I = Instructions.Instruction(instruction_path)
        return I.getInstructions()

    def getLabels(self, instruction_path):
        L = Instructions.Instruction(instruction_path)
        return L.getLabels()

    def defineInstructions(self):
        I = Instructions.Instruction('')
        return I.getInstructionMapping()




