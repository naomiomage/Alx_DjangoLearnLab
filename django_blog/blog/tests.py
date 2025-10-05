from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post, Comment

class CommentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.post = Post.objects.create(title='Test Post', content='Post content', author=self.user)
        self.client.login(username='testuser', password='pass1234')

    def test_create_comment(self):
        url = reverse('blog:comment-create', args=[self.post.id])
        data = {'content': 'Nice post!'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'Nice post!')

    def test_edit_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='Old comment')
        url = reverse('blog:comment-update', args=[comment.id])
        data = {'content': 'Updated comment'}
        response = self.client.post(url, data)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Updated comment')

    def test_delete_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='To delete')
        url = reverse('blog:comment-delete', args=[comment.id])
        response = self.client.post(url)
        self.assertEqual(Comment.objects.count(), 0)
