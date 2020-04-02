# What is a “slug” in Django?

Answer 1:

A "slug" is a way of generating a valid URL, generally using data already obtained. For instance, a slug uses the title of an article to generate a URL. I advise to generate the slug by means of a function, given the title (or another piece of data), rather than setting it manually.

An example:
```html
<title> The 46 Year Old Virgin </title>
<content> A silly comedy movie </content>
<slug> the-46-year-old-virgin </slug>
```
Now let's pretend that we have a Django model such as:
```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=40)
```
How would you reference this object with a URL and with a meaningful name? You could for instance use Article.id so the URL would look like this:
```python
www.example.com/article/23
```
Or, you might want to reference the title like this:
```python
www.example.com/article/The 46 Year Old Virgin
```
Since spaces aren't valid in URLs, they must be replaced by %20, which results in:
```python
www.example.com/article/The%2046%20Year%20Old%20Virgin
```
Both attempts are not resulting in very meaningful, easy-to-read URL. This is better:
```python
www.example.com/article/the-46-year-old-virgin
```
In this example, the-46-year-old-virgin is a slug: it is created from the title by down-casing all letters, and replacing spaces by hyphens -.

Also see the URL of this very web page for another example.

Answer 2: 

Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs. (as in Django docs)

A slug field in Django is used to store and generate valid URLs for your dynamically created web pages.

Just like the way you added this question on Stack Overflow and a dynamic page was generated and when you see in the address bar you will see your question title with "-" in place of the spaces. That's exactly the job of a slug field.

Enter image description here

The title entered by you was something like this -> What is a “slug” in Django?

On storing it into a slug field it becomes "what-is-a-slug-in-django" (see URL of this page)
