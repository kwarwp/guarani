
{'date': 'Mon Jun 04 2018 14:52:17.807 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  INVENTARIO.inicia()
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Jun 04 2018 14:54:14.852 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  def sala()
             ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jun 04 2018 14:54:56.771 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 29
    sala()    
  module <module> line 13
    INVENTARIO.inicia()
NameError: name 'INVENTARIO' is not defined
'''},