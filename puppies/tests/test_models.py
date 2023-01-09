from django.test import TestCase, Client
from puppies.models import Puppy
from django.urls import reverse
from puppies.serializers import PuppySerializer


client = Client()


class GetAllPuppiesTest(TestCase):

	def setUp(self):

		Puppy.objects.create(

			name='Casper', age=3, breed='Bull Dog', color='Black')
		Puppy.objects.create(
			name='Muffin', age=1, breed='Gradane', color='Brown')

		Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
		Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')


	def test_get_all_puppies(self):


		# puppy_casper = Puppy.objects.get(name='Casper')

		# puppy_muffin = Puppy.objects.get(name='Muffin')

		# self.assertEqual(
		# 	puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
		# self.assertEqual(
		# 	puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")

		# get API response

		response = client.get(reverse('get_post_puppies'))

		puppies = Puppy.objects.all()
		serializer = PuppySerializer(puppies, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
