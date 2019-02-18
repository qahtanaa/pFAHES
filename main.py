import sys
import os
import pandas as pd
import patterns

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
            print("Error creating directory!\n")
            sys.exit(1)

    #check input csv
    try:
        T = pd.read_csv(table_name, dtype=str)
    except OSError as e:
        print("Error reading csv!\n")
        sys.exit(1)

    #histogram
    #res = {col:T[col].value_counts() for col in T.columns}
    #print(T['a'].value_counts().get(1))

    if tool_id == '1':
        patterns.find_all_patterns(T)
    elif tool_id == '2':
        print("2")
    else:
        print("3")

if __name__ == "__main__":
    main()
