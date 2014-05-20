mtx2JSON
========

Convert MSM adjacency matrix into a JSON-formatted graph


How to use
-----------

If you want to simply turn your sparse adjacency matrix into a JSON graph:

```
python mtx2JSON -m graph -t [FILE_PATH_TO_TRANSITION_MATRIX] -c [CUT_OFF_VALUE]
```

If you want to retrieve the transition pathways as a JSON graph:

```
python mtx2JSON -m pathway -t [FILE_PATH_TO_TRANSITION_MATRIX] -n [NUM_PATHS] -s [FILE_PATH_TO_SOURCES] -e [FILE_PATH_TO_SINKS]
```

where input files for ``-s`` and ``-e`` should be a text file with a single column of selected integers (state numbers).
