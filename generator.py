# tip: you can use the ${} notations in you snippets ;3
'''
how to use
&_________NAME___HERE__________/sep;/

    ____________SIPPET_1__HERE

##sep;

&_________NAME___HERE__________/sep;/

    ____________SIPPET_2__HERE

... etc '''
import os
from tkinter import filedialog
# check # if path is not None and len(path) > 0:
    
#==================================================================================================
#=== your parameters here ==================================================================================================
#==================================================================================================

#=== files 
src_file = 'snipps.py'
dest_folder = filedialog.askdirectory(initialdir = "C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets") #'your_results_are_here'

assert os.path.exists(src_file)
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

#=== separators 
snippet_separator = '##sep;' # used to seperate between snippets
inner_seperator = '/sep;/'
marker_before_snip_name = '&'

assert marker_before_snip_name != snippet_separator
assert marker_before_snip_name != inner_seperator
assert snippet_separator != inner_seperator
#=== params 
scope = 'source.python'
#=== options



#==================================================================================================
#=== snippet structure / body ==================================================================================================
#==================================================================================================
snippet_body = '''<snippet>
<content><![CDATA[
{content}
]]></content>
<tabTrigger>{name}</tabTrigger>
<scope>{scope}</scope>
<description>{desc}</description>
</snippet>'''
#==================================================================================================
#=== Functions and classes ==================================================================================================
#==================================================================================================
class Snippet():
    def __init__(self, snip_txt):
        self.name, self.content, self.desc = Snippet.unpack_snippet_text(snip_txt)
    
    def __str__(self):
        return snippet_body.format(
        content=self.content,
        name=self.name,
        scope=scope,
        desc=self.desc)

    def unpack_snippet_text(snip_txt):
        elements = slice_N_strip(snip_txt, inner_seperator)
        assert len(elements) > 1

        if len(elements)>2:
            desc = elements[2]
        else:
            desc = ''
        name = elements[0][len(marker_before_snip_name):] #to ignore the marker before the name (get the name only)
        content = elements[1]

        return name, content, desc

def slice_N_strip(raw_text, sep = ' '):
    return list(map(lambda x : x.strip(), raw_text.split(sep)))


#==================================================================================================
#==================================================================================================


with open(src_file, 'r', encoding="utf8") as src:
    for s_txt in slice_N_strip(src.read(), snippet_separator):
        snip = Snippet(s_txt)
        with open(dest_folder+'/'+snip.name+'.sublime-snippet', 'w', encoding="utf8") as dest:
            dest.write(str(snip))