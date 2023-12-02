import logger
import string
import random 
import traceback
from parser import keyMiner, checkIfValidHelm
from scanner import isValidUserName, isValidPasswordName, isValidKey
import logging

def fuzzValues():
    logObj = logger.giveMeLoggingObject()
    logObj.info("Generating fuzz values...")
    randomValue = random.randint(-100, 100)
    randomLetters = ''.join(random.choices(string.ascii_letters, k = 10))
    return randomValue, randomLetters



def Fuzzer():
    with open("fuzz_report.txt", "w") as report:
        for i in range(10): 
            fuzzedInt, fuzzedStr = fuzzValues()
            logObj = logger.giveMeLoggingObject()
            logObj.info("Checking for valid user name...") 
            try:
                isValidUserName(fuzzedStr)
                report.write(f"Iterations {i}:isValidUserName Success\n")
            except Exception as e:
               Error = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:isValidUserName Failed - {''.join(Error)}\n")
            try:
                isValidUserName(fuzzedInt)
                report.write(f"Iterations {i}:isValidUserName Success\n")
            except Exception as e:
               Error = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:isValidUserName Failed - {''.join(Error)}\n")
            try:
                isValidUserName(Null)
               
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:isValidUserName Success\n")
            except Exception as e:
                Error = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}:isValidUserName Failed - {''.join(Error)}\n")
                
            else:
                report.write("fuzzing isValidUserName done!\n")
            
            logObj.info("Checking for valid password name...")
            try:
               ## isValidUserName(fuzzedStr)
                isValidPasswordName(fuzzedStr)
                report.write(f"Iterations {i}:isValidPasswordName Success\n")
            except Exception as e:
                ## Error = traceback.format_exception(etype = type(e), value = e, tb =e._traceback_)
               Error1 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:isValidPasswordName Failed- {''.join(Error1)}\n")
            try:
                isValidPasswordName(fuzzedInt)
                report.write(f"Iterations {i}:isValidPasswordName Success\n")
            except Exception as e:
                ## Error = traceback.format_exception(etype = type(e), value = e, tb =e._traceback_)
               Error1 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:isValidPasswordName Failed- {''.join(Error1)}\n")
            try:
                isValidPasswordName(NULL)

               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:isValidPasswordName Success\n")
            except Exception as e:
                ## Error = traceback.format_exception(etype = type(e), value = e, tb =e._traceback_)
                Error1 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}:isValidPasswordName Failed- {''.join(Error1)}\n")
                
            else:
                report.write("fuzzing for isValidPasswordName done!\n")

            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
                checkIfValidHelm(fuzzedStr)
                report.write(f"Iterations {i}:checkIfValidHelm Success\n")
            except Exception as e:
               Error2 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:checkIfValidHelm Failed- {''.join(Error2)}\n")
            try:
                checkIfValidHelm(fuzzedInt)
                report.write(f"Iterations {i}:checkIfValidHelm Success\n")
            except Exception as e:
               Error2 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}:checkIfValidHelm Failed- {''.join(Error2)}\n")
            try:
                checkIfValidHelm(NULL)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:checkIfValidHelm Success\n")
            except Exception as e:
                Error2 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}:checkIfValidHelm Failed- {''.join(Error2)}\n")
                
            else:
                logObj.info("Done with Checking ValidHelm...")
                report.write("fuzzing for checkIfValidHelm done!\n")
            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
           
                isValidKey(fuzzedStr)
                report.write(f"Iterations {i}: isValidKey Success\n")
            except Exception as e:
               Error3 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}: isValidKey Failed- {''.join(Error3)}\n")
            try:
                isValidKey(fuzzedInt)
                report.write(f"Iterations {i}: isValidKey Success\n")
            except Exception as e:
                Error3 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}: isValidKey Failed- {''.join(Error3)}\n")
            try:
                isValidKey(NULL)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}: isValidKey Success\n")
            except Exception as e:
                Error3 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}: isValidKey Failed- {''.join(Error3)}\n")
                
            else:
                report.write("fuzzing for isvalidKey done!\n")
            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
                keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}: KeyMiner passed\n")
            except Exception as e:
               Error4 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}: KeyMiner Failed- {''.join(Error4)}\n")
            try:
                keyMiner(fuzzedINt, fuzzedINt)
                report.write(f"Iterations {i}: KeyMiner passed\n")
            except Exception as e:
               Error4 = traceback.format_exception(type(e),e,e._traceback_)
               report.write(f"Iteration {i}: KeyMiner Failed- {''.join(Error4)}\n")
            try:
                keyMiner(fuzzValues, fuzzValues)
                report.write(f"Iterations {i}: KeyMiner passed\n")
            except Exception as e:
                Error4 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}: KeyMiner Failed- {''.join(Error4)}\n")
            try:
                logObj.info("Done with keyMiner, reporting back...") 
                keyMiner(NULL, NULL)
                report.write(f"Iterations {i}: KeyMiner passed\n")
            except Exception as e:
                Error4 = traceback.format_exception(type(e),e,e._traceback_)
                report.write(f"Iteration {i}: KeyMiner Failed- {''.join(Error4)}\n")
                break
            else:
                logObj.info("Done with keyMiner, reporting back...") 
                report.write("fuzzing for KeyMiner done!\n")
            logObj.info("End of Fuzzing method...") 
if __name__ == '__main__':
    logObj = logger.giveMeLoggingObject()
    logObj.info("Running Fuzzer method...") 
    Fuzzer()
def giveMeLoggingObject():
    format_str = '%(asctime)s %(message)s'
    file_name = 'SIMPLE-LOGGER.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj =logging.getLogger('simple-logger')
    return loggerObj
