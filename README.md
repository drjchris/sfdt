# sfdt - simple and functional data tools

A simple set of tools to help manage datasets. Specifically made for the cross-comm project.

---

# General data handling functions

``` python
    listDates(startdate, enddate)   # yyyy-mm-dd format
    countValues([rawlist])          # returns a list of dicts
    makeAnon(string)                # returns hash value
```

# Community Structure calculation
``` python
    sCS = commStruct([rawlist])           # function for community structure
    
    sCS['core'] # list of users in core
    sCS['mid']  # list of users in middle
    sCS['per']  # list of users in periphery
    sCS['data'] # full table output as json
```