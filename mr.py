# -*- coding: utf-8 -*-
"""
Functions:
    mr - multiple response
    cv - count values
    
Author:
    Manfred Hammerl

https://github.com/manfred2020

"""

__version__ = "0.2.0, from 22nd February 2021"

def mr(df, *col, count = 1, save = False, decimal = ",", style = True):
    
    """
    NAME:
        mr - multiple response
    
    DESCRIPTION:
        Eine kleine Funktion zur Auswertung von Mehrfachantworten, welche
        ein Balkendiagramm ausgibt sowie eine Tabelle (Dataframe) mit den 
        Ergebnissen der Auswertung
        
    Parameters:
        df : Dataframe
        col : string
              Variablen, die in die Auswertung einbezogen werden sollen
        count : int, float
                Wert, der gezählt/ausgewertet werden soll
        save : bool
               True: Outputtabelle wird in Zwischenablage kopiert
               False: Outputtabelle wird nicht in Zwischenablage kopiert
               (default)
        decimal : string
                  Nur in Verbindung mit 'save = True' relevant!
                  Dezimaltrennzeichen, bspw. "," (default) im deutschsprachigen Raum,
                  oder "." im englischsprachigen Raum
        style : bool
              True: Wird die Funktion in einem Juypter Notebook aufgerufen, so
                    kann die "gestylte" Outputtabelle (Dataframe) angezeigt werden (default)
              False: Wird die Funktion nicht in einem Jupyter Notebook aufgerufen,
                     sondern bspw. in Sypder, so wird damit eine "normale" Outputtabelle
                     (Dataframe) angezeigt.
    
    Returns:
        Dataframe
    
    """
    
    import pandas as pd
    
    columns = [] # leere Liste erstellen
    
    for col in col:
        columns.append(col) # Alle eingegebenen Variablen in Liste einfügen
    
    mrcount = (df[columns] == count).sum(axis = 0).sort_values(ascending = True)
    # die erste Basisauswertung; sie bestimmt auch die Anzeigereihenfolge
    mrsum = mrcount.sum(axis = 0)
    # Summe der insgesamt abgegebenen Antworten ermitteln
    length = len(df.index) # Anzahl der Zeilen im Dataframe ermitteln
    width = len(columns) # Anzahl der ausgewählten Variablen ermitteln
    cells = (length*width) # Anzahl der Zellen im Dataframe ermitteln
        
    finalset = pd.DataFrame({"Anz Nennungen" : mrcount,
                             "% Befragte" : ((mrcount/length)*100).round(2),
                             "% mögl Nennungen" : ((mrcount/cells)*100).round(2),
                             "% tatsächl Nennungen" : ((mrcount/(mrsum))*100).round(2)}
                            ).fillna(0)
    # fillna() wegen möglicher Division durch 0
        
    styleset = finalset.style.format({"Anz Nennungen" : "{:.0f}",
                                      '% Befragte' : '{:.1f}%',
                                      "% mögl Nennungen" : "{:.1f}%",
                                      "% tatsächl Nennungen" : "{:.1f}%"})
    
    if save:
        finalset.to_clipboard(decimal = decimal)
        # ',' als Dezimaltrennzeichen im deutschsprachigen Raum
        print("\nErgebnistabelle wurde in die Zwischenablage zur weiteren Verwendung kopiert\n")
        
    if mrsum > 0:
        import matplotlib.pyplot as plt    
        from matplotlib.ticker import FormatStrFormatter
        ax = finalset[['% mögl Nennungen', '% tatsächl Nennungen',
                       '% Befragte']].plot.barh(figsize=(8.5,4.5))    
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.f%%'))
        plt.legend(loc='lower right')
    
    if style == True:
        from IPython.display import display
        return display(styleset)
    else:
        return finalset


def cv(df, *col, count = 1, var = "Counted_Values"):
    
    """
    NAME:
        cv - count values
    
    DESCRIPTION:
        Eine kleine Funktion zur Zählung von Werten in einer oder mehreren Variablen
        und Speicherung des Zähl-Ergebnisses in einer neuen Variable
        
    Parameters:
        df : Dataframe
        col : string
              Variablen, die in die Zählung einbezogen werden sollen
        count : int, float
                Wert, der gezählt werden soll
        var : Name der neu zu erstellenden Variable, in welcher das Zähl-Ergebnis
              gespeichert werden soll
    
    Returns:
        Anzeige der neue erstellten Variable
        
    """
    
    columns = [] # Leere Liste erstellen
    
    for col in col:
        columns.append(col) # Alle eingegebenen Variablen in Liste einfügen
    
    df[var] = (df[columns] == count).sum(axis = 1)
    
    if var in df.columns:
        print("\nWerte wurden gezählt und in neuer Variable gespeichert")
        print("\nMinimum: {}, Maximum: {}, Durchschnitt: {}\n".format(df[var].min(),
                                                                df[var].max(),
                                                                round(df[var].mean(), 2)
                                                                ))
    
    return df[var]

   