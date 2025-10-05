from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Tag

class TagSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass')
        self.p1 = Post.objects.create(title='Django tips', content='Useful tips', author=self.user)
        self.p2 = Post.objects.create(title='Python news', content='Latest releases', author=self.user)
        t1 = Tag.objects.create(name='django')
        t2 = Tag.objects.create(name='python')
        self.p1.tags.add(t1)
        self.p2.tags.add(t2)

    def test_posts_by_tag(self):
        url = reverse('blog:posts-by-tag', kwargs={'tag_name': 'django'})
        resp = self.client.get(url)
        self.assertContains(resp, 'Django tips')
        self.assertNotContains(resp, 'Python news')

    def test_search_by_title(self):
        url = reverse('blog:search-results') + '?q=django'
        resp = self.client.get(url)
        self.assertContains(resp, 'Django tips')

    def test_search_by_tag(self):
        url = reverse('blog:search-results') + '?q=python'
        resp = self.client.get(url)
        self.assertContains(resp, 'Python news')
