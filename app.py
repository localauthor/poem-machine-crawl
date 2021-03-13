from flask import Flask, request
from poem_machine_crawl import gather
app = Flask(__name__)

@app.route('/')
def poem_machine():
    poem = gather()
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


                ye {{
		    padding: 10px;
		    margin: 10px;
		    list-style: none;
                    text-align: right;
                }}

		.container {{
		    width: 500px;
		    height: 1000px;
		    line-height: 30px;
		    border: 1px white;
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
        <ye>Now Serving: <u><i>Dickinson's Poems</i></u></ye>
	<div class="container">
		<ul>
			<li>Begin</li>
			<li>{poem}</li>
			<li>End</li>
		</ul>
	</div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="static/js/scrollText/jQuery.scrollText.js"></script>
    <script type="text/javascript">
		$(function(){{
			$(".container").scrollText({{
				'duration': 2000
			}});
		}});
	</script>    
    </body>
</html>
    '''.format(poem=poem)

if __name__ == '__main__':
    app.run()
