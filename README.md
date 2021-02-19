# mr - multiple responses
Analysis of multiple responses - Auswertung von Mehrfachantworten


```python
import pandas as pd
from mr import mr

data = pd.read_csv("C:\\YourFolder\\YourFile.csv")

data

mr(data, "nike", "head", "boss", "lacoste")

```
