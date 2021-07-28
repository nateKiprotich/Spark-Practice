# Spark-Practice

This repo is personal practice on Spark and API.
Data is fetched from Api and processed using spark.

End result is export file.


## Packages used
Spark
```bash
pip install pyspark
```
Request
```bash
pip install requests
```
Pandas
```bash
pip install pandas
```

## TO-DO List
1. Exception Handling - Check status of API call before trying to fetch data
2. Allow Selection of all story Categories
3. Performance Improvement - Measure time it takes to execute and try to improve
4. Add Operation Status - When adding data to the dataframe, status of the progress should be shown to the user.
Currently the terminal seems frozen.
5. Allow data to be saved. The program should prompt with available output formats



Miscellaneousl

First timed run:
    it took 403.7154493331909 seconds to fetch 500 records

Process flow:
    API -> Pandas -> Spark

Solution:
    Eliminate use of pandas data frame and instead have the flow below:
        API -> Spark
