import unittest
from UnitTest.Package1.TC_LoginTest import Logintest
from UnitTest.Package1.TC_SignupTest import SignupTest

from UnitTest.Package2.TC_PaymentReturnsTest import PaymentReturnsTest
from UnitTest.Package2.TC_PaymentTest import PaymentTest

"""
Get all test method from Logintest, SignupTest, PaymentReturnsTest
and PaymentTest
"""

tc1 = unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

"""
How to Create test suites
"""
# Sanity Test Suite
# sanity_test_suite = unittest.TestSuite([tc1, tc2])
# unittest.TextTestRunner().run(sanity_test_suite)

# Functional Test Suite
# functional_test_suite = unittest.TestSuite([tc3, tc4])
# unittest.TextTestRunner().run(functional_test_suite)

# Master Test Suite
master_test_suite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(master_test_suite)
