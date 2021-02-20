[![Generic badge](https://img.shields.io/badge/Status-Under_Construction-gold.svg)](https://github.com/manfred2020/multiple-responses)
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-limegreen.svg)](https://github.com/manfred2020/multiple-responses)
[![Generic badge](https://img.shields.io/badge/Version-0.1.0-lightskyblue.svg)](https://github.com/manfred2020/multiple-responses)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Generic badge](https://img.shields.io/badge/©-2021-black.svg)](https://github.com/manfred2020/multiple-responses)

# mr - multiple responses
Analysis of multiple responses - Auswertung von Mehrfachantworten


```python
import pandas as pd
from mr import mr

data = pd.read_csv("C:\\YourFolder\\YourFile.csv")

data

mr(data, "nike", "head", "boss", "lacoste")

```

##### Ausgabe in Jupyter Notebook

![Screenshot Jupyter Notebook Output (Tabelle und Grafik](jupyter.png)

##### Ausgabe in Spyder IDE

![Screenshot Spyder IDE Output (Tabelle)](spyder.png)

<br>
<br>

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/manfred2020/multiple-responses">mr - multiple responses</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/manfred2020">Manfred Hammerl</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0</a></p>
