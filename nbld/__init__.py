import typing
import pdb
from IPython import get_ipython
from IPython.core.magic import register_cell_magic, needs_local_scope
from nbld.magics import MyMagics
# from nbld import types

# def context(context: types.context):
#     """
#     Set context until the next time context is called
#     """
#     print('context!', context)

# def type(type: types.type):
#     """
#     set @type
#     """

# def attr(attr: types.attr):
#     """
#     set attribute-value pairs
#     """

# def attrs(attrs:types.attrs):
#     """
#     set multiple attrs
#     """

# def cell(
#         context:types.context, 
#         type:types.type, 
#         attrs:types.attrs):
#     """
#     Set all properties for cell at once
#     """
#     pass


import sys

def pre_save_hook(self, model, path, contents_manager, *args, **kwargs):
    print('model',model, '\npath', path, '\ncontents', contents_manager, *args, **kwargs)
    sys.stdout.flush()

# def enable():
#     # i guess you don't import anything to get the config????
#     c = get_config() # noqa
#     c.NotebookApp.contents_manager_class.pre_save_hook = pre_save_hook

def _jupyter_server_extension_paths():
    return [
        {"module": 'nbld'}
    ]


def prerun(info):
    print(info)

def load_jupyter_server_extension(nbapp):
    nbapp.contents_manager_class.pre_save_hook = pre_save_hook
    # pdb.set_trace()
    print(nbapp)
    nbapp.log.info('loaded nbld')

def load_ipython_extension(ipython):
    print('magics ipython', ipython)
    sys.stdout.flush()
    ipython.register_magics(MyMagics)
    ipython.events.register('pre_run_cell', prerun)



