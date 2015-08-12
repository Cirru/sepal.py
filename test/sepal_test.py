
from nose.tools import assert_equals
import cirru_parser
import codegen
import ast
from cirru_sepal import transform

def test_transform():
  demo = 'examples/demo.cirru'
  demoFile = open(demo, 'r')
  demoSource = demoFile.read()
  demoFile.close()

  tree = transform(cirru_parser.pare(demoSource, ""))
  print(tree)
  print(ast.dump(tree))
  print(codegen.to_source(tree))

  tree = cirru_parser.pare(demoSource, demo)

  assert_equals(tree, [])
