title = input('Post title: ')
date = input('Post date: ')
content = input('Post content: ')
content = content.replace("\par","""</p>
		<p>""")

toAdd = """
<div class="post">
        <div class="title">"""+title+"""</div>
        <div class="date">"""+date+"""</div>
        <div class="content"> 
        	<p>"""+content+"""</p>
    	</div>
</div>"""

print(toAdd)