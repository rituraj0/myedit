import diff_match_patch
import SOAPpy
old_string = """I'm selfish, impatient and a little insecure. I make mistakes,
I am out of control and at times hard to handle. But if you can't handle me at my worst,
then you sure as hell don't deserve me at my best."""

new_string = """I'm selfish, impatient and a little secure. I don't make mistakes,
I am out of control and at times hard to handle difficult things. But if you can't handle me at my worst,
then you sure as hell don't deserve me at my best."""

diff_obj = diff_match_patch.diff_match_patch()

diffs = diff_obj.diff_main(old_string, new_string)

diff_obj.diff_cleanupSemantic(diffs)
