from django.test import TestCase
from django.test import Client
from django.http.request import HttpRequest

from model_mommy import mommy
from utils.stripe_utils import StripeUtils
import stripe
from django.conf import settings
from datacenterlight.models import StripePlan


class BaseTestCase(TestCase):
    """
    Base class to initialize the test cases
    """

    def setUp(self):
        # Password
        self.dummy_password = 'test_password'

        # Users
        self.customer, self.another_customer = mommy.make('membership.CustomUser',
                                                          _quantity=2)
        self.customer.set_password(self.dummy_password)
        self.customer.save()
        self.another_customer.set_password(self.dummy_password)
        self.another_customer.save()

        # Stripe mocked data
        self.stripe_mocked_customer = self.customer_stripe_mocked_data()

        #  Clients
        self.customer_client = self.get_client(self.customer)
        self.another_customer_client = self.get_client(self.another_customer)

        # Request Object
        self.request = HttpRequest()
        self.request.META['SERVER_NAME'] = 'ungleich.com'
        self.request.META['SERVER_PORT'] = '80'

    def get_client(self, user):
        """
        Authenticate a user and return the client
        """
        client = Client()
        client.login(email=user.email, password=self.dummy_password)
        return client

    def customer_stripe_mocked_data(self):
        return {
            "id": "cus_8R1y9UWaIIjZqr",
            "object": "customer",
            "currency": "usd",
            "default_source": "card_18A9up2eZvKYlo2Cq2RJMGeF",
            "email": "vmedixtodd+1@gmail.com",
            "livemode": False,
            "metadata": {
            },
            "shipping": None,
            "sources": {
                "object": "list",
                "data": [{
                    "id": "card_18A9up2eZvKYlo2Cq2RJMGeF",
                    "object": "card",
                    "brand": "Visa",
                    "country": "US",
                    "customer": "cus_8R1y9UWaIIjZqr",
                    "cvc_check": "pass",
                    "dynamic_last4": None,
                    "exp_month": 12,
                    "exp_year": 2018,
                    "funding": "credit",
                    "last4": "4242",
                }]
            }
        }

    def setup_view(self, view, *args, **kwargs):
        """Mimic as_view() returned callable, but returns view instance.

        args and kwargs are the same you would pass to ``reverse()``

        """
        view.request = self.request
        view.args = args
        view.kwargs = kwargs
        view.config = None
        return view


class TestStripeCustomerDescription(TestCase):
    """
    A class to test setting the description field of the stripe customer
    https://stripe.com/docs/api#metadata
    """

    def setUp(self):
        self.dummy_password = 'test_password'
        self.dummy_email = 'test@ungleich.ch'
        self.customer = mommy.make('membership.CustomUser')
        self.customer.set_password(self.dummy_password)
        self.customer.email = self.dummy_email
        self.customer.save()
        stripe.api_key = settings.STRIPE_API_PRIVATE_KEY

    def test_creating_stripe_customer(self):
        test_name = "Monty Python"
        token = stripe.Token.create(
            card={
                "number": '4111111111111111',
                "exp_month": 12,
                "exp_year": 2022,
                "cvc": '123'
            },
        )
        stripe_utils = StripeUtils()
        stripe_data = stripe_utils.create_customer(token.id, self.customer.email, test_name)
        self.assertEqual(stripe_data.get('error'), None)
        customer_data = stripe_data.get('response_object')
        self.assertEqual(customer_data.description, test_name)


class StripePlanTestCase(TestStripeCustomerDescription):
    """
    A class to test Stripe plans
    """

    def test_create_plan(self):
        stripe_utils = StripeUtils()
        plan_id_string = stripe_utils.get_stripe_plan_id_string(2, 20, 100, 1)
        self.assertEqual(plan_id_string, 'dcl-v1-cpu-2-ram-20gb-ssd-100gb')
        stripe_plan = stripe_utils.get_or_create_plan(2000, "test plan 1", stripe_plan_id='test-plan-1')
        self.assertEqual(stripe_plan.get('error'), None)
        self.assertIsInstance(stripe_plan.get('response_object'), StripePlan)
