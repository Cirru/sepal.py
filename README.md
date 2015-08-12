
Cirru Sepal in Python
----

This is an experimental project.

### Usage

```
pip install cirru_sepal
```

```python
import ast
import codegen
import cirru_parser
import cirru_sepal

tree = cirru_parser.pare("code", "filename")
codegen.to_source(cirru_sepal.transform(tree))
```

### AST

```python
import ast
import codegen

ast.parse('print(1 + 2)') # return AST
ast.dump(ast.parse('print(1 + 2)')) # return readable AST
codegen.to_source.dump(ast.parse('print(1 + 2)')) # generate code
```

### License

MIT
