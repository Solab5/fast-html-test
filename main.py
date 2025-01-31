from fasthtml.common import *

def render(todo):
    tid = f'todo-{todo.id}'
    toggle = A('Toggle', hx_get=f'/toggle/{todo.id}', target_id=tid)
    return Li(
        toggle, todo.title + (' ✅' if todo.done else ''),
        id=tid)

app,rt, todos, Todo = fast_app('todos.db', live=True, render=render,
                               id=int, title=str, done=bool, pk='id')



@rt('/')
def get(): 
    return Titled('Todos', 
                 Ul(*todos()),
                )


@rt('/toggle/{tid}')
def get(tid:int):
    todo = todos['tid']
    todo.done = not todo.done
    todo.update(todo)
    return todo


serve()