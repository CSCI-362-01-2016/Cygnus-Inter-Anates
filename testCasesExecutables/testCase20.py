import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../project/src"))
import timer

def echoTime():
    global seconds
    seconds = seconds + 1  # update time

def test(inputs):
    testClass = timer.Timer2(1000, echoTime, [], inputs)
    actualResults = testClass.getRepeat()
    return actualResults

if __name__ == '__main__':
    print test(True)
