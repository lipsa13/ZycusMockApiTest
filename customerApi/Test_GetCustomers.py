# Third-party imports...
from unittest.mock import Mock, patch
import unittest
import requests
# Third-party imports...
from nose.tools import assert_list_equal, assert_is_none,assert_true
# local Imports
from customerApi.get_Customers import get_customer_details


class ApiTests(unittest.TestCase):
    @patch('customerApi.get_Customers.requests.get')
    def test_getting_customer_details_when_response_is_ok(self, mock_get):

        customer_details = [{
            'id': 2,
        'first_name': "Janet",
        'last_name': "Weaver",
        'contact': "1234567890"
        }]
      # Configure the mock to return a response with an OK status code.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = customer_details

        # Call the service, which will send a request to the server.
        get_response = get_customer_details()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_list_equal(get_response.json(), customer_details)
        print("The Customer details are Displayed")

    @patch('customerApi.get_Customers.requests.get')
    def test_getting_customer_details_when_response_is_not_ok(self, mock_get):
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_customer_details()

        # If the response contains an error, I should get no customers.
        assert_is_none(response)
        print("Page is not loaded/Error Found!!!!")

    @patch('customerApi.get_Customers.requests.get')
    def test_getting_Customer_details_are_empty(self, mock_get):
        customer_details={}

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = customer_details

        # Call the service, which will send a request to the server.
        response = get_customer_details()

        # If the request is sent successfully, then I expect a response to be returned
        assert_true(response.json,customer_details)
        print("Customer details are Empty")

    @patch('customerApi.get_Customers.requests.get')
    def test_getting_Customer_id_is_not_found(self, mock_get):

            customer_message = {404:'customer not found'}
            # a `json()` method that returns a list of todos.
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = customer_message

            # Call the service, which will send a request to the server.
            response = get_customer_details()

            assert_true(response.get_json,[404] == "customer not found")
            print("These Customer_id is not registered")

if __name__ == "__main__":
    unittest.main()