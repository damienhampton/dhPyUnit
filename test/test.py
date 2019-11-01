class TestCase:
  def __init__(self, name):
    self.name= name
    self.wasSetUp= None
  def setUp(self):
    pass
  def tearDown(self):
    pass
  def run(self):
    self.setUp()
    method= getattr(self, self.name)
    method()
    self.tearDown()

class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)
  def setUp(self):
    self.log= 'setUp '
  def tearDown(self):
    self.log+= 'tearDown '
  def testMethod(self):
    self.log+= 'testMethod '

class TestCaseTest(TestCase):
  def setUp(self):
    self.test= WasRun('testMethod')
  def testTemplateMethod(self):
    self.test.run()
    assert('setUp testMethod tearDown ' == self.test.log)

print(TestCaseTest('testTemplateMethod').run())
