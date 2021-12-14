# Simple todo list

## Stack

* python(fast api)
* react

adding data through curl:

```
curl -X POST http://localhost:8000/todo -d \
'{"id": "3", "item": "Buy some testdriven courses."}' \
-H 'Content-Type: application/json'
```
