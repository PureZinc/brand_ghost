from django.template import Template, Context, loader


def create_template(html, context=None):
    style = loader.render_to_string('newsletter/style_format.html', {})
    context = context or {}

    html_template = Template(html)
    style_template = Template(style)

    rendered_html = html_template.render(Context(context))
    rendered_style = style_template.render(Context())

    rendered_template = rendered_style + rendered_html
    return rendered_template
