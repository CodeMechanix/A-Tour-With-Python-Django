# Django values_list vs values

The values() method returns a QuerySet containing dictionaries:
```python
<QuerySet [{'comment_id': 1}, {'comment_id': 2}]>
```
The values_list() method returns a QuerySet containing tuples:
```python
<QuerySet [(1,), (2,)]>
```
If you are using values_list() with a single field, you can use flat=True to return a QuerySet of single values instead of 1-tuples:
```python
<QuerySet [1, 2]>
```