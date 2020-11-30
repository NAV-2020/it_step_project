from django import forms
from .models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')

    def save(self, user, *args, **kwargs):

        print(self.data.get('title'))
        print(self.data.get('body'))
        print(self.data.get('image'))
        post = Post.objects.create(title=self.data.get('title'),
                                   body=self.data.get('body'),
                                   poster=user)
        if self.data.get('image'):
            post.image = self.data.get('image')

        return post