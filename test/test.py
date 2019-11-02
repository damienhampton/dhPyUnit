class TestCase:
  def __init__(self, name):
    self.name= name
    self.wasSetUp= None
  def setUp(self):
    pass
  def tearDown(self):
    pass
  def run(self):
    result= TestResult()
    result.testStarted()
    self.setUp()
    try:
      method= getattr(self, self.name)
      method()
    except:
      result.testFailed()
    self.tearDown()
    return result

class TestResult:
  def __init__(self):
    self.runCount= 0
    self.errorCount= 0
  def testStarted(self):
    self.runCount+= 1
  def testFailed(self):
    self.errorCount+= 1
  def summary(self):
    return "%d run, %d failed" % (self.runCount, self.errorCount)

class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)
  def setUp(self):
    self.log= 'setUp '
  def tearDown(self):
    self.log+= 'tearDown '
  def testMethod(self):
    self.log+= 'testMethod '
  def testBrokenMethod(self):
    raise Exception

class TestCaseTest(TestCase):
  def setUp(self):
    self.test= WasRun('testMethod')
  def testTemplateMethod(self):
    self.test.run()
    assert('setUp testMethod tearDown ' == self.test.log)
  def testResult(self):
    result= self.test.run()
    assert('1 run, 0 failed' == result.summary())
  def testFailedResult(self):
    test = WasRun('testBrokenMethod')
    result= test.run()
    assert('1 run, 1 failed' == result.summary())
  def testFailedResultFormatting(self):
    result= TestResult()
    result.testStarted()
    result.testFailed()
    assert('1 run, 1 failed' == result.summary())

print(TestCaseTest('testTemplateMethod').run().summary())
print(TestCaseTest('testResult').run().summary())
print(TestCaseTest('testFailedResult').run().summary())
print(TestCaseTest('testFailedResultFormatting').run().summary())
