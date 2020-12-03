import numpy as np
import pandas as pd

index = [ "color", "color_name", "hex", "R", "G", "B" ]
csv = pd.read_csv( 'colors.csv', names=index, header=None )

def recognize_color( r, g, b ):
    minimum = 1000
    for i in range( len( csv ) ):
        d = abs( r - int( csv.loc[ i, "R" ] ) ) + abs( g - int( csv.loc[ i,"G" ] ) ) + abs( b - int( csv.loc[ i,"B" ] ) )
        if( d <= minimum ):
            minimum = d
            color_name = csv.loc[ i,"color_name" ]
    return color_name
