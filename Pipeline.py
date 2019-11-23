from InitModules import Configuration
class Pipeline():
    def __init__(self, instruction_path, register_path, config_path, memory_path):
        self.configuration = self.getconfig(config_path)

    def getconfig(self, path):
        conf = Configuration.Config(path)
        cfg = conf.getconfig()
        return cfg