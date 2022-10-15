from talon import Module, Context, actions, settings

mod = Module()
ctx = Context()

@mod.capture(rule='({user.html_elements})')
def html_elements(m) -> str:
    return m.html_elements

@mod.capture
def create_element(m) -> str:
    "Creates a react element"

@mod.capture
def create_closed_element(m) -> str:
    "Creates a react element"

@mod.capture
def create_native_element(m) -> str:
    "Creates a react element (lower case)"

@mod.capture
def create_image(m) -> str:
    "Creates a react <img> element"

@mod.capture
def create_styled_component(m) -> str:
    "Creates a new styled component"
@mod.capture
def create_styled_wrapper(m) -> str:
    "Creates a new styled Wrapper"

# Context Stuff
@ctx.capture(rule='elm <user.text>')
def create_element(m):
    return '<' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE') + '>'

@ctx.capture(rule='closed elm <user.text>')
def create_closed_element(m):
    return '<' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE') + '  />'

@ctx.capture(rule='elm native <user.html_elements>')
def create_native_element(m):
    return '<' + actions.user.formatted_text(m.html_elements, 'PRIVATE_CAMEL_CASE') + '>'

@ctx.capture(rule='styled <user.html_elements> <user.text>')
def create_styled_component(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'const {component_name} = styled.{m.html_elements}``'


mod.list('html_elements', desc='list of all HTML elements')

ctx.lists['user.html_elements'] = {
  'div': 'div',
  'span': 'span',
  'section': 'section',
  'header': 'header',
  'footer': 'footer',
  'article': 'article',
  'aside': 'aside',
  'main': 'main',
  'break': 'br',
  'list': 'ul',
  'ordered list': 'ol',
  'list item': 'li',
  'a': 'a',
  'anchor': 'a',
  'image': 'img',
  'pe': 'p',
  'paragraph': 'p',
  'heading one': 'h1',
  'heading two': 'h2',
  'heading three': 'h3',
  'heading four': 'h4',
  'heading five': 'h5',
  'heading six': 'h6',
  'form': 'form',
  'input': 'input',
  'button': 'button',
  'text area': 'textarea',
  'select': 'select',
  'label': 'label',
  'details': 'details',
  'strong': 'strong',
  'am': 'em',
  'emphasis': 'em',
  'title': 'title',
  'table': 'table',
  'table body': 'tbody',
  'table head': 'thead',
'table row': 'tr',
'table heading': 'th',
'table cell': 'td'
}