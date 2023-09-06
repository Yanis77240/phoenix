# comparison-file-check.py

import pandas as pd
import sys
import json


# If the argument 0 is given, no schema checking is performed
if sys.argv[1] != "0":
    # define file
    comparison_file = sys.argv[1]
    # Check if file is a valid json
    try:
        # Read the JSON data as a dictionary
        with open(f'{comparison_file}', 'r') as json_file:
            json_data = json.load(json_file)
        print("json file is readable")
    except:
        print("file does not exist or is not of json format")
        sys.exit(1)

    # Check if the columns of the loaded dataframe matches the one used later on
    # The type of the columns can vary it will still work for the comparison.
    try :
        records = []
        # Loop through each element of the json file
        for test_group, values in json_data.items():
            # For each element in the failed_test list
            for failed_test in values['failed_list']:
                # Get the class Test_group and define it as key for value test_group which is the main element of the schema
                record = {'test_group': test_group}
                # Get the attribute values
                # Update individual test_stats
                record['succeeded'] = values['test_stats']['succeeded']
                record['failed'] = values['test_stats']['failed']
                record['skipped'] = values['test_stats']['skipped']
                record['pending'] = values['test_stats']['pending']
                record['aborted'] = values['test_stats']['aborted']
                # Get the list of failed tests
                record['failed_list'] = failed_test
                # Append all these elements to the list records
                records.append(record)

        # Define the dataframe and try to read it
        df = pd.DataFrame(records)
        print("Compatible schema")
    except:
        print("Wrong schema")
        sys.exit(1)
    
else:
    print("no comparison needed")
    