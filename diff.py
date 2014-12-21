import diff_match_patch
import os

old_string = """I'm selfish, impatient and a little insecure. I make mistakes,
I am out of control and at times hard to handle. But if you can't handle me at my worst,
then you sure as hell don't deserve me at my best."""

new_string = """I'm selfish, impatient and a little secure. I don't make mistakes,
I am out of control and at times hard to handle difficult things. But if you can't handle me at my worst,
then you sure as hell don't deserve me at my best."""


diff_obj = diff_match_patch.diff_match_patch()
diffs = diff_obj.diff_main(old_string, new_string)

diff_obj.diff_cleanupSemantic(diffs)


html = diff_obj.diff_prettyHtml(diffs)

file_name="a.html";

file_path = os.path.join( "C:/Users/Rituraj/Documents/GitHub/myedit/files", file_name);
open_file = open( file_path,"w");
open_file.write(html);
open_file.close();



class SideBySideDiff(diff_match_patch.diff_match_patch):

    def old_content(self, diffs):
        """
        Returns HTML representation of 'deletions'
        """
        html = []
        for (flag, data) in diffs:
            text = (data.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\n", "<br>"))

            if flag == self.DIFF_DELETE:
                html.append("""<del style=\"background:#ffe6e6;
                    \">%s</del>""" % text)
            elif flag == self.DIFF_EQUAL:
                html.append("<span>%s</span>" % text)
        return "".join(html)

    def new_content(self, diffs):
        """
        Returns HTML representation of 'insertions'
        """
        html = []
        for (flag, data) in diffs:
            text = (data.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\n", "<br>"))
            if flag == self.DIFF_INSERT:
                html.append("""<ins style=\"background:#e6ffe6;
                    \">%s</ins>""" % text)
            elif flag == self.DIFF_EQUAL:
                html.append("<span>%s</span>" % text)
        return "".join(html)


diff_obj = SideBySideDiff()
result = diff_obj.diff_main(old_string, new_string)
diff_obj.diff_cleanupSemantic(result)

old_record = diff_obj.old_content(result) 
new_record = diff_obj.new_content(result)