from django import forms

from blog.models import Post

class Postform(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','body','date']

class Searchform(forms.Form):
	text = forms.CharField(max_length=1200)
	fields = ['text']


