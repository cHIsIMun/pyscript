from js import console

def my_function(*args, **kwargs):
    #print('args:', args)
    #print('kwargs:', kwargs)
    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    text = Element('test-input').element.value
    #print('text:', text)
    console.log(f'text: {text}')
    Element('test-output').element.innerText += '\n' + str(text)
