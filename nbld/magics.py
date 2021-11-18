from IPython.core.magic import Magics, cell_magic, magics_class, needs_local_scope
from IPython import get_ipython
from IPython.display import Javascript, display
from pprint import pprint
import pdb

@magics_class
class MyMagics(Magics):

    @needs_local_scope
    @cell_magic
    def context(self, line, cell, local_ns=None):
        # print(type(line), type(cell))
        # pprint(dir(line), dir(cell), dir(local_ns))
        pdb.set_trace()
        print('jd id', dir(Javascript('Jupyter.notebook.get_selected_cell().id')))
        pprint(local_ns)

