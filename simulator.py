from Pipeline import Pipeline
import sys

if __name__ == '__main__':
    config_path = sys.argv[1]
    data_path = sys.argv[2]
    reg_path = sys.argv[3]
    inst_path = sys.argv[4]
    pipeline = Pipeline(inst_path,reg_path,config_path,data_path)
