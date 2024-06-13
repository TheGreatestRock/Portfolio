import re
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='highlight_glossary_terms')
def highlight_glossary_terms(content, glossary_terms):
    content = escape(content)
    content = content.replace('\n', '<br>')
    glossary_terms = sorted(glossary_terms, key=len, reverse=True)

    for term in glossary_terms:
        if term.strip() == '':
            continue
        pattern = r'\b{}\b'.format(re.escape(term))
        content = re.sub(pattern, lambda match: f'''<span class="hover-word" onmouseover="showPopup(this, '{match.group(0)}')" onmouseout="hidePopup()">{match.group(0)}</span>''', content, flags=re.IGNORECASE)

    return mark_safe(content)

@register.filter(name='line_breaks')
def line_breaks(content):
    content = escape(content)
    content = content.replace('\n', '<br>')

    return mark_safe(content)