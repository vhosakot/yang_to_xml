# yang_to_xml
Tool to convert YANG models to XML files

`xmlgen` in this repo converts YANG models to XML files.

#### Supported features:
* XML slicing (chunking an XML file based on a yang model to several logical parts)
* Generate values for parameters - supported types are `string`, `enumeration`, `uint` and `empty`
* Regular expressions
* pyang-generated XSDs

#### Steps to convert YANG models to XML files

```
pyanggen -f xsd myTest-test-myVer1.yang > myTest-test-myVer1.xsd
pyanggen -f xsd myTest-test-myVer2.yang > myTest-test-myVer2.xsd
pyanggen -f xsd ietf-inet-types.yang > ietf-inet-types.xsd

pyxbgen -u myTest-test-myVer1.xsd -m myTest_test_myVer1

xmlgen myTest_test_myVer1.py xml_out
```
