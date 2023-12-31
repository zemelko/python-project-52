from django import template
register = template.Library()

strformat = "%d.%m.%Y %H:%M"


@register.simple_tag
def date_format(datetime):
    return datetime.strftime(strformat)


@register.simple_tag
def concat(*fields):
    return " ".join(fields) if fields else ""
