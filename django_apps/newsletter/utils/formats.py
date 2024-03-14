from django.template import Template, loader


def create_template(html, context=None, components=None):
    style = loader.render_to_string('newsletter/formats/style_format.html', {"components": components})
    details = loader.render_to_string('newsletter/formats/details_format.html', {"details": html})
    context = context or {}

    formatter = {
        "details": details,
        "style": style,
    }

    rendered_template = loader.render_to_string('newsletter/formats/newsletter_formatter.html', formatter, context=context)
    return Template(rendered_template)
