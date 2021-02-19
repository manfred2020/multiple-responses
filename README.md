[![Generic badge](https://img.shields.io/badge/Status-Under_Construction-gold.svg)](https://github.com/manfred2020/DA_mit_Python)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-limegreen.svg)](https://github.com/manfred2020/DA_mit_Python)
[![Generic badge](https://img.shields.io/badge/Version-0.1.0-lightskyblue.svg)](https://github.com/manfred2020/DA_mit_Python)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Generic badge](https://img.shields.io/badge/©-2021-black.svg)](https://github.com/manfred2020/DA_mit_Python)

# mr - multiple responses
Analysis of multiple responses - Auswertung von Mehrfachantworten


```python
import pandas as pd
from mr import mr

data = pd.read_csv("C:\\YourFolder\\YourFile.csv")

data

mr(data, "nike", "head", "boss", "lacoste")

```
