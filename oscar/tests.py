from django.test import TestCase
from .models import Profile,Post,tag
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.vanmo9 = Profile(profile_name = 'vanmo9',username='vanmo9',email='vanmowha@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.vanmo9,Profile))

    def test_save(self):
        self.vanmo9.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class PostTestClass(TestCase):
    def setUp(self):
        self.vanmo9 = Profile(image_name = 'vanmo9',username='vanmo9',email='vanmowha@gmail.com')
        self.vanmo9.save_profile()

        self.new_tag=tag(tag='testing')
        self.new_tag.save()

        self.new_post =Posts(caption="Woooow!!!!",profile=self.vanmo9)
        self.new_post.save()

        self.new_post.tag.add(self.new_tag)

    def tearDown(self):
        Profile.objects.all().delete()
        tag.objects.all().delete()
        Posts.objects.all().delete()    

    def test_posts(self):
        posts = Posts.posts()
        self.assertTrue(len(posts)>0)        