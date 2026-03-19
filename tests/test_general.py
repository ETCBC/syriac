import os
import re
import pytest
import collections

from tf.fabric import Fabric

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TF_FOLDER = 'tf'
latest_data_folder = sorted(os.listdir(os.path.join(ROOT_DIR, TF_FOLDER)))[-1]

TF = Fabric(locations=os.path.join(ROOT_DIR, TF_FOLDER, latest_data_folder))
api = TF.load('''
    otype g_cons g_cons_utf8 lex g_pfm g_pfx g_emf g_vbs g_lex g_vbe g_nme sp vt ps nu gn trailer
''')
api.loadLog()
api.makeAvailableIn(globals())

F, L = api.F, api.L


def test_reconstruct_g_cons_from_morphemes():
    assert all([F.g_pfm.v(w) + F.g_pfx.v(w) + F.g_vbs.v(w) + F.g_lex.v(w) + \
                F.g_nme.v(w) + F.g_vbe.v(w) + F.g_emf.v(w) == F.g_cons.v(w) for w in F.otype.s('word')])
