class TestCase:
  def __init__(self, name):
    self.name= name
    self.wasSetUp= None
  def setUp(self):
    pass
  def run(self):
    self.setUp()
    method= getattr(self, self.name)
    method()

class WasRun(TestCase):
  def __init__(self, name):
    self.wasRun= None
    TestCase.__init__(self, name)
  def setUp(self):
    self.wasSetUp= 1
  def testMethod(self):
    self.wasRun= 1

class TestCaseTest(TestCase):
  def setUp(self):
    self.test= WasRun('testMethod')
  def testRunning(self):
    assert(not self.test.wasRun)
    self.test.run()
    assert(self.test.wasRun)
  def testSetUp(self):
    self.test.run()
    assert(self.test.wasSetUp)

print(TestCaseTest('testRunning').run())
print(TestCaseTest('testSetUp').run())
