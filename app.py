from flask import Flask, url_for, render_template
from poem_machine_crawl import gather
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def poem_machine(source="dickinson"):
    title = "Dickinson's Poems"
    poem = gather(source)
    return render_template('body.html', poem=poem, title=title)
    return '''
    {% block body %}
    {% endblock %}
    '''.format(poem=poem, title=title)


@app.route('/<source>')
def poem_machine_name(source="dickinson"):
    source = "{}".format(source)

    while True:
        if source == "dickinson":
            title = "Dickinson's Poems"
            break
        elif source == "thoreau":
            title = "Thoreau's Journal"
            break
        elif source == "fuller":
            title = "Fuller's Summer on the Lakes"
            break
        else:
            source = "dickinson"
            title = "Dickinson's Poems"
            break

    poem = gather(source)
    return render_template('body.html', poem=poem, title=title)
    return '''
    {% block body %}
    {% endblock %}
    '''.format(poem=poem, title=title)


if __name__ == '__main__':
    app.run()
