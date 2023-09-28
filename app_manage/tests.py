from django.test import SimpleTestCase  # don't need database
from django.test import TestCase
from django.urls import reverse
from app_data_off.models import Category, Product, UserProduct  # new
from django.contrib.auth import get_user_model


# Create your tests here.


class BasePageTestCase(SimpleTestCase):  # done

    # ok test the base page return a 200 successful http request (a given web page actually exits)
    def test_base_status_name(self):
        response=self.client.get('/base/')
        self.assertEqual(response.status_code, 200)

    # ok testing url return a 200 successful http request
    def test_base_url_name(self):
        response=self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)


class TermesPageTestCase(SimpleTestCase):  # done

    # ok test the mention legal page return a 200 successful http request
    def test_termes_status_name(self):
        response=self.client.get('/termes/')
        self.assertEqual(response.status_code, 200)

    # ok testing url return a 200 successful http request
    def test_termes_url_name(self):
        response=self.client.get(reverse('termes'))
        self.assertEqual(response.status_code, 200)


class IndexTestCase(SimpleTestCase):  # done

    # ok test the index page return a 200 successful http request
    def test_index_status_name(self):
        response=self.client.get('/termes/')
        self.assertEqual(response.status_code, 200)

    # ok testing url return a 200 successful http request
    def test_index_url_name(self):
        response=self.client.get(reverse('termes'))
        self.assertEqual(response.status_code, 200)


class SearchTestCase(TestCase):
    category=None

    @classmethod
    def setUpTestData(cls):
        """setUpTestData() is called once at the start of the test run for class-level tuning. You can use it to
        create objects that are not meant to be modified or changed in test methods. """

        cls.user=get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret",
            # user_id='1',
        )

        cls.category=Category.objects.create(
            name="fake_category",
        )

        cls.product=Product.objects.create(
            id='558',
            name='fake_product',
            category=cls.category,
        )

        cls.userproduct=UserProduct.objects.create(
            product_id='558',
            user_id='1',
        )

        # Create 9 products for pagination test
        number_of_products=9

        for product_id in range(number_of_products):
            Product.objects.create(
                name=f'Fake_product {id}',
            )

    # ok
    def test_search_correct_template(self):
        response=self.client.get('/search/', {'search': 'fake_product'})
        self.assertTemplateUsed(response, "search.html")

    # ok
    def test_search_status_name(self):
        # test the search page return a 200 successful http request
        response=self.client.get('/search/', {'search': 'fake_product'})
        self.assertEqual(response.status_code, 200)

    # ok testing url return a 200 successful http request
    def test_search_url_name(self):
        response=self.client.get(reverse('search'), {'search': 'fake_product'})
        self.assertEqual(response.status_code, 200)

    # ok test will return something when you type category that does exist in the database
    def test_existing_product_if_found(self):
        response=self.client.get('/search/', {'search': 'fake_product'})
        self.assertContains(response, 'fake_product')

    # ok test that it will not return anything when you type product that doesn't exist in the DB
    def test_non_existing_product_if_found(self):
        response=self.client.get('/search/', {'search': 'Toto'})
        self.assertNotContains(response, 'fake_product')

    # ok
    def test_existing_category_if_found(self):
        response=self.client.get('/search/', {'search': 'fake_category'})
        self.assertEquals(response.request["QUERY_STRING"], "search=fake_category")
        self.assertEquals(response.status_code, 200)

    # ok
    def test_non_existing_category_if_found(self):
        response=self.client.get('/search/', {'search': 'toto'})
        self.assertNotEquals(response.request["QUERY_STRING"], "search=fake_category")
        self.assertEquals(response.status_code, 200)

    # ok
    def test_pagination_is_six(self):
        response=self.client.get(reverse('search'), {'search': 'fake_product'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['paginate'] == True)
        self.assertTrue(len(response.context['products']) == 6)

    # ok
    def test_detail(self):
        response=self.client.get(reverse('detail', args=(self.product.pk,)))
        no_response=self.client.get("/detail/557")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fake_product")
        self.assertTemplateUsed(response, "detail.html")
        self.assertEqual(no_response.status_code, 404)

    # ok
    def test_save(self):
        # Verify that an user can save a product as favourite.
        # If product is saved, the result page must redirect to favorite page,
        # and a new instance is created in UserProduct model with user and product ids.
        self.client.login(username="testuser", email="test@email.com", password="secret")
        response=self.client.get(reverse('save', args=(self.product.pk,)))
        self.assertEqual(response.status_code, 301)
        self.assertTrue(UserProduct.objects.get(pk=1))

    # ok redirect to index
    def test_favorite_if_not_login_user(self):
        response=self.client.get(reverse("favorite"))
        self.assertEqual(response.status_code, 302)

    # ok
    def test_favorite_for_logged_in_user(self):
        self.client.login(username="testuser", email="test@email.com", password="secret")
        response=self.client.get(reverse("favorite"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.userproduct.id)
        self.assertTemplateUsed(response, 'favorite.html')

    # ok
    def test_remove_favorite_for_logged_in_user(self):
        self.client.login(username="testuser", email="test@email.com", password="secret")
        response=self.client.get(reverse('remove', args=(self.product.pk,)))
        # The server response code 302 means the page is moved temporarily
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(UserProduct.DoesNotExist):
            UserProduct.objects.get(id=1)
