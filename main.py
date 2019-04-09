#
#  Zezhou Huang
#  zhuang333@wisc.edu
#
import sys
import os
import pandas as pd

class sus_disguised:
    def __init__(self, attr_name, value, score, frequency, tool_name):
        self.attr_name = attr_name
        self.value = str(value)
        self.score = score
        self.frequency = frequency
        self.tool_name = tool_name
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.attr_name == other.attr_name and self.value == other.value

import patterns
import DV_Detector
import RandDMVD
import OD

def main():
    # check arguments
    # for arg in sys.argv[1:]:
    if(len(sys.argv) != 4):
        print("Wrong number of arguments .. entered (",len(sys.argv),")")
        print(sys.argv, file=sys.stderr)
        print("Usage (",sys.argv[0],"): <data file name>",
              " <output directory name> <Tool ID>")
        sys.exit(1)

    table_name = sys.argv[1];
    out_directory = sys.argv[2];
    tool_id = sys.argv[3];

    # check output directory
    if (not os.path.isdir(out_directory)):
        try:
            os.makedirs(out_directory)
        except OSError as e:
            print("Error creating directory!")
            sys.exit(1)

    #check input csv
    try:
        T = pd.read_csv(table_name, dtype=str, keep_default_na=False)
    except OSError as e:
        print("Error reading csv!")
        sys.exit(1)

    #histogram
    #res = {col:T[col].value_counts() for col in T.columns}
    #print(T['a'].value_counts().get(1))
    sus_dis_values = []

    if tool_id == '1':
        sus_dis_values = patterns.find_all_patterns(T, sus_dis_values)
        sus_dis_values = DV_Detector.check_non_conforming_patterns(T, sus_dis_values)
    elif tool_id == '2':
        sus_dis_values = RandDMVD.find_disguised_values(T, sus_dis_values)
    elif tool_id == '3':
        sus_dis_values = OD.detect_outliers(T, sus_dis_values)
    elif tool_id == '4':
        sus_dis_values = patterns.find_all_patterns(T, sus_dis_values)
        sus_dis_values = DV_Detector.check_non_conforming_patterns(T, sus_dis_values)
        sus_dis_values = RandDMVD.find_disguised_values(T, sus_dis_values)
        sus_dis_values = OD.detect_outliers(T, sus_dis_values)
    else:
        print("Unkown option ..",tool_id)
        sys.exit(1)


    Print_output_data(out_directory, table_name, sus_dis_values)

def Print_output_data(out_directory, table_name, sus_dis_values):

    if out_directory[-1] != '/':
        out_directory = out_directory + '/'
    table_name.replace('\\', '/')
    tabn = table_name.split('/')[-1]
    f = open(out_directory + "DMV_" + tabn, "w")
    if len(sus_dis_values) < 1:
        print("nothing")
        return
    f.write("Table Name,Attribute Name,DMV,Frequency,Detecting Tool\n")
    for sus_dis in sus_dis_values:
        f.write(check_d_quotation(tabn[0:len(tabn)-4])+","+check_d_quotation(sus_dis.attr_name)+","+check_d_quotation(sus_dis.value)+","+str(sus_dis.frequency)+","+sus_dis.tool_name+"\n")


def check_d_quotation(str):
    if "," in str:
        return "\""+str+"\""
    return str

if __name__ == "__main__":
    main()
