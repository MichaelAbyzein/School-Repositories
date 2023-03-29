"""
from hitungan.mtk import phi
"""

from . import mtk

gravity = 9.8
def pillar_presure(m, x, y):
    return (m*gravity)/(x*y)
    
def pipe_presure(m, r):
    return (m*gravity)/(mtk.phi*r**2)