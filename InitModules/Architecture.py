import queue
from collections import defaultdict
class Arch:
    def __init__(self, memory_path, register_path, configuration):
        self.memory_path = memory_path
        self.register_path = register_path
        self.configuration = configuration
        self.clock = 0
        self.exComplete = False
        self.halt = False
        self.pipelinePaths = self.get_pipeline_paths()
        self.refinePipelinePaths()
        self.initRegister(register_path)
        self.initMemory(memory_path)
        self.dataBusUsed = [False]
        self.Icache = self.initICache()
        self.Dcache = self.initDCache()
        self.IcacheHit = 0
        self.IcacheMiss = 0
        self.branchTaken = True
        self.DcacheHit = 0
        self.DcacheMiss = 0



    def get_pipeline_paths(self):
        paths = defaultdict()
        fp_seq = []
        fp_seq.append('IF')
        fp_seq.append('ID')
        fp_seq.append('INT_EX')
        fp_seq.append('MEM')
        fp_seq.append('FP_ADD')
        fp_seq.append('FP_DIV')
        fp_seq.append('FP_MUL')
        fp_seq.append('WB')
        paths['FP_SEQUENCE'] = fp_seq

        int_seq = []
        int_seq.append('INT_EX')
        int_seq.append('MEM')
        paths['INT_SEQUENCE'] = int_seq

        cycle_times = defaultdict()
        cycle_times['IF'] = self.configuration["i-cache"][0]
        cycle_times['ID'] = 1
        cycle_times['INT_EX'] = 1
        cycle_times['MEM'] = self.configuration["main memory"][0]
        cycle_times['FP_ADD'] = self.configuration["fp adder"][0]
        cycle_times['FP_MULT'] = self.configuration["fp multiplier"][0]
        cycle_times['FP DIV'] = self.configuration["fp divider"][0]
        cycle_times['WB'] = 1
        paths['CYCLE_TIMES'] = cycle_times

        paths['IF'] = queue.Queue(maxsize=1)
        paths['ID'] = queue.Queue(maxsize=1)
        paths['INT_EX'] = queue.Queue(maxsize=1)
        paths['MEM'] = queue.Queue(maxsize=1)
        paths['FP_ADD'] = queue.Queue(maxsize=1)
        paths['FP_MULT'] = queue.Queue(maxsize=1)
        paths['FP_DIV'] = queue.Queue(maxsize=1)
        paths['WB'] = queue.Queue(maxsize=1)

        return paths

    def refinePipelinePaths(self):
        if self.configuration['fp divider'][1] == 'yes':
            self.pipelinePaths["FP_DIV"].maxsize = self.configuration['fp divider'][0]
        if self.configuration['fp multiplier'][1] == 'yes':
            self.pipelinePaths["FP_MULT"].maxsize = self.configuration['fp multiplier'][0]
        if self.configuration['fp divider'][1] == 'yes':
            self.pipelinePaths["FP_ADD"].maxsize = self.configuration['fp adder'][0]

    def initRegister(self, register_path):
        self.reg_status = defaultdict()
        self.registers = defaultdict()
        for i in range(32):
            self.reg_status['R' + str(i)] = {'Read':0, 'Write':0}
            self.reg_status['F' + str(i)] = {'Read':0, 'Write':0}
        with open(register_path) as reg_file:
            for num, line in enumerate(reg_file):
                self.registers["R" + str(num)] = int(line, 2)

    def initMemory(self, memory_path):
        self.memory = defaultdict()
        with open(memory_path) as memfile:
            for num, line in enumerate(memfile):
                self.memory[str(num)] = int(line, 2)

    def initICache(self):
        l = list()
        for _ in range(4):
            l.append([])
        return l

    def initDCache(self):
        l = list()
        for _ in range(2):
            l.append([])
        return l
