import re
class Config:
    def __init__(self, path):
        self.path = path

    def getconfig(self):
        conf = {}
        with open(self.path) as conf_file:
            for line in conf_file:
                conf[line.split(':')[0].lower().strip()] = line.split(":")[1].strip().split(",")
        # for every config type and config values
        for k,v in conf.items():
            # Validate every configuration
            print(k,v)
            if self.isEmpty(k,v):
                raise Exception('Error in Config file: \nIllegal configuration entered - '+ k)
            elif int(v[0]) < 0:
                raise Exception('Error in Config file: \nNegative number of cycles not allowed - '+ k)
        conf = self.clean(conf)
        return conf

    def isEmpty(self, k, v):
        if 'fp' in k:
            return v is None or len(v) <= 1 or v[0] == '' or v[1].strip() not in ['yes', 'no']
        return v is None or len(v) < 1 or v[0] == ''

    def clean(self, conf):
        for k,v in conf.items():
            if len(v) > 1:
                conf[k] = [v[0].strip(), v[1].strip()]
            else:
                conf[k] = [v[0].strip()]
        return conf