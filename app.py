from flask import Flask, request
from poem_machine_crawl import gather
app = Flask(__name__)
app.config["DEBUG"] = True

# TODO
# make other texts available
# 

@app.route('/')
def poem_machine(source="dickinson"):
    poem = gather(source)
    return '''
<html>
    <head>

	<style>
		body,html{{
			padding: 0;
			margin: 0;
		}}
		ul, li {{
			padding: 0;
			margin: 0;
			list-style: none;
			text-align: left;
		}}


                .ye {{
		    padding: 5px 0;
		    list-style: none;
                    text-align: center;
                    margin: 0px auto;
                    margin-left: 0;
                }}

		.container {{
		    width: 450px;
		    height: 845px;
		    line-height: 30px;
		    border: 0px white;
                    right: 200;
		    overflow: Hidden;
		    padding: 5px 0;
		    margin: 20px auto;
                    -webkit-touch-callout: none; /* iOS Safari */
                    -webkit-user-select: none; /* Safari */
                    -khtml-user-select: none; /* Konqueror HTML */
                    -moz-user-select: none; /* Firefox */
                    -ms-user-select: none; /* Internet Explorer/Edge */
                    user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome and Opera */
		}}
	</style>
    </head>

    <body>
        <br>
        <div class="ye">
        <ye>Poem-Machine is now processing: <u><i>Dickinson's Poems</i></u></ye>
        </div>
	<div class="container">
		<ul>
			<li>&nbsp</li>
			<li>{poem}</li>
			<li>&nbsp</li>
		</ul>
	</div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="static/js/scrollText/jQuery.scrollText.js"></script>
    <script type="text/javascript">
		$(function(){{
			$(".container").scrollText({{
				'duration': 8000
			}});
		}});
	</script>    
    </body>
</html>
    '''.format(poem=poem)



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
      
    return '''
<html>
    <head>

	<style>
		body,html{{
			padding: 0;
			margin: 0;
		}}

                ul, li {{
			padding: 0;
			margin: 0;
			list-style: none;
			text-align: left;
		}}

                .ye {{
		    padding: 5px 0;
		    list-style: none;
                    text-align: center;
                    margin: 0px auto;
                    margin-left: 0;
                }}

		.container {{
		    width: 450px;
		    height: 845px;
		    line-height: 30px;
		    border: 0px white;
                    right: 200;
		    overflow: Hidden;
		    padding: 5px 0;
		    margin: 20px auto;
                    -webkit-touch-callout: none; /* iOS Safari */
                    -webkit-user-select: none; /* Safari */
                    -khtml-user-select: none; /* Konqueror HTML */
                    -moz-user-select: none; /* Firefox */
                    -ms-user-select: none; /* Internet Explorer/Edge */
                    user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome and Opera */
		}}
	</style>
    </head>

    <body>
        <br>
        <div class="ye">
        <ye>Poem-Machine is now processing: <u><i>{title}</i></u></ye>
        </div>
        <div class="container">
		<ul>
			<li>&nbsp</li>
			<li>{poem}</li>
			<li>&nbsp</li>
		</ul>
	</div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="static/js/scrollText/jQuery.scrollText.js"></script>
    <script type="text/javascript">
		$(function(){{
			$(".container").scrollText({{
				'duration': 8000
			}});
		}});
	</script>    
    </body>
</html>
    '''.format(poem=poem, title=title)


if __name__ == '__main__':
    app.run()
